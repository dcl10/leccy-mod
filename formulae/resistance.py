from typing import Union


def wire_resistance(
    resistivity: float, length: Union[int, float], area: Union[int, float]
) -> float:
    f"""Calculate the resistance of a wire based on its length, area and resistivity.

    Args:
        resistivity (float): The resistivity of the wire's material, in Ohm metres (\u03A9m).
        length (Union[int, float]): The length of the wire, in metres (m).
        area (Union[int, float]): The cross-sectional area of the wire, in sq. metres (m^2).

    Returns:
        float: The resistance of the wire, in Ohms (\u03A9).
    """
    return resistivity * (length / area)


def resistivity(
    resistance: Union[int, float], area: Union[int, float], length: Union[int, float]
) -> float:
    """Calculate the resistivity of the material of a wire, in Ohm metres (\u03A9m).

    Args:
        resistance (Union[int, float]): The resistance of the wire, in Ohms (\u03A9).
        area (Union[int, float]): The cross-sectional area of the wire, in sq. metres (m^2).
        length (Union[int, float]): The length of the wire, in metres (m).

    Returns:
        float: _description_
    """
    return (resistance * area) / length
