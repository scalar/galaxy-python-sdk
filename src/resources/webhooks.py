# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Mapping

from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource

import base64
import hashlib
import hmac
import json

from typing import Mapping

_SIGNATURE_HEADER = "webhook-signature"
_TIMESTAMP_HEADER = None
_SIGNATURE_HASH = "sha256"


def _header(headers: Mapping[str, str], name: str) -> str | None:
    lower = name.lower()
    for key, value in headers.items():
        if key.lower() == lower:
            return value
    return None


def _signature_candidates(value: str) -> set[str]:
    candidates = {value.strip()}
    for part in value.replace(";", ",").split(","):
        candidate = part.strip()
        if "=" in candidate:
            candidate = candidate.split("=", 1)[1].strip()
        if candidate:
            candidates.add(candidate)
    return candidates


def _verify_signature(payload: str, headers: Mapping[str, str], key: str | bytes) -> None:
    signature = _header(headers, _SIGNATURE_HEADER)
    if not signature:
        raise ValueError(f"Missing webhook signature header: {_SIGNATURE_HEADER}")
    timestamp = _header(headers, _TIMESTAMP_HEADER) if _TIMESTAMP_HEADER else None
    signed_payload = f"{timestamp}.{payload}" if timestamp else payload
    secret = key if isinstance(key, bytes) else key.encode("utf-8")
    digest = hmac.new(secret, signed_payload.encode("utf-8"), getattr(hashlib, _SIGNATURE_HASH)).digest()
    expected = {
        hmac.new(secret, signed_payload.encode("utf-8"), getattr(hashlib, _SIGNATURE_HASH)).hexdigest(),
        base64.b64encode(digest).decode("ascii"),
    }
    if not any(
        hmac.compare_digest(candidate, allowed)
        for candidate in _signature_candidates(signature)
        for allowed in expected
    ):
        raise ValueError("Invalid webhook signature")


def _parse_payload(payload: str) -> object:
    return json.loads(payload)


__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self)

    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> object:
        if key is not None:
            _verify_signature(payload, headers, key)
        return _parse_payload(payload)

    def unsafe_unwrap(self, payload: str) -> object:
        return _parse_payload(payload)


class AsyncWebhooksResource(AsyncAPIResource):

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> object:
        if key is not None:
            _verify_signature(payload, headers, key)
        return _parse_payload(payload)

    async def unsafe_unwrap(self, payload: str) -> object:
        return _parse_payload(payload)


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

    def unwrap(self, *args: object, **kwargs: object) -> object:
        return self._webhooks.unwrap(*args, **kwargs)

    def unsafe_unwrap(self, *args: object, **kwargs: object) -> object:
        return self._webhooks.unsafe_unwrap(*args, **kwargs)


class WebhooksResourceWithStreamingResponse(WebhooksResourceWithRawResponse):
    pass


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

    async def unwrap(self, *args: object, **kwargs: object) -> object:
        return await self._webhooks.unwrap(*args, **kwargs)

    async def unsafe_unwrap(self, *args: object, **kwargs: object) -> object:
        return await self._webhooks.unsafe_unwrap(*args, **kwargs)


class AsyncWebhooksResourceWithStreamingResponse(AsyncWebhooksResourceWithRawResponse):
    pass
