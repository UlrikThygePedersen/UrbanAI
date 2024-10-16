# Imports
import requests
import random
from swarm import Swarm, Agent
from loguru import logger

# Functions


## Traffic Light Control Functions
def get_vehicle_count(intersection_id):
    # Simulating an API call or database query to get the vehicle count at a specific intersection.
    response = requests.get(
        f"http://traffic-api.com/intersection/{intersection_id}/vehicle_count"
    )
    if response.status_code == 200:
        return response.json().get("vehicle_count", 0)
    return 0


def adjust_traffic_lights(intersection_id):
    # Get the current number of vehicles at the intersection
    vehicle_count = get_vehicle_count(intersection_id)
    # Adjust traffic light timing based on vehicle count (e.g., longer green light if there are more vehicles)
    if vehicle_count > 10:
        logger.info(
            f"At intersection {intersection_id}: Green light extended by 20 seconds."
        )
    else:
        logger.info(
            f"At intersection {intersection_id}: Green light kept at normal duration."
        )


## Public Transport Functions
def get_bus_load(bus_id):
    # Simulating checking the current number of passengers on a bus
    # This could be an API call to the bus tracking system
    return random.randint(0, 50)  # Random passenger count for simplicity


def reroute_bus(bus_id, current_traffic_conditions):
    bus_load = get_bus_load(bus_id)
    if current_traffic_conditions == "heavy":
        logger.info(
            f"Bus {bus_id} is rerouted to avoid traffic. Current load: {bus_load} passengers."
        )
    else:
        logger.info(
            f"Bus {bus_id} continues on normal route. Current load: {bus_load} passengers."
        )


## Emergency Response Functions
def get_traffic_conditions(route_id):
    # Simulating an API call to get traffic conditions on a specific route
    response = requests.get(f"http://traffic-api.com/routes/{route_id}/conditions")
    if response.status_code == 200:
        return response.json().get("traffic_conditions", "normal")
    return "unknown"


def clear_path_for_emergency(route_id):
    # Get current traffic conditions
    traffic_conditions = get_traffic_conditions(route_id)
    # Clear the path based on traffic conditions
    if traffic_conditions == "heavy":
        logger.info(
            f"Route {route_id} has heavy traffic. Adjusting traffic lights and rerouting vehicles for emergency clearance."
        )
    else:
        logger.info(f"Route {route_id} has normal traffic. No need for adjustments.")


## Pedestrian Flow Functions
def get_pedestrian_count(crosswalk_id):
    # Simulating a sensor or API call to get pedestrian count at a crosswalk
    response = requests.get(
        f"http://city-api.com/crosswalks/{crosswalk_id}/pedestrian_count"
    )
    if response.status_code == 200:
        return response.json().get("pedestrian_count", 0)
    return 0


def adjust_pedestrian_crossing(crosswalk_id):
    pedestrian_count = get_pedestrian_count(crosswalk_id)
    # Adjust the crossing signal time based on pedestrian count
    if pedestrian_count > 20:
        logger.info(f"At crosswalk {crosswalk_id}: Extending pedestrian crossing time.")
    else:
        logger.info(
            f"At crosswalk {crosswalk_id}: Keeping pedestrian crossing time at normal duration."
        )


## Coordination Functions
def monitor_city_conditions():
    # Simulate API calls to monitor the overall state of the city
    traffic_status = requests.get("http://traffic-api.com/city/traffic_status").json()
    bus_status = requests.get("http://bus-api.com/city/bus_status").json()
    emergency_status = requests.get("http://emergency-api.com/city/status").json()
    return {"traffic": traffic_status, "bus": bus_status, "emergency": emergency_status}


def coordinate_agents():
    # Get overall city conditions
    city_conditions = monitor_city_conditions()
    # Make decisions based on city-wide data
    if city_conditions["traffic"]["congestion_level"] > 80:
        logger.info(
            "High traffic congestion detected. Instructing Traffic Light Control Agent to extend green lights."
        )
    if city_conditions["emergency"]["active_incidents"] > 0:
        logger.info(
            "Emergency incidents detected. Instructing Emergency Response Agent to clear routes."
        )
