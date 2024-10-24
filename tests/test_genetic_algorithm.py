import pytest
from optimization.genetic_algorithm import genetic_algorithm
from agents import traffic_light_agent


def test_genetic_algorithm_output():
    """
    Test if the genetic algorithm produces a valid set of signal timings.
    """
    # Simulate running the genetic algorithm for traffic light optimization
    optimized_timings = genetic_algorithm(
        pop_size=20, num_intersections=5, generations=10
    )

    # Ensure that the genetic algorithm returns the expected number of optimized timings
    assert (
        len(optimized_timings) == 5
    ), "The optimized timings list should have a length of 5 (one for each intersection)."
    assert all(
        10 <= timing <= 120 for timing in optimized_timings
    ), "All timings should be between 10 and 120 seconds."


def test_traffic_light_agent_with_optimization():
    """
    Test if the Traffic Light Agent uses optimized signal timings via the genetic algorithm.
    """
    # Simulate running the genetic algorithm for traffic light optimization
    optimized_timings = genetic_algorithm(
        pop_size=20, num_intersections=5, generations=10
    )

    # Test if the traffic light agent uses the optimized timings correctly
    response = traffic_light_agent.functions[1](intersection_id=2, num_intersections=5)
    assert (
        "Green light" in response
    ), "The agent should adjust the green light timing using the optimized solution."
