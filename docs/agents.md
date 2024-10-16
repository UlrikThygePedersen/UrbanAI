# Agents Documentation

This document provides an overview of the agents used in the Smart City Traffic Management System.

## 1. Traffic Light Control Agent
- **Role**: Controls traffic lights to optimize vehicle flow.
- **Functions**:
  - `get_vehicle_count`: Fetches the number of vehicles at a specific intersection.
  - `adjust_traffic_lights`: Adjusts the green light time based on the vehicle count.

## 2. Public Transport Agent
- **Role**: Manages public transportation routes and schedules.
- **Functions**:
  - `get_bus_load`: Checks the load of passengers on a bus.
  - `reroute_bus`: Reroutes buses based on traffic conditions.

## 3. Emergency Response Agent
- **Role**: Clears traffic for emergency vehicles.
- **Functions**:
  - `get_traffic_conditions`: Fetches the traffic condition for a specific route.
  - `clear_path_for_emergency`: Clears a route for emergency vehicles.

## 4. Pedestrian Flow Agent
- **Role**: Controls pedestrian crossings.
- **Functions**:
  - `get_pedestrian_count`: Fetches the number of pedestrians at a crosswalk.
  - `adjust_pedestrian_crossing`: Adjusts pedestrian crossing signals.

## 5. Coordination Agent
- **Role**: Coordinates the other agents and ensures smooth operation across the city.
- **Functions**:
  - `monitor_city_conditions`: Monitors overall city conditions.
  - `coordinate_agents`: Coordinates tasks between agents.
