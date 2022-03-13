from typing import NamedTuple


class Material(NamedTuple):
    temp_coeff: float
    rho_0: float

    @property
    def conductivity_0(self) -> float:
        """The conductivity of the material.

        Returns:
            float: The conductivity of the material.
        """
        return 1 / self.rho_0


ALUMINIUM = Material(temp_coeff=3.9e-3, rho_0=2.65e-8)
COPPER = Material(temp_coeff=4.04e-3, rho_0=1.68e-8)
GOLD = Material(temp_coeff=3.4e-3, rho_0=2.44e-8)
IRON = Material(temp_coeff=9.7e-3, rho_0=5e-8)
LEAD = Material(temp_coeff=3.9e-3, rho_0=22e-8)
NICKEL = Material(temp_coeff=6e-3, rho_0=6.99e-8)
PLATINUM = Material(temp_coeff=3.92e-3, rho_0=10.6e-8)
SILVER = Material(temp_coeff=3.8e-3, rho_0=1.59e-8)
TUNGSTEN = Material(temp_coeff=4.5e-3, rho_0=5.6e-5)
ZINC = Material(temp_coeff=3.7e-3, rho_0=5.9e-8)
