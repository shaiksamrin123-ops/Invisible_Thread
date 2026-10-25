# Invisible Thread

### Discovering Hidden Dependencies Across Essential Services

What happens when one essential service fails, and the services depending on it begin to fail too?

Invisible Thread explores the interconnected systems behind roads, healthcare facilities, and delivery networks. It aims to reveal hidden dependencies, examine cascading consequences, and help users explore alternative recommendations when disruptions occur.

## Problem Statement

Essential services rarely operate independently. A road disruption may restrict access to healthcare facilities, delay deliveries, and affect multiple connected services. These dependencies are often difficult to understand when infrastructure systems are examined separately.

Understanding how these systems interact can help identify potential consequences beyond the initial disruption.

## Proposed Solution

Invisible Thread brings infrastructure data, service relationships, and disruption scenarios into a single exploratory platform.

By combining geospatial data, network analysis, and simulated disruptions, the project enables users to investigate how a disruption in one part of a network may affect connected services and explore possible alternatives.

The core objective is to make hidden dependencies visible and provide a clearer understanding of how connected systems respond to disruptions.

## Key Features

### Infrastructure Exploration

Explore geographic data related to roads, healthcare facilities, and delivery-related services using available datasets.

### Dependency Analysis

Investigate relationships between connected services and identify dependencies that may not be immediately visible.

### Cascading Impact Analysis

Explore how an initial disruption could propagate through a network and affect downstream services.

### Alternative Recommendations

Investigate possible alternative routes, connections, or service options that may reduce the impact of a disruption.

### Disruption Simulation

Examine clearly labelled simulated scenarios alongside real-world base data to understand potential outcomes.

### Data Visualization

Use maps, visualizations, and analytical resources to make complex infrastructure relationships easier to understand.

## How It Works

1. Data Collection: Use available infrastructure and service datasets.
2. Network Construction: Represent relevant connections and dependencies.
3. Disruption Simulation: Introduce or examine a disruption scenario.
4. Impact Analysis: Explore which connected services may be affected.
5. Alternative Exploration: Investigate possible alternatives and responses.

Actual outputs depend on the available data, implemented network logic, and simulation assumptions.

## Technology Stack

The project repository includes:

- Python for backend application logic.
- HTML, CSS, and JavaScript resources for the web interface.
- Geospatial datasets, including GeoJSON files.
- CSV datasets for facility and dependency-related information.
- Network analysis resources for studying connected systems.

Exact framework versions and dependencies will be documented after verification.

## Project Structure

```text
Invisible_Thread1/
├── backend/
│   └── backend.py
├── data/
│   ├── network_analysis/
│   └── infrastructure datasets
├── web/
│   ├── assets/
│   ├── data/
│   ├── index.html
│   ├── explorer.html
│   ├── simulator.html
│   ├── insights.html
│   └── about.html
├── FINAL_DELIVERY_CHECKLIST.txt
└── README.md
```

This is a representative structure. Additional files and resources may be present in the repository.

## Data and Limitations

The project distinguishes between real-world base datasets, simulated disruptions, and analytical outputs.

Simulation results are exploratory and should not be interpreted as guaranteed predictions of real-world events or verified real-time infrastructure conditions. Results depend on dataset completeness, data freshness, model assumptions, and implementation.

## Future Scope

- Expand infrastructure coverage across additional regions of India.
- Integrate more verified public datasets.
- Improve dependency discovery and network analysis.
- Evaluate disruptions across multiple essential service sectors.
- Enhance alternative recommendation methods.
- Introduce data validation and freshness indicators.
- Evaluate model performance using realistic scenarios.

## Team

Developed collaboratively by Vandana Vajji and Samrin.

## Vision

Invisible Thread aims to encourage a connected-systems perspective when examining essential infrastructure. By making hidden dependencies and potential cascading consequences easier to explore, the project seeks to support better-informed analysis of disruptions and possible responses.

**Invisible Thread: Understanding what connects our world, and what happens when those connections are disrupted.**
