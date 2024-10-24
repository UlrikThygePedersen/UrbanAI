import requests
import random
from swarm import Swarm, Agent
from loguru import logger
from optimization.genetic_algorithm import genetic_algorithm


## Traffic Light Control Functions
def get_vehicle_count(intersection_id: int) -> int:
    """
    Simulates an API call or database query to get the vehicle count at a specific intersection.

    Args:
        intersection_id (int): The ID of the intersection to query.

    Returns:
        int: The number of vehicles at the specified intersection.
    """
    response = requests.get(
        f"http://traffic-api.com/intersection/{intersection_id}/vehicle_count"
    )
    if response.status_code == 200:
        return response.json().get("vehicle_count", 0)
    return 0


def adjust_traffic_lights(intersection_id: int) -> None:
    """
    Adjusts the traffic light timings based on the vehicle count at a specific intersection.

    Args:
        intersection_id (int): The ID of the intersection to adjust the traffic lights for.

    Returns:
        None
    """
    vehicle_count = get_vehicle_count(intersection_id)
    if vehicle_count > 10:
        logger.info(
            f"At intersection {intersection_id}: Green light extended by 20 seconds."
        )
    else:
        logger.info(
            f"At intersection {intersection_id}: Green light kept at normal duration."
        )


## Public Transport Functions
def get_bus_load(bus_id: int) -> int:
    """
    Simulates checking the current number of passengers on a bus.

    Args:
        bus_id (int): The ID of the bus to check.

    Returns:
        int: The number of passengers on the bus.
    """
    return random.randint(0, 50)


def reroute_bus(bus_id: int, current_traffic_conditions: str) -> None:
    """
    Reroutes the bus if traffic conditions are heavy, otherwise continues on the normal route.

    Args:
        bus_id (int): The ID of the bus to reroute.
        current_traffic_conditions (str): The current traffic conditions (e.g., 'heavy').

    Returns:
        None
    """
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
def get_traffic_conditions(route_id: int) -> str:
    """
    Simulates an API call to get traffic conditions on a specific route.

    Args:
        route_id (int): The ID of the route to check.

    Returns:
        str: The current traffic conditions for the route.
    """
    response = requests.get(f"http://traffic-api.com/routes/{route_id}/conditions")
    if response.status_code == 200:
        return response.json().get("traffic_conditions", "normal")
    return "unknown"


def clear_path_for_emergency(route_id: int) -> None:
    """
    Clears the path for emergency vehicles by adjusting traffic lights and rerouting other vehicles.

    Args:
        route_id (int): The ID of the route that needs to be cleared.

    Returns:
        None
    """
    traffic_conditions = get_traffic_conditions(route_id)
    if traffic_conditions == "heavy":
        logger.info(
            f"Route {route_id} has heavy traffic. Adjusting traffic lights and rerouting vehicles for emergency clearance."
        )
    else:
        logger.info(f"Route {route_id} has normal traffic. No need for adjustments.")


## Pedestrian Flow Functions
def get_pedestrian_count(crosswalk_id: int) -> int:
    """
    Simulates a sensor or API call to get the pedestrian count at a crosswalk.

    Args:
        crosswalk_id (int): The ID of the crosswalk to check.

    Returns:
        int: The number of pedestrians at the crosswalk.
    """
    response = requests.get(
        f"http://city-api.com/crosswalks/{crosswalk_id}/pedestrian_count"
    )
    if response.status_code == 200:
        return response.json().get("pedestrian_count", 0)
    return 0


def adjust_pedestrian_crossing(crosswalk_id: int) -> None:
    """
    Adjusts the pedestrian crossing time based on the current pedestrian count at a crosswalk.

    Args:
        crosswalk_id (int): The ID of the crosswalk to adjust.

    Returns:
        None
    """
    pedestrian_count = get_pedestrian_count(crosswalk_id)
    if pedestrian_count > 20:
        logger.info(f"At crosswalk {crosswalk_id}: Extending pedestrian crossing time.")
    else:
        logger.info(
            f"At crosswalk {crosswalk_id}: Keeping pedestrian crossing time at normal duration."
        )


## Coordination Functions
def monitor_city_conditions() -> dict:
    """
    Simulates monitoring the overall state of the city, retrieving traffic, bus, and emergency status.

    Returns:
        dict: A dictionary containing the traffic, bus, and emergency status of the city.
    """
    traffic_status = requests.get("http://traffic-api.com/city/traffic_status").json()
    bus_status = requests.get("http://bus-api.com/city/bus_status").json()
    emergency_status = requests.get("http://emergency-api.com/city/status").json()
    return {"traffic": traffic_status, "bus": bus_status, "emergency": emergency_status}


def coordinate_agents() -> None:
    """
    Coordinates city-wide agents based on real-time data from traffic, bus, and emergency status.

    Returns:
        None
    """
    city_conditions = monitor_city_conditions()
    if city_conditions["traffic"]["congestion_level"] > 80:
        logger.info(
            "High traffic congestion detected. Instructing Traffic Light Control Agent to extend green lights."
        )
    if city_conditions["emergency"]["active_incidents"] > 0:
        logger.info(
            "Emergency incidents detected. Instructing Emergency Response Agent to clear routes."
        )


def adjust_traffic_lights_using_optimization(
    intersection_id: int, num_intersections: int = 5
) -> str:
    """
    Adjusts the traffic lights using the optimal timings generated by the genetic algorithm.

    Args:
        intersection_id (int): The intersection at which the traffic lights will be adjusted.
        num_intersections (int): The total number of intersections the algorithm will optimize for.

    Returns:
        str: A message indicating the adjusted traffic light duration for the given intersection.
    """
    optimized_timings = genetic_algorithm(
        pop_size=20, num_intersections=num_intersections, generations=50
    )

    timing = optimized_timings[intersection_id]
    if timing > 10:
        return f"At intersection {intersection_id}: Green light extended by {timing} seconds."
    else:
        return (
            f"At intersection {intersection_id}: Green light kept at normal duration."
        )
