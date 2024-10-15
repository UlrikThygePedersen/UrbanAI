from swarm import Swarm
from loguru import logger

from agents import (
    traffic_light_agent,
    public_transport_agent,
    emergency_response_agent,
    pedestrian_flow_agent,
    coordination_agent,
)

AGENT_TASK = "Check traffic at intersection 12"

# Context variables for the task
context = {
    "intersection_id": 12,  # ID of the intersection where we need to check traffic
    "bus_id": 101,  # ID of the bus at the intersection
    "route_id": 7,  # ID of the bus route
    "crosswalk_id": 5,  # ID of the crosswalk in the intersection
    "current_traffic_conditions": "heavy",  # Current traffic conditions
}

logger.info(
    f"Starting a swarm with Coordination Agent to check traffic at intersection {context['intersection_id']}.\n"
    f"Additional details: Bus ID {context['bus_id']}, Route ID {context['route_id']}, "
    f"Crosswalk ID {context['crosswalk_id']}, and current traffic conditions: {context['current_traffic_conditions']}.\n"
    f"The swarm will attempt to answer the following task: '{AGENT_TASK}'."
)

# Initialize the Swarm
client = Swarm()

# Example of conversation: Start with the coordination agent, who delegates to other agents
response = client.run(
    agent=coordination_agent,  # First Agent initialized to distribute the problem
    messages=[
        {"role": "user", "content": AGENT_TASK}
    ],  # Start the Swarm with the task given
    context_variables=context,  # Context given above
    max_turns=10,  # Limit to 10 conversational turns
    model_override="gpt-4o",  # OpenAI Model gpt-4o
    execute_tools=True,  # Allow the agents to use tools
    stream=True,  # Stream response as the agents communicate
    debug=False,  # Debug logging, turned off for normal use
)

# Print the response from the Swarm
logger.info(f"Swarm response: {response.messages[-1]['content']}")
