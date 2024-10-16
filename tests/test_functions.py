import unittest
from functions import get_vehicle_count, adjust_traffic_lights


class TestFunctions(unittest.TestCase):
    def test_get_vehicle_count(self):
        # Test the vehicle count retrieval function
        vehicle_count = get_vehicle_count(12)
        self.assertIsInstance(vehicle_count, int)

    def test_adjust_traffic_lights(self):
        # Test that traffic lights adjust based on vehicle count
        result = adjust_traffic_lights(12)
        self.assertIn("Green light", result)


if __name__ == "__main__":
    unittest.main()
