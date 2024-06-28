"""Contains all the data models used in inputs/outputs"""

from .filter_ import Filter
from .kurzinformation import Kurzinformation
from .merkmal import Merkmal
from .merkmal_bookmarked import MerkmalBookmarked
from .merkmal_boundary_values_item import MerkmalBoundaryValuesItem
from .merkmal_connected_properties_item import MerkmalConnectedPropertiesItem
from .merkmal_connected_properties_item_names_in_language_item import MerkmalConnectedPropertiesItemNamesInLanguageItem
from .merkmal_creators_language import MerkmalCreatorsLanguage
from .merkmal_definitions_in_language_item import MerkmalDefinitionsInLanguageItem
from .merkmal_descriptions_in_language_item import MerkmalDescriptionsInLanguageItem
from .merkmal_digital_format_item import MerkmalDigitalFormatItem
from .merkmal_examples_in_language_item import MerkmalExamplesInLanguageItem
from .merkmal_group_of_properties_item import MerkmalGroupOfPropertiesItem
from .merkmal_group_of_properties_item_names_in_language_item import MerkmalGroupOfPropertiesItemNamesInLanguageItem
from .merkmal_list_of_possible_values_in_language_item import MerkmalListOfPossibleValuesInLanguageItem
from .merkmal_metadata import MerkmalMetadata
from .merkmal_names_in_language_item import MerkmalNamesInLanguageItem
from .merkmal_names_of_the_defining_values_item import MerkmalNamesOfTheDefiningValuesItem
from .merkmal_observed import MerkmalObserved
from .merkmal_parameters_of_the_dynamic_property_item import MerkmalParametersOfTheDynamicPropertyItem
from .merkmal_parameters_of_the_dynamic_property_item_names_in_language_item import (
    MerkmalParametersOfTheDynamicPropertyItemNamesInLanguageItem,
)
from .merkmal_physical_quantity_item import MerkmalPhysicalQuantityItem
from .merkmal_relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item import (
    MerkmalRelationOfThePropertyIdentifiersInTheInterconnectedDictionariesItem,
)
from .merkmal_replaced_by_item import MerkmalReplacedByItem
from .merkmal_replaced_by_item_names_in_language_item import MerkmalReplacedByItemNamesInLanguageItem
from .merkmal_replaces_item import MerkmalReplacesItem
from .merkmal_replaces_item_names_in_language_item import MerkmalReplacesItemNamesInLanguageItem
from .merkmal_symbols_of_the_property_in_a_given_property_group_item import (
    MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem,
)
from .merkmal_symbols_of_the_property_in_a_given_property_group_item_group_names_item import (
    MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItemGroupNamesItem,
)
from .merkmal_tags_item import MerkmalTagsItem
from .merkmal_tags_item_tag import MerkmalTagsItemTag
from .merkmal_text_format import MerkmalTextFormat
from .merkmalsfiltergruppe import Merkmalsfiltergruppe
from .merkmalsgruppe import Merkmalsgruppe
from .merkmalsgruppe_bookmarked import MerkmalsgruppeBookmarked
from .merkmalsgruppe_children_property_groups_item import MerkmalsgruppeChildrenPropertyGroupsItem
from .merkmalsgruppe_creators_language import MerkmalsgruppeCreatorsLanguage
from .merkmalsgruppe_definitions_in_language_item import MerkmalsgruppeDefinitionsInLanguageItem
from .merkmalsgruppe_metadata import MerkmalsgruppeMetadata
from .merkmalsgruppe_names_in_language_item import MerkmalsgruppeNamesInLanguageItem
from .merkmalsgruppe_observed import MerkmalsgruppeObserved
from .merkmalsgruppe_parent_group import MerkmalsgruppeParentGroup
from .merkmalsgruppe_parent_group_names_in_language_item import MerkmalsgruppeParentGroupNamesInLanguageItem
from .merkmalsgruppe_relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries import (
    MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries,
)
from .merkmalsgruppe_replaced_by_item import MerkmalsgruppeReplacedByItem
from .merkmalsgruppe_replaced_by_item_names_in_language_item import MerkmalsgruppeReplacedByItemNamesInLanguageItem
from .merkmalsgruppe_replaces_item import MerkmalsgruppeReplacesItem
from .merkmalsgruppe_replaces_item_names_in_language_item import MerkmalsgruppeReplacesItemNamesInLanguageItem
from .merkmalsgruppe_simple_inherited_properties_item import MerkmalsgruppeSimpleInheritedPropertiesItem
from .merkmalsgruppe_simple_inherited_properties_item_names_item import (
    MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem,
)
from .merkmalsgruppe_tags_item import MerkmalsgruppeTagsItem
from .merkmalsgruppe_tags_item_tag import MerkmalsgruppeTagsItemTag
from .organisation import Organisation
from .suchkriterium import Suchkriterium

__all__ = (
    "Filter",
    "Kurzinformation",
    "Merkmal",
    "MerkmalBookmarked",
    "MerkmalBoundaryValuesItem",
    "MerkmalConnectedPropertiesItem",
    "MerkmalConnectedPropertiesItemNamesInLanguageItem",
    "MerkmalCreatorsLanguage",
    "MerkmalDefinitionsInLanguageItem",
    "MerkmalDescriptionsInLanguageItem",
    "MerkmalDigitalFormatItem",
    "MerkmalExamplesInLanguageItem",
    "MerkmalGroupOfPropertiesItem",
    "MerkmalGroupOfPropertiesItemNamesInLanguageItem",
    "MerkmalListOfPossibleValuesInLanguageItem",
    "MerkmalMetadata",
    "MerkmalNamesInLanguageItem",
    "MerkmalNamesOfTheDefiningValuesItem",
    "MerkmalObserved",
    "MerkmalParametersOfTheDynamicPropertyItem",
    "MerkmalParametersOfTheDynamicPropertyItemNamesInLanguageItem",
    "MerkmalPhysicalQuantityItem",
    "MerkmalRelationOfThePropertyIdentifiersInTheInterconnectedDictionariesItem",
    "MerkmalReplacedByItem",
    "MerkmalReplacedByItemNamesInLanguageItem",
    "MerkmalReplacesItem",
    "MerkmalReplacesItemNamesInLanguageItem",
    "Merkmalsfiltergruppe",
    "Merkmalsgruppe",
    "MerkmalsgruppeBookmarked",
    "MerkmalsgruppeChildrenPropertyGroupsItem",
    "MerkmalsgruppeCreatorsLanguage",
    "MerkmalsgruppeDefinitionsInLanguageItem",
    "MerkmalsgruppeMetadata",
    "MerkmalsgruppeNamesInLanguageItem",
    "MerkmalsgruppeObserved",
    "MerkmalsgruppeParentGroup",
    "MerkmalsgruppeParentGroupNamesInLanguageItem",
    "MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries",
    "MerkmalsgruppeReplacedByItem",
    "MerkmalsgruppeReplacedByItemNamesInLanguageItem",
    "MerkmalsgruppeReplacesItem",
    "MerkmalsgruppeReplacesItemNamesInLanguageItem",
    "MerkmalsgruppeSimpleInheritedPropertiesItem",
    "MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem",
    "MerkmalsgruppeTagsItem",
    "MerkmalsgruppeTagsItemTag",
    "MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem",
    "MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItemGroupNamesItem",
    "MerkmalTagsItem",
    "MerkmalTagsItemTag",
    "MerkmalTextFormat",
    "Organisation",
    "Suchkriterium",
)
