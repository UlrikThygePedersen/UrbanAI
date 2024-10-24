import pytest
from agents import traffic_light_agent, public_transport_agent


def test_traffic_light_agent():
    """
    Test if the Traffic Light Agent adjusts lights correctly.
    """
    vehicle_count = 15
    response = traffic_light_agent.functions[1](
        intersection_id=12
    )  # adjust_traffic_lights
    assert (
        "Green light extended" in response
    ), "The green light should be extended based on vehicle count."


def test_public_transport_agent():
    """
    Test if the Public Transport Agent reroutes buses correctly.
    """
    bus_load = 35
    traffic_condition = "heavy"
    response = public_transport_agent.functions[1](
        bus_id=101, current_traffic_conditions=traffic_condition
    )
    assert (
        "rerouted" in response
    ), "The bus should be rerouted based on traffic conditions."
