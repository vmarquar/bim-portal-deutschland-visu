"""A client library for accessing BIM-Portal REST-API für öffentliche Merkmale"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
