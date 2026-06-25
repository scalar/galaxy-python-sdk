# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

"""A celestial body which can be either a planet or a satellite"""

from typing import Optional, Union
from typing_extensions import Literal, TypeAlias
from .._models import BaseModel
from .planet import Planet

__all__ = ["CelestialBody", "Satellite", "Orbit"]

class Orbit(BaseModel):

    planetId: Optional[int] = None
    """The ID of the planet this satellite orbits"""

    orbitalPeriod: Optional[float] = None
    """Orbital period in Earth days"""

    distance: Optional[float] = None
    """Average distance from the planet in kilometers"""

class Satellite(BaseModel):

    id: Optional[int] = None

    name: str

    description: Optional[str] = None

    diameter: Optional[float] = None
    """Diameter in kilometers"""

    type: Literal["satellite", "moon", "asteroid", "comet"]

    orbit: Optional[Orbit] = None



CelestialBody: TypeAlias = Union[Planet, Satellite]
