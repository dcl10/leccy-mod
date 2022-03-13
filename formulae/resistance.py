from typing import Union


def wire_resistance(
    resistivity: float, length: Union[int, float], area: Union[int, float]
) -> float:
    """Calculate the resistance of a wire based on its length, area and resistivity.

    Args:
        resistivity (float): The resistivity of the wire's material, in Ohm metres
        length (Union[int, float]): _description_
        area (Union[int, float]): _description_

    Returns:
        float: _description_
    """
    return resistivity * (length / area)
