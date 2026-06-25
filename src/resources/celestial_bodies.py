# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.celestial_body_create_response import CelestialBodyCreateResponse
from ..types.celestial_body import CelestialBody
from ..types import celestial_body_create_params

__all__ = ["CelestialBodiesResource", "AsyncCelestialBodiesResource"]


class CelestialBodiesResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> CelestialBodiesResourceWithRawResponse:
        return CelestialBodiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CelestialBodiesResourceWithStreamingResponse:
        return CelestialBodiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CelestialBodyCreateResponse:
        """Create a celestial body"""
        return self._post(
            "/celestial-bodies",
            body=body,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=CelestialBodyCreateResponse,
        )


class AsyncCelestialBodiesResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncCelestialBodiesResourceWithRawResponse:
        return AsyncCelestialBodiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCelestialBodiesResourceWithStreamingResponse:
        return AsyncCelestialBodiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CelestialBodyCreateResponse:
        """Create a celestial body"""
        return await self._post(
            "/celestial-bodies",
            body=body,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, idempotency_key=idempotency_key),
            cast_to=CelestialBodyCreateResponse,
        )


class CelestialBodiesResourceWithRawResponse:
    def __init__(self, celestial_bodies: CelestialBodiesResource) -> None:
        self._celestial_bodies = celestial_bodies

        self.create = to_raw_response_wrapper(
            celestial_bodies.create,
        )


class AsyncCelestialBodiesResourceWithRawResponse:
    def __init__(self, celestial_bodies: AsyncCelestialBodiesResource) -> None:
        self._celestial_bodies = celestial_bodies

        self.create = async_to_raw_response_wrapper(
            celestial_bodies.create,
        )


class CelestialBodiesResourceWithStreamingResponse:
    def __init__(self, celestial_bodies: CelestialBodiesResource) -> None:
        self._celestial_bodies = celestial_bodies

        self.create = to_streamed_response_wrapper(
            celestial_bodies.create,
        )


class AsyncCelestialBodiesResourceWithStreamingResponse:
    def __init__(self, celestial_bodies: AsyncCelestialBodiesResource) -> None:
        self._celestial_bodies = celestial_bodies

        self.create = async_to_streamed_response_wrapper(
            celestial_bodies.create,
        )
