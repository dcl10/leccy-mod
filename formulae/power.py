from typing import Union


def power_dc(
    current: Union[int, float], voltage: Union[int, float]
) -> Union[int, float]:
    """Calculate the electrical power of a DC circuit.

    Args:
        current (Union[int, float]): The current of the circuit, in Amperes (A).
        voltage (Union[int, float]): The voltage of the circuit, in volts (V).

    Returns:
        Union[int, float]: The electrical power of the circuit, in Watts (W).
    """
    return current * voltage


def consumption(kilowatts: Union[int, float], hours: int) -> Union[int, float]:
    """Calculate energy consumption, in kilowatt hours (kWh).

    Args:
        kilowatts (Union[int, float]): The power used, in kilowatts (kW).
        hours (int): The number of hours the power is sustained, in hours (h)/

    Returns:
        Union[int, float]: _description_
    """
    return kilowatts * hours
