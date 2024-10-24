from swarm import Agent
from functions import (
    get_vehicle_count,
    adjust_traffic_lights_using_optimization,
    get_bus_load,
    reroute_bus,
    get_traffic_conditions,
    clear_path_for_emergency,
    get_pedestrian_count,
    adjust_pedestrian_crossing,
    monitor_city_conditions,
    coordinate_agents,
)

# Traffic Light Control Agent
traffic_light_agent = Agent(
    name="Traffic Light Control Agent",
    model="gpt-4o",
    instructions="You control the traffic lights in the city to optimize vehicle flow.",
    functions=[get_vehicle_count, adjust_traffic_lights_using_optimization],
    tool_choice=None,
    """
    The Traffic Light Control Agent is responsible for adjusting traffic light timings 
    across the city. It uses vehicle count data from sensors or APIs (via the 
    `get_vehicle_count` function) and applies traffic light adjustments using optimized 
    algorithms (via `adjust_traffic_lights_using_optimization`). The goal is to minimize 
    congestion and improve traffic flow.
    """
)

# Public Transport Agent
public_transport_agent = Agent(
    name="Public Transport Agent",
    model="gpt-4o",
    instructions="You manage public transportation, optimizing bus and train schedules.",
    functions=[get_bus_load, reroute_bus],
    tool_choice=None,
    """
    The Public Transport Agent is tasked with managing bus and train schedules to 
    ensure efficiency and reduce delays. It retrieves the current load of passengers 
    on buses (via `get_bus_load`) and reroutes buses if necessary based on traffic 
    conditions (via `reroute_bus`), ensuring public transportation operates smoothly.
    """
)

# Emergency Response Agent
emergency_response_agent = Agent(
    name="Emergency Response Agent",
    model="gpt-4o",
    instructions="You manage emergency responses by clearing traffic for emergency vehicles.",
    functions=[
        get_traffic_conditions,
        clear_path_for_emergency,
    ],
    tool_choice=None,
    """
    The Emergency Response Agent monitors the city's traffic conditions during 
    emergencies and clears traffic to allow emergency vehicles to navigate 
    through the city efficiently. It checks real-time traffic conditions (via 
    `get_traffic_conditions`) and reroutes vehicles as needed (via `clear_path_for_emergency`).
    """
)

# Pedestrian Flow Agent
pedestrian_flow_agent = Agent(
    name="Pedestrian Flow Agent",
    model="gpt-4o",
    instructions="You control pedestrian crossings to balance the flow of pedestrians and vehicles.",
    functions=[
        get_pedestrian_count,
        adjust_pedestrian_crossing,
    ],
    tool_choice=None,
    """
    The Pedestrian Flow Agent manages pedestrian crossings to ensure a balance between 
    pedestrian and vehicle flow. It retrieves real-time data on the number of pedestrians 
    at crosswalks (via `get_pedestrian_count`) and adjusts the timing of pedestrian 
    crossing signals accordingly (via `adjust_pedestrian_crossing`).
    """
)

# Coordination Agent
coordination_agent = Agent(
    name="Coordination Agent",
    model="gpt-4o",
    instructions="You oversee and coordinate all other agents to ensure the city runs smoothly.",
    functions=[
        monitor_city_conditions,
        coordinate_agents,
    ],
    tool_choice=None,
    """
    The Coordination Agent is responsible for overseeing the city's operations and ensuring 
    that all other agents (traffic, public transport, emergency response, and pedestrian flow) 
    are working together harmoniously. It monitors the overall city conditions (via 
    `monitor_city_conditions`) and coordinates actions across agents (via `coordinate_agents`).
    """
)
