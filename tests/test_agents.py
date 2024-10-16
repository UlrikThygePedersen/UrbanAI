import unittest
from agents import traffic_light_agent, public_transport_agent


class TestAgents(unittest.TestCase):
    def test_traffic_light_agent(self):
        # Simulate input and check if the Traffic Light Agent adjusts lights correctly
        vehicle_count = 15
        response = traffic_light_agent.functions[1](
            intersection_id=12
        )  # adjust_traffic_lights
        self.assertIn("Green light extended", response)

    def test_public_transport_agent(self):
        # Simulate input and test if the Public Transport Agent reroutes buses correctly
        bus_load = 35
        traffic_condition = "heavy"
        response = public_transport_agent.functions[1](
            bus_id=101, current_traffic_conditions=traffic_condition
        )
        self.assertIn("rerouted", response)


if __name__ == "__main__":
    unittest.main()
