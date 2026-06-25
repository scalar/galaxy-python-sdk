# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import base64
import os
import threading
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Literal, Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources.planets import PlanetsResource, AsyncPlanetsResource
    from .resources.celestial_bodies import CelestialBodiesResource, AsyncCelestialBodiesResource
    from .resources.authentication import AuthenticationResource, AsyncAuthenticationResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

ENVIRONMENTS: dict[str, str] = {
    "production": "https://galaxy.scalar.com",
    "responds_with_your_request_data": "{protocol}://void.scalar.com/{path}",
}

__all__ = ["ENVIRONMENTS", "ScalarGalaxy", "AsyncScalarGalaxy", "Client", "AsyncClient", "Timeout", "Transport", "ProxiesTypes", "RequestOptions"]


class ScalarGalaxy(SyncAPIClient):
    # client options
    bearer_auth: str | None
    basic_auth_username: str | None
    basic_auth_password: str | None
    api_key_header: str | None
    api_key_query: str | None
    api_key_cookie: str | None
    o_auth2: str | None
    open_id_connect: str | None

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
        api_key_cookie: str | None = None,
        o_auth2: str | None = None,
        open_id_connect: str | None = None,
        environment: Literal["production", "responds_with_your_request_data"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        http_client: httpx.Client | None = None,
        _strict_response_validation: bool = False,
        **kwargs: Any,
    ) -> None:
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        self.bearer_auth = bearer_auth
        if basic_auth_username is None:
            basic_auth_username = os.environ.get("BASIC_AUTH_USERNAME")
        self.basic_auth_username = basic_auth_username
        if basic_auth_password is None:
            basic_auth_password = os.environ.get("BASIC_AUTH_PASSWORD")
        self.basic_auth_password = basic_auth_password
        if api_key_header is None:
            api_key_header = os.environ.get("API_KEY_HEADER")
        self.api_key_header = api_key_header
        if api_key_query is None:
            api_key_query = os.environ.get("API_KEY_QUERY")
        self.api_key_query = api_key_query
        if api_key_cookie is None:
            api_key_cookie = os.environ.get("API_KEY_COOKIE")
        self.api_key_cookie = api_key_cookie
        if o_auth2 is None:
            o_auth2 = os.environ.get("SCALAR_O_AUTH2")
        self.o_auth2 = o_auth2
        if open_id_connect is None:
            open_id_connect = os.environ.get("SCALAR_OPEN_ID_CONNECT")
        self.open_id_connect = open_id_connect
        self._environment = environment
        base_url_env = os.environ.get("SCALAR_BASE_URL")
        if is_given(base_url) and base_url is not None:
            if is_given(environment):
                raise ValueError(
                    "Ambiguous URL; the `base_url` and `environment` arguments are both set. Pass `base_url=None` to use the environment.",
                )
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; the base URL environment variable and the `environment` argument are both set. Pass base_url=None to use the environment.",
                )
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        # Extra keyword args flow through `with_options(_extra_kwargs=...)` to the default HTTPX client.
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
            **kwargs,
        )
        self._idempotency_header = "Idempotency-Key"
        self._default_stream_cls = Stream
        self._streaming_handlers: list[dict[str, object]] = []

    @cached_property
    def planets(self) -> "PlanetsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import PlanetsResource
        return PlanetsResource(self)

    @cached_property
    def celestial_bodies(self) -> "CelestialBodiesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import CelestialBodiesResource
        return CelestialBodiesResource(self)

    @cached_property
    def authentication(self) -> "AuthenticationResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResource
        return AuthenticationResource(self)

    @cached_property
    def webhooks(self) -> "WebhooksResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import WebhooksResource
        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> ScalarGalaxyWithRawResponse:
        return ScalarGalaxyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScalarGalaxyWithStreamingResponse:
        return ScalarGalaxyWithStreamingResponse(self)

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
        api_key_cookie: str | None = None,
        o_auth2: str | None = None,
        open_id_connect: str | None = None,
        environment: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] | None = None,
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        copied_base_url = base_url if base_url is not None else self.base_url
        # Environment overrides must resolve their own URL instead of reusing this client's host.
        if environment is not None and base_url is None:
            copied_base_url = None
        return self.__class__(
            bearer_auth=bearer_auth if bearer_auth is not None else self.bearer_auth,
            basic_auth_username=basic_auth_username if basic_auth_username is not None else self.basic_auth_username,
            basic_auth_password=basic_auth_password if basic_auth_password is not None else self.basic_auth_password,
            api_key_header=api_key_header if api_key_header is not None else self.api_key_header,
            api_key_query=api_key_query if api_key_query is not None else self.api_key_query,
            api_key_cookie=api_key_cookie if api_key_cookie is not None else self.api_key_cookie,
            o_auth2=o_auth2 if o_auth2 is not None else self.o_auth2,
            open_id_connect=open_id_connect if open_id_connect is not None else self.open_id_connect,
            environment=environment if environment is not None else self._environment,
            base_url=copied_base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **(_extra_kwargs or {}),
        )

    with_options = copy

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @override
    def _auth_headers(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._basic_auth_header_auth,
            **self._bearer_auth_header_auth,
            **self._api_key_header_header_auth,
            **self._o_auth2_header_auth,
            **self._open_id_connect_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_query_query_auth,
        }

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_cookie_cookie_auth,
        }

    @property
    def _basic_auth_header_auth(self) -> dict[str, str]:
        username = self.basic_auth_username
        password = self.basic_auth_password
        if username is None or password is None:
            return {}
        value = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        return {"Authorization": f"Basic {value}"}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_header_header_auth(self) -> dict[str, str]:
        value = self.api_key_header
        if value is None:
            return {}
        return {"X-API-Key": value}

    @property
    def _o_auth2_header_auth(self) -> dict[str, str]:
        value = self.o_auth2
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _open_id_connect_header_auth(self) -> dict[str, str]:
        value = self.open_id_connect
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_query_query_auth(self) -> dict[str, str]:
        value = self.api_key_query
        if value is None:
            return {}
        return {"api_key": value}

    @property
    def _api_key_cookie_cookie_auth(self) -> dict[str, str]:
        value = self.api_key_cookie
        if value is None:
            return {}
        return {"api_key": value}


    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        if headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return
        if params.get("api_key") is not None:
            return
        if cookies.get("api_key") is not None:
            return
        raise TypeError("Could not resolve authentication method. Expected Authorization or X-API-Key or query api_key or cookie api_key to be set.")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncScalarGalaxy(AsyncAPIClient):
    # client options
    bearer_auth: str | None
    basic_auth_username: str | None
    basic_auth_password: str | None
    api_key_header: str | None
    api_key_query: str | None
    api_key_cookie: str | None
    o_auth2: str | None
    open_id_connect: str | None

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
        api_key_cookie: str | None = None,
        o_auth2: str | None = None,
        open_id_connect: str | None = None,
        environment: Literal["production", "responds_with_your_request_data"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        http_client: httpx.AsyncClient | None = None,
        _strict_response_validation: bool = False,
        **kwargs: Any,
    ) -> None:
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        self.bearer_auth = bearer_auth
        if basic_auth_username is None:
            basic_auth_username = os.environ.get("BASIC_AUTH_USERNAME")
        self.basic_auth_username = basic_auth_username
        if basic_auth_password is None:
            basic_auth_password = os.environ.get("BASIC_AUTH_PASSWORD")
        self.basic_auth_password = basic_auth_password
        if api_key_header is None:
            api_key_header = os.environ.get("API_KEY_HEADER")
        self.api_key_header = api_key_header
        if api_key_query is None:
            api_key_query = os.environ.get("API_KEY_QUERY")
        self.api_key_query = api_key_query
        if api_key_cookie is None:
            api_key_cookie = os.environ.get("API_KEY_COOKIE")
        self.api_key_cookie = api_key_cookie
        if o_auth2 is None:
            o_auth2 = os.environ.get("SCALAR_O_AUTH2")
        self.o_auth2 = o_auth2
        if open_id_connect is None:
            open_id_connect = os.environ.get("SCALAR_OPEN_ID_CONNECT")
        self.open_id_connect = open_id_connect
        self._environment = environment
        base_url_env = os.environ.get("SCALAR_BASE_URL")
        if is_given(base_url) and base_url is not None:
            if is_given(environment):
                raise ValueError(
                    "Ambiguous URL; the `base_url` and `environment` arguments are both set. Pass `base_url=None` to use the environment.",
                )
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; the base URL environment variable and the `environment` argument are both set. Pass base_url=None to use the environment.",
                )
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        # Extra keyword args flow through `with_options(_extra_kwargs=...)` to the default HTTPX client.
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
            **kwargs,
        )
        self._idempotency_header = "Idempotency-Key"
        self._default_stream_cls = AsyncStream
        self._streaming_handlers: list[dict[str, object]] = []

    @cached_property
    def planets(self) -> "AsyncPlanetsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import AsyncPlanetsResource
        return AsyncPlanetsResource(self)

    @cached_property
    def celestial_bodies(self) -> "AsyncCelestialBodiesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import AsyncCelestialBodiesResource
        return AsyncCelestialBodiesResource(self)

    @cached_property
    def authentication(self) -> "AsyncAuthenticationResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResource
        return AsyncAuthenticationResource(self)

    @cached_property
    def webhooks(self) -> "AsyncWebhooksResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import AsyncWebhooksResource
        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncScalarGalaxyWithRawResponse:
        return AsyncScalarGalaxyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScalarGalaxyWithStreamingResponse:
        return AsyncScalarGalaxyWithStreamingResponse(self)

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
        api_key_cookie: str | None = None,
        o_auth2: str | None = None,
        open_id_connect: str | None = None,
        environment: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] | None = None,
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        copied_base_url = base_url if base_url is not None else self.base_url
        # Environment overrides must resolve their own URL instead of reusing this client's host.
        if environment is not None and base_url is None:
            copied_base_url = None
        return self.__class__(
            bearer_auth=bearer_auth if bearer_auth is not None else self.bearer_auth,
            basic_auth_username=basic_auth_username if basic_auth_username is not None else self.basic_auth_username,
            basic_auth_password=basic_auth_password if basic_auth_password is not None else self.basic_auth_password,
            api_key_header=api_key_header if api_key_header is not None else self.api_key_header,
            api_key_query=api_key_query if api_key_query is not None else self.api_key_query,
            api_key_cookie=api_key_cookie if api_key_cookie is not None else self.api_key_cookie,
            o_auth2=o_auth2 if o_auth2 is not None else self.o_auth2,
            open_id_connect=open_id_connect if open_id_connect is not None else self.open_id_connect,
            environment=environment if environment is not None else self._environment,
            base_url=copied_base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **(_extra_kwargs or {}),
        )

    with_options = copy

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @override
    def _auth_headers(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._basic_auth_header_auth,
            **self._bearer_auth_header_auth,
            **self._api_key_header_header_auth,
            **self._o_auth2_header_auth,
            **self._open_id_connect_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_query_query_auth,
        }

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_cookie_cookie_auth,
        }

    @property
    def _basic_auth_header_auth(self) -> dict[str, str]:
        username = self.basic_auth_username
        password = self.basic_auth_password
        if username is None or password is None:
            return {}
        value = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        return {"Authorization": f"Basic {value}"}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_header_header_auth(self) -> dict[str, str]:
        value = self.api_key_header
        if value is None:
            return {}
        return {"X-API-Key": value}

    @property
    def _o_auth2_header_auth(self) -> dict[str, str]:
        value = self.o_auth2
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _open_id_connect_header_auth(self) -> dict[str, str]:
        value = self.open_id_connect
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_query_query_auth(self) -> dict[str, str]:
        value = self.api_key_query
        if value is None:
            return {}
        return {"api_key": value}

    @property
    def _api_key_cookie_cookie_auth(self) -> dict[str, str]:
        value = self.api_key_cookie
        if value is None:
            return {}
        return {"api_key": value}


    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        if headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return
        if params.get("api_key") is not None:
            return
        if cookies.get("api_key") is not None:
            return
        raise TypeError("Could not resolve authentication method. Expected Authorization or X-API-Key or query api_key or cookie api_key to be set.")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ScalarGalaxyWithRawResponse:
    def __init__(self, client: ScalarGalaxy) -> None:
        self._client = client

    @cached_property
    def planets(self) -> "PlanetsResourceWithRawResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import PlanetsResourceWithRawResponse
        return PlanetsResourceWithRawResponse(self._client.planets)

    @cached_property
    def celestial_bodies(self) -> "CelestialBodiesResourceWithRawResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import CelestialBodiesResourceWithRawResponse
        return CelestialBodiesResourceWithRawResponse(self._client.celestial_bodies)

    @cached_property
    def authentication(self) -> "AuthenticationResourceWithRawResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResourceWithRawResponse
        return AuthenticationResourceWithRawResponse(self._client.authentication)

    @cached_property
    def webhooks(self) -> "WebhooksResourceWithRawResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import WebhooksResourceWithRawResponse
        return WebhooksResourceWithRawResponse(self._client.webhooks)


class AsyncScalarGalaxyWithRawResponse:
    def __init__(self, client: AsyncScalarGalaxy) -> None:
        self._client = client

    @cached_property
    def planets(self) -> "AsyncPlanetsResourceWithRawResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import AsyncPlanetsResourceWithRawResponse
        return AsyncPlanetsResourceWithRawResponse(self._client.planets)

    @cached_property
    def celestial_bodies(self) -> "AsyncCelestialBodiesResourceWithRawResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import AsyncCelestialBodiesResourceWithRawResponse
        return AsyncCelestialBodiesResourceWithRawResponse(self._client.celestial_bodies)

    @cached_property
    def authentication(self) -> "AsyncAuthenticationResourceWithRawResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResourceWithRawResponse
        return AsyncAuthenticationResourceWithRawResponse(self._client.authentication)

    @cached_property
    def webhooks(self) -> "AsyncWebhooksResourceWithRawResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import AsyncWebhooksResourceWithRawResponse
        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)


class ScalarGalaxyWithStreamingResponse:
    def __init__(self, client: ScalarGalaxy) -> None:
        self._client = client

    @cached_property
    def planets(self) -> "PlanetsResourceWithStreamingResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import PlanetsResourceWithStreamingResponse
        return PlanetsResourceWithStreamingResponse(self._client.planets)

    @cached_property
    def celestial_bodies(self) -> "CelestialBodiesResourceWithStreamingResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import CelestialBodiesResourceWithStreamingResponse
        return CelestialBodiesResourceWithStreamingResponse(self._client.celestial_bodies)

    @cached_property
    def authentication(self) -> "AuthenticationResourceWithStreamingResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResourceWithStreamingResponse
        return AuthenticationResourceWithStreamingResponse(self._client.authentication)

    @cached_property
    def webhooks(self) -> "WebhooksResourceWithStreamingResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import WebhooksResourceWithStreamingResponse
        return WebhooksResourceWithStreamingResponse(self._client.webhooks)


class AsyncScalarGalaxyWithStreamingResponse:
    def __init__(self, client: AsyncScalarGalaxy) -> None:
        self._client = client

    @cached_property
    def planets(self) -> "AsyncPlanetsResourceWithStreamingResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import AsyncPlanetsResourceWithStreamingResponse
        return AsyncPlanetsResourceWithStreamingResponse(self._client.planets)

    @cached_property
    def celestial_bodies(self) -> "AsyncCelestialBodiesResourceWithStreamingResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import AsyncCelestialBodiesResourceWithStreamingResponse
        return AsyncCelestialBodiesResourceWithStreamingResponse(self._client.celestial_bodies)

    @cached_property
    def authentication(self) -> "AsyncAuthenticationResourceWithStreamingResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResourceWithStreamingResponse
        return AsyncAuthenticationResourceWithStreamingResponse(self._client.authentication)

    @cached_property
    def webhooks(self) -> "AsyncWebhooksResourceWithStreamingResponse":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse
        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = ScalarGalaxy
AsyncClient = AsyncScalarGalaxy
