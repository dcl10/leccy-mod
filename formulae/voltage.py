from typing import Union


def voltage(current: Union[int, float], resistance: Union[int, float]) -> float:
    """Calculate the current, in Amperes (A), based on Ohm's law.

    Args:
        current (Union[int, float]): The current, in Amperes (A).
        resistance (Union[int, float]): The resistance, in Ohms (\u03A9).

    Returns:
        float: The voltage, in volts (V).
    """
    return current * resistance
