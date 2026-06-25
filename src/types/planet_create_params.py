# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Annotated, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, TypedDict
from .._types import SequenceNotStr
from .user import User
from .._utils import PropertyInfo

__all__ = ["PlanetCreateParams", "PhysicalProperties", "Temperature", "Atmosphere", "Satellite", "Orbit"]


class PlanetCreateParams(TypedDict, total=False):

    name: Required[str]

    description: Optional[str]

    type: Required[Literal["planet", "terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"]]

    habitability_index: Annotated[float, PropertyInfo(alias="habitabilityIndex")]
    """A score from 0 to 1 indicating potential habitability"""

    physical_properties: Annotated[PhysicalProperties, PropertyInfo(alias="physicalProperties")]

    atmosphere: Iterable[Atmosphere]
    """Atmospheric composition"""

    discovered_at: Annotated[datetime, PropertyInfo(alias="discoveredAt")]

    image: Optional[str]

    satellites: Iterable[Satellite]

    creator: User
    """A user"""

    tags: SequenceNotStr[str]

    success_callback_url: Annotated[str, PropertyInfo(alias="successCallbackUrl")]
    """URL which gets invoked upon a successful operation"""

    failure_callback_url: Annotated[str, PropertyInfo(alias="failureCallbackUrl")]
    """URL which gets invoked upon a failed operation"""


class Orbit(TypedDict, total=False):

    planet_id: int
    """The ID of the planet this satellite orbits"""

    orbital_period: float
    """Orbital period in Earth days"""

    distance: float
    """Average distance from the planet in kilometers"""

class Satellite(TypedDict, total=False):

    name: Required[str]

    description: Optional[str]

    diameter: float
    """Diameter in kilometers"""

    type: Required[Literal["satellite", "moon", "asteroid", "comet"]]

    orbit: Orbit

class Atmosphere(TypedDict, total=False):

    compound: str

    percentage: float

class Temperature(TypedDict, total=False):

    min: float
    """Minimum temperature in Kelvin"""

    max: float
    """Maximum temperature in Kelvin"""

    average: float
    """Average temperature in Kelvin"""

class PhysicalProperties(TypedDict, total=False):

    mass: float
    """Mass in Earth masses (must be greater than 0)"""

    radius: float
    """Radius in Earth radii (must be greater than 0)"""

    gravity: float
    """Surface gravity in Earth g"""

    temperature: Temperature

