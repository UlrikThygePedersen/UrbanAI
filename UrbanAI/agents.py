# Imports
from swarm import Agent
from functions import (
    get_vehicle_count,
    adjust_traffic_lights,
    get_bus_load,
    reroute_bus,
    get_traffic_conditions,
    clear_path_for_emergency,
    get_pedestrian_count,
    adjust_pedestrian_crossing,
    monitor_city_conditions,
    coordinate_agents,
)


traffic_light_agent = Agent(
    name="Traffic Light Control Agent",
    model="gpt-4o",
    instructions="You control the traffic lights in the city to optimize vehicle flow.",
    functions=[get_vehicle_count, adjust_traffic_lights],
    tool_choice=None,
)

public_transport_agent = Agent(
    name="Public Transport Agent",
    model="gpt-4o",
    instructions="You manage public transportation, optimizing bus and train schedules.",
    functions=[get_bus_load, reroute_bus],
    tool_choice=None,
)

emergency_response_agent = Agent(
    name="Emergency Response Agent",
    model="gpt-4o",
    instructions="You manage emergency responses by clearing traffic for emergency vehicles.",
    functions=[
        get_traffic_conditions,
        clear_path_for_emergency,
    ],
    tool_choice=None,
)

pedestrian_flow_agent = Agent(
    name="Pedestrian Flow Agent",
    model="gpt-4o",
    instructions="You control pedestrian crossings to balance the flow of pedestrians and vehicles.",
    functions=[
        get_pedestrian_count,
        adjust_pedestrian_crossing,
    ],
    tool_choice=None,
)

coordination_agent = Agent(
    name="Coordination Agent",
    model="gpt-4o",
    instructions="You oversee and coordinate all other agents to ensure the city runs smoothly.",
    functions=[
        monitor_city_conditions,
        coordinate_agents,
    ],
    tool_choice=None,
)
