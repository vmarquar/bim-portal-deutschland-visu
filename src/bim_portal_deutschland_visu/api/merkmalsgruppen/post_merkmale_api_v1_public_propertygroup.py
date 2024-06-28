from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.kurzinformation import Kurzinformation
from ...models.suchkriterium import Suchkriterium
from ...types import Response


def _get_kwargs(
    *,
    body: Suchkriterium,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/merkmale/api/v1/public/propertygroup",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["Kurzinformation"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Kurzinformation.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["Kurzinformation"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Suchkriterium,
) -> Response[Union[Any, List["Kurzinformation"]]]:
    """Liste von Merkmalsgruppen

     Liste aller öffentlich sichtbaren Merkmalsgruppen, welche die übermittelten Suchkriterien erfüllen

    Args:
        body (Suchkriterium):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Kurzinformation']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Suchkriterium,
) -> Optional[Union[Any, List["Kurzinformation"]]]:
    """Liste von Merkmalsgruppen

     Liste aller öffentlich sichtbaren Merkmalsgruppen, welche die übermittelten Suchkriterien erfüllen

    Args:
        body (Suchkriterium):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['Kurzinformation']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Suchkriterium,
) -> Response[Union[Any, List["Kurzinformation"]]]:
    """Liste von Merkmalsgruppen

     Liste aller öffentlich sichtbaren Merkmalsgruppen, welche die übermittelten Suchkriterien erfüllen

    Args:
        body (Suchkriterium):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Kurzinformation']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Suchkriterium,
) -> Optional[Union[Any, List["Kurzinformation"]]]:
    """Liste von Merkmalsgruppen

     Liste aller öffentlich sichtbaren Merkmalsgruppen, welche die übermittelten Suchkriterien erfüllen

    Args:
        body (Suchkriterium):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['Kurzinformation']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
