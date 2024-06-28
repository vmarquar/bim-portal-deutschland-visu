from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organisation import Organisation
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/infrastruktur/api/v1/public/organisation",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["Organisation"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Organisation.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["Organisation"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, List["Organisation"]]]:
    """Liste aller Organisationen

     Diese Anfrage generiert eine Liste aller Organisationen, deren Informationen über die REST-API
    abgerufen werden können. Hierfür ist eine Freischaltung der Organisationen für den öffentlichen
    Zugriff per REST-API im Portal notwendig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Organisation']]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, List["Organisation"]]]:
    """Liste aller Organisationen

     Diese Anfrage generiert eine Liste aller Organisationen, deren Informationen über die REST-API
    abgerufen werden können. Hierfür ist eine Freischaltung der Organisationen für den öffentlichen
    Zugriff per REST-API im Portal notwendig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['Organisation']]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, List["Organisation"]]]:
    """Liste aller Organisationen

     Diese Anfrage generiert eine Liste aller Organisationen, deren Informationen über die REST-API
    abgerufen werden können. Hierfür ist eine Freischaltung der Organisationen für den öffentlichen
    Zugriff per REST-API im Portal notwendig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Organisation']]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, List["Organisation"]]]:
    """Liste aller Organisationen

     Diese Anfrage generiert eine Liste aller Organisationen, deren Informationen über die REST-API
    abgerufen werden können. Hierfür ist eine Freischaltung der Organisationen für den öffentlichen
    Zugriff per REST-API im Portal notwendig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['Organisation']]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed