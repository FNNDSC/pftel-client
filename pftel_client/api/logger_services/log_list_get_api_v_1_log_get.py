from http import HTTPStatus
from typing import Any, Dict, List, Optional, cast

import httpx

from ... import errors
from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/log/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List[Any]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[Any], response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List[Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[List[Any]]:
    """
        GET the list of configured log element objects


     Description
    -----------
    GET the list of configured log element objects handlers.
    These objects constitute the most general level of log aggregation.
    At this level, each handler can be thought of as a handler for a
    large group of logging collections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Any]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Optional[List[Any]]:
    """
        GET the list of configured log element objects


     Description
    -----------
    GET the list of configured log element objects handlers.
    These objects constitute the most general level of log aggregation.
    At this level, each handler can be thought of as a handler for a
    large group of logging collections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Any]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[List[Any]]:
    """
        GET the list of configured log element objects


     Description
    -----------
    GET the list of configured log element objects handlers.
    These objects constitute the most general level of log aggregation.
    At this level, each handler can be thought of as a handler for a
    large group of logging collections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Any]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[List[Any]]:
    """
        GET the list of configured log element objects


     Description
    -----------
    GET the list of configured log element objects handlers.
    These objects constitute the most general level of log aggregation.
    At this level, each handler can be thought of as a handler for a
    large group of logging collections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[Any]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
