# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import TypeAlias
from .._models import BaseModel

__all__ = ["PlanetUploadImageResponse", "PlanetUploadImageResponse"]

class PlanetUploadImageResponse(BaseModel):

    message: Optional[str] = None

    imageUrl: Optional[str] = None
    """The URL where the uploaded image can be accessed"""

    uploadedAt: Optional[datetime] = None
    """Timestamp when the image was uploaded"""

    fileSize: Optional[int] = None
    """Size of the uploaded image in bytes"""

    mimeType: Optional[str] = None
    """The content type of the uploaded image"""



PlanetUploadImageResponse: TypeAlias = PlanetUploadImageResponse
