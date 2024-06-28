# bim_portal_deutschland_visu (WIP)

This is an open source module to consume the REST API of the BIM Portal Deutschland. In the future, it will show the relationship between the properties and their associated propery-sets / name-sets (PSETs) as a graph tree.

BIM-Portal-Deutschland-Visu is also a python client library for accessing the "BIM-Portal REST-API für öffentliche Merkmale".

### Create the endpoints from the swagger / openapi documentation

The endpoint client (including documentation, typing, url requests etc.) was created automagically:

`poetry add openapi-python-client`

`openapi-python-client generate --url https://bimdeutschland.github.io/BIM-Portal-REST-API-Dokumentation/swagger.yaml`


## Example
```python
from bim_portal_deutschland_visu.models import *

from bim_portal_deutschland_visu.api.organisationen import get_infrastruktur_api_v1_public_organisation
from bim_portal_deutschland_visu.api.merkmalsgruppen import get_merkmale_api_v1_public_propertygroup_guid, post_merkmale_api_v1_public_propertygroup
from bim_portal_deutschland_visu.api.filter_ import get_merkmale_api_v1_public_filter
from bim_portal_deutschland_visu.api.merkmale import get_merkmale_api_v1_public_property_guid, post_merkmale_api_v1_public_property
from bim_portal_deutschland_visu.types import Response
from bim_portal_deutschland_visu.client import Client, AuthenticatedClient


if __name__ == "__main__":
    
    client = Client(base_url="https://via.bund.de/bim") # infrastruktur/api/v1/public/organisation

    with client as client:
        
        # 1) Access first api endpoint and get an list of Organisation classes back:
        # Hint: The Organisation must provice their pset list via the rest api. This has set up explicitly by the org (?)
        organisations: Organisation = get_infrastruktur_api_v1_public_organisation.sync(client=client)        


        # 2) Access the second API Endpoint and get a list of all Filter classes back:
        # "Merkmalsfiltergruppen" are filter possibilites on property sets (PSETs)
        # Currently, as of 28.06.2024, a property-set can be filtered by follwowing Filters: "Harmoniesierte AwF", "Leistungsphasen", "LOI" or one of their subclasses e.g. "Lph 1", "'010 Bestandserfassung und -modellierung'", "LOI 400"
        pset_filter_groups: Filter = get_merkmale_api_v1_public_filter.sync(client=client)
        print(pset_filter_groups)


        # 3a) Access all publicly available and visible PSETs, that match the filter criteria
        # Liste aller öffentlich sichtbaren Merkmalsgruppen, welche die übermittelten Suchkriterien erfüllen
        # A pagination is active by default and gives a maximum of 1000 items per requests
        # it returns a list of Merkmalsgruppen Classes, by default paginated to a maximum of 1000 if not further filter criteria are applied
        matching_psets: Merkmalsgruppe = post_merkmale_api_v1_public_propertygroup.sync(client=client, body=Suchkriterium(page_number=0))
        print(matching_psets[-1])


        # 4a) Properties Post
        # A pagination is active by default and gives a maximum of 1000 items per requests
        # it returns a list of Merkmal Classes, by default paginated to a maximum of 1000 if not further filter criteria is applied
        props_page0 : Merkmal = post_merkmale_api_v1_public_property.sync(body=Suchkriterium(page_number=0), client=client)

        
        
        pass



```


## General Usage
First, create a client:

```python
from bim_portal_deutschland_visu import Client

client = Client(base_url="https://via.bund.de/bim/infrastruktur/api/v1/public")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from bim_portal_deutschland_visu import AuthenticatedClient

client = AuthenticatedClient(base_url="https://via.bund.de/bim/infrastruktur/api/v1/public", token="ThisApiHasNoSecretTokenYet")
```

Now call your endpoint and use your models:

```python
from bim_portal_deutschland_visu.models import MyDataModel
from bim_portal_deutschland_visu.api.my_tag import get_my_data_model
from bim_portal_deutschland_visu.types import Response

with client as client:
    my_data: MyDataModel = get_my_data_model.sync(client=client)
    # or if you need more info (e.g. status_code)
    response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from bim_portal_deutschland_visu.models import MyDataModel
from bim_portal_deutschland_visu.api.my_tag import get_my_data_model
from bim_portal_deutschland_visu.types import Response

async with client as client:
    my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
    response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```



## Details - SSL Certificate Verfication and custom keychains
By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `bim_portal_deutschland_visu.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from bim_portal_deutschland_visu import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from bim_portal_deutschland_visu import Client

client = Client(
    base_url="https://api.example.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.example.com", proxies="http://localhost:8030"))
```

## Building / publishing this package
This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`

