# File generated from our OpenAPI spec by Scalar. See README.md for details.


from .._models import BaseModel

__all__ = ["Credentials"]


class Credentials(BaseModel):
    """Credentials to authenticate a user"""

    email: str
