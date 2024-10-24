import pytest
from functions import get_vehicle_count, adjust_traffic_lights


def test_get_vehicle_count():
    """
    Test that get_vehicle_count returns an integer.
    """
    vehicle_count = get_vehicle_count(12)
    assert isinstance(vehicle_count, int), "Vehicle count should be an integer"


def test_adjust_traffic_lights():
    """
    Test that adjust_traffic_lights includes 'Green light' in its result.
    """
    result = adjust_traffic_lights(12)
    assert "Green light" in result, "Response should include 'Green light'"
