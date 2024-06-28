
from bim_portal_deutschland_visu.models import *
#from bim_portal_deutschland_visu.models import Filter, Kurzinformation, Merkmal, Organisation, Suchkriterium, MerkmalsgruppeBookmarked, MerkmalBookmarked, Merkmalsgruppe, Merkmals

from bim_portal_deutschland_visu.api.organisationen import get_infrastruktur_api_v1_public_organisation
from bim_portal_deutschland_visu.api.merkmalsgruppen import get_merkmale_api_v1_public_propertygroup_guid, post_merkmale_api_v1_public_propertygroup
from bim_portal_deutschland_visu.api.filter_ import get_merkmale_api_v1_public_filter
from bim_portal_deutschland_visu.api.merkmale import get_merkmale_api_v1_public_property_guid, post_merkmale_api_v1_public_property
from bim_portal_deutschland_visu.types import Response
from bim_portal_deutschland_visu.client import Client, AuthenticatedClient
# from bim_portal_deutschland_visu.models import 


if __name__ == "__main__":
    
    client = Client(base_url="https://via.bund.de/bim") # infrastruktur/api/v1/public/organisation

    with client as client:
        
        # 1) Access first api endpoint and get an list of Organisation classes back:
        # Hint: The Organisation must provice their pset list via the rest api. This has set up explicitly by the org (?)
        organisations: Organisation = get_infrastruktur_api_v1_public_organisation.sync(client=client)        
        # or if you need more info (e.g. status_code)
        # organisation_detailed_data_response: Response[Organisation] = get_infrastruktur_api_v1_public_organisation.sync_detailed(client=client)


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
        # matching_psets_page2: Merkmalsgruppe = post_merkmale_api_v1_public_propertygroup.sync(client=client, body=Suchkriterium(page_number=1))
        # print(matching_psets_page2[0])

        # 3b) Get one specific PSET by its GUID
        # Liefert die Merkmalsgruppe mit der übergebenen GUID zurück
        # GUID = '91ba0be4-0440-4759-8e5c-1ff741fa182f' # matching_psets[-1].guid
        # no_pset : Merkmalsgruppe = get_merkmale_api_v1_public_propertygroup_guid.sync(guid="no-existing-guid", client=client)
        # no_pset : Merkmalsgruppe = get_merkmale_api_v1_public_propertygroup_guid.sync_detailed(guid=GUID, client=client)
        # example_pset_by_guid_filter : Merkmalsgruppe = get_merkmale_api_v1_public_propertygroup_guid.sync(guid=GUID, client=client)
        # TODO: Gives an error at the moment!

        # 4a) Properties Post
        # A pagination is active by default and gives a maximum of 1000 items per requests
        # it returns a list of Merkmal Classes, by default paginated to a maximum of 1000 if not further filter criteria is applied
        props_page0 : Merkmal = post_merkmale_api_v1_public_property.sync(body=Suchkriterium(page_number=0), client=client)

        # 4b) Properties Get by GUID
        #TODO: WIP - Gives an error at the moment!
        # example_prop_guid = "5fe6bc21-aad7-47b8-8c35-b4cf9c3d2c34"
        # get_merkmale_api_v1_public_property_guid.sync(guid=example_prop_guid, client=client)
        # example_prop = Merkmal(guid=example_prop_guid)
        # get_merkmale_api_v1_public_property_guid.sync(guid=example_prop.guid, client=client)
        
        
        
        pass