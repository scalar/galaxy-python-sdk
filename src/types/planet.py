# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .user import User

__all__ = ["Planet", "PhysicalProperties", "Temperature", "Atmosphere", "Satellite", "Orbit"]


class Orbit(BaseModel):

    planet_id: Optional[int] = FieldInfo(alias="planetId", default=None)
    """The ID of the planet this satellite orbits"""

    orbital_period: Optional[float] = FieldInfo(alias="orbitalPeriod", default=None)
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

class Atmosphere(BaseModel):

    compound: Optional[str] = None

    percentage: Optional[float] = None

class Temperature(BaseModel):

    min: Optional[float] = None
    """Minimum temperature in Kelvin"""

    max: Optional[float] = None
    """Maximum temperature in Kelvin"""

    average: Optional[float] = None
    """Average temperature in Kelvin"""

class PhysicalProperties(BaseModel):

    mass: Optional[float] = None
    """Mass in Earth masses (must be greater than 0)"""

    radius: Optional[float] = None
    """Radius in Earth radii (must be greater than 0)"""

    gravity: Optional[float] = None
    """Surface gravity in Earth g"""

    temperature: Optional[Temperature] = None



class Planet(BaseModel):
    """A planet in the Scalar Galaxy"""

    id: int

    name: str

    description: Optional[str] = None

    type: Literal["planet", "terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"]

    habitability_index: Optional[float] = FieldInfo(alias="habitabilityIndex", default=None)
    """A score from 0 to 1 indicating potential habitability"""

    physical_properties: Optional[PhysicalProperties] = FieldInfo(alias="physicalProperties", default=None)

    atmosphere: Optional[List[Atmosphere]] = None
    """Atmospheric composition"""

    discovered_at: Optional[datetime] = FieldInfo(alias="discoveredAt", default=None)

    image: Optional[str] = None

    satellites: Optional[List[Satellite]] = None

    creator: Optional[User] = None
    """A user"""

    tags: Optional[List[str]] = None

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)

    success_callback_url: Optional[str] = FieldInfo(alias="successCallbackUrl", default=None)
    """URL which gets invoked upon a successful operation"""

    failure_callback_url: Optional[str] = FieldInfo(alias="failureCallbackUrl", default=None)
    """URL which gets invoked upon a failed operation"""
