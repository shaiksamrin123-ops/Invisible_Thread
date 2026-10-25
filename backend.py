
import json
import math
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Invisible Thread API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = Path(__file__).resolve().parent.parent / "web" / "data" / "ap_city_facilities.geojson"

with DATA_FILE.open("r", encoding="utf-8") as f:
    DATA = json.load(f)

FACILITIES = DATA.get("features", [])

class ScenarioRequest(BaseModel):
    facility_id: str = ""
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    radius_km: float = Field(default=2, gt=0, le=25)
    amenity: str = ""

def distance_km(lat1, lon1, lat2, lon2):
    r = 6371
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(min(1, math.sqrt(a)))

@app.get("/api/health")
def health():
    return {"status": "ok", "facilities_loaded": len(FACILITIES)}

@app.post("/api/scenario")
def scenario(req: ScenarioRequest):
    results = []

    for feature in FACILITIES:
        geometry = feature.get("geometry") or {}
        coords = geometry.get("coordinates") or []

        if geometry.get("type") != "Point" or len(coords) < 2:
            continue

        lon, lat = coords[0], coords[1]
        props = feature.get("properties") or {}
        fid = str(props.get("facility_id", feature.get("id", "")))

        if req.facility_id and fid == req.facility_id:
            continue

        amenity = str(props.get("amenity", ""))

        if req.amenity and amenity.lower() != req.amenity.lower():
            continue

        distance = distance_km(req.latitude, req.longitude, lat, lon)

        if distance <= req.radius_km:
            results.append({
                "facility_id": fid,
                "name": props.get("name", "Unnamed facility"),
                "city": props.get("city", "Unknown"),
                "amenity": amenity,
                "latitude": lat,
                "longitude": lon,
                "distance_km": round(distance, 3),
                "verified_dependency": False
            })

    results.sort(key=lambda x: x["distance_km"])

    return {
        "radius_km": req.radius_km,
        "count": len(results),
        "method": "straight-line distance",
        "verified_dependencies": False,
        "results": results
    }
