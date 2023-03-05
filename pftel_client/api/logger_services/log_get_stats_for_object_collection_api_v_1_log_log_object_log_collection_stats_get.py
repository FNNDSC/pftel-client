from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.log_get_stats_for_object_collection_api_v1_log_log_object_log_collection_stats_get_response_log_getstatsforobjectcollection_api_v1_log_logobject_logcollection_stats_get import (
    LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    log_object: str,
    log_collection: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = "execTime",
) -> Dict[str, Any]:
    url = "{}/api/v1/log/{logObject}/{logCollection}/stats".format(
        client.base_url, logObject=log_object, logCollection=log_collection
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[
    Union[
        HTTPValidationError,
        LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet.from_dict(
            response.json()
        )

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[
    Union[
        HTTPValidationError,
        LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    log_object: str,
    log_collection: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = "execTime",
) -> Response[
    Union[
        HTTPValidationError,
        LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet,
    ]
]:
    """
        GET stats on the specified log object collection. The column to
        process is specified in the optional query parameter.


     Description
    -----------
    GET statistics on all the events in the collection `logCollection` of
    the object `logObject`.

    The URL query `key=<key>` specifies the actual key field in the event
    collection to process. This field key must contain numeric values.

    Args:
        log_object (str):
        log_collection (str):
        key (Union[Unset, None, str]):  Default: 'execTime'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet]]
    """

    kwargs = _get_kwargs(
        log_object=log_object,
        log_collection=log_collection,
        client=client,
        key=key,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    log_object: str,
    log_collection: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = "execTime",
) -> Optional[
    Union[
        HTTPValidationError,
        LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet,
    ]
]:
    """
        GET stats on the specified log object collection. The column to
        process is specified in the optional query parameter.


     Description
    -----------
    GET statistics on all the events in the collection `logCollection` of
    the object `logObject`.

    The URL query `key=<key>` specifies the actual key field in the event
    collection to process. This field key must contain numeric values.

    Args:
        log_object (str):
        log_collection (str):
        key (Union[Unset, None, str]):  Default: 'execTime'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet]]
    """

    return sync_detailed(
        log_object=log_object,
        log_collection=log_collection,
        client=client,
        key=key,
    ).parsed


async def asyncio_detailed(
    log_object: str,
    log_collection: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = "execTime",
) -> Response[
    Union[
        HTTPValidationError,
        LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet,
    ]
]:
    """
        GET stats on the specified log object collection. The column to
        process is specified in the optional query parameter.


     Description
    -----------
    GET statistics on all the events in the collection `logCollection` of
    the object `logObject`.

    The URL query `key=<key>` specifies the actual key field in the event
    collection to process. This field key must contain numeric values.

    Args:
        log_object (str):
        log_collection (str):
        key (Union[Unset, None, str]):  Default: 'execTime'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet]]
    """

    kwargs = _get_kwargs(
        log_object=log_object,
        log_collection=log_collection,
        client=client,
        key=key,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    log_object: str,
    log_collection: str,
    *,
    client: Client,
    key: Union[Unset, None, str] = "execTime",
) -> Optional[
    Union[
        HTTPValidationError,
        LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet,
    ]
]:
    """
        GET stats on the specified log object collection. The column to
        process is specified in the optional query parameter.


     Description
    -----------
    GET statistics on all the events in the collection `logCollection` of
    the object `logObject`.

    The URL query `key=<key>` specifies the actual key field in the event
    collection to process. This field key must contain numeric values.

    Args:
        log_object (str):
        log_collection (str):
        key (Union[Unset, None, str]):  Default: 'execTime'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, LogGetStatsForObjectCollectionApiV1LogLogObjectLogCollectionStatsGetResponseLogGetstatsforobjectcollectionApiV1LogLogobjectLogcollectionStatsGet]]
    """

    return (
        await asyncio_detailed(
            log_object=log_object,
            log_collection=log_collection,
            client=client,
            key=key,
        )
    ).parsed
