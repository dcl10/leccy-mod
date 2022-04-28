from typing import Union


def current(voltage: Union[int, float], resistance: Union[int, float]) -> float:
    """Calculate the current, in Amperes (A), based on Ohm's law.

    Args:
        voltage (Union[int, float]): The voltage, in volts (V).
        resistance (Union[int, float]): The resistance, in Ohms (\u03A9).

    Returns:
        float: The current, in Amperes (A).
    """
    return voltage / resistance
