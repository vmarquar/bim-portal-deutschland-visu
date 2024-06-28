from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merkmal import Merkmal
    from ..models.merkmalsgruppe_bookmarked import MerkmalsgruppeBookmarked
    from ..models.merkmalsgruppe_children_property_groups_item import MerkmalsgruppeChildrenPropertyGroupsItem
    from ..models.merkmalsgruppe_creators_language import MerkmalsgruppeCreatorsLanguage
    from ..models.merkmalsgruppe_definitions_in_language_item import MerkmalsgruppeDefinitionsInLanguageItem
    from ..models.merkmalsgruppe_metadata import MerkmalsgruppeMetadata
    from ..models.merkmalsgruppe_names_in_language_item import MerkmalsgruppeNamesInLanguageItem
    from ..models.merkmalsgruppe_observed import MerkmalsgruppeObserved
    from ..models.merkmalsgruppe_parent_group import MerkmalsgruppeParentGroup
    from ..models.merkmalsgruppe_relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries import (
        MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries,
    )
    from ..models.merkmalsgruppe_replaced_by_item import MerkmalsgruppeReplacedByItem
    from ..models.merkmalsgruppe_replaces_item import MerkmalsgruppeReplacesItem
    from ..models.merkmalsgruppe_simple_inherited_properties_item import MerkmalsgruppeSimpleInheritedPropertiesItem
    from ..models.merkmalsgruppe_tags_item import MerkmalsgruppeTagsItem


T = TypeVar("T", bound="Merkmalsgruppe")


@_attrs_define
class Merkmalsgruppe:
    """
    Attributes:
        id (Union[Unset, str]):
        guid (Union[Unset, str]): global eindeutiger Be-zeichner
        status (Union[Unset, str]): Status der Merkmals-gruppe während ihres Lebenszyklus
        property_status (Union[Unset, str]):
        date_of_creation (Union[Unset, str]): Datum der Validierung der Anfrage zur Erstel-lung der Merkmals-gruppe
            durch Sachver-ständige
        date_of_activation (Union[Unset, str]): Datum, nach dem die Merkmalsgruppe ver-wendet werden kann
        date_of_last_change (Union[Unset, str]): Datum der Validierung der letzten Änderungs-anfrage durch Sachver-
            ständige
        date_of_revision (Union[Unset, str]): Datum der Überarbeitung
        date_of_version (Union[Unset, str]): Datum der Version
        date_of_deactivation (Union[Unset, str]): Datum, ab dem die Merkmalsgruppe veraltet ist; die Merkmals-gruppe
            wird im Daten-katalog behalten
        version_number (Union[Unset, int]): Diese Versionsnummer ermöglicht die Verfol-gung größerer Ände-rungen. Die
            Sachver-ständigen entscheiden, ob die Versionsnummer geändert wer-den muss oder nicht.
        revision_number (Union[Unset, int]): Diese Nummer der Überarbeitung ermög-licht die Verfolgung kleinerer
            Änderungen, z. B. neue Übersetzung, Korrekturen von Tipp-fehlern; wenn sich die Versionsnummer än-dert, beginnt
            die Nummer der Überarbeitung wieder bei 1. Die Sach-verständigen treffen die Entscheidung über die Änderung
            einer Nummer der Überar-beitung.
        replaces (Union[Unset, List['MerkmalsgruppeReplacesItem']]): Liste von globalen Bezeichnern für die ersetzten
            Merk-malsgruppen
        replaced_by (Union[Unset, List['MerkmalsgruppeReplacedByItem']]): Liste von globalen Bezeichnern für die
            ersetzenden Merkmalsgruppen
        deprecation_explanation (Union[Unset, str]): Satz, der den Grund für die Ablehnung erläu-tert, der erklären
            kann, wie Werte umzurech-nen sind, damit sie der neuen Merkmals-gruppe entsprechen; diese Erläuterung muss in
            internationalem Englisch geschrieben werden
        relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries (Union[Unset,
            MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries]): Liste von Paaren (inter-
            ner Bezeichner der Merkmalsgruppe, ent-sprechender Daten-katalog-Bezeichner) dieses Attribut sollte für die
            Kompatibilität zwischen bereits vorhandenen Merk-malsgruppen verwen-det werden
        creators_language (Union[Unset, MerkmalsgruppeCreatorsLanguage]): Sprache des Erstellers der Merkmalsgruppe
        names_in_language (Union[Unset, List['MerkmalsgruppeNamesInLanguageItem']]): Liste von Paaren (Name der
            Merkmals-gruppe und Sprache) dieses Attribut kann verwendet werden, um Synonyme für verschie-dene Domänen hinzu-
            zufügen
        definitions_in_language (Union[Unset, List['MerkmalsgruppeDefinitionsInLanguageItem']]): Liste von Paaren (Defi-
            nition der Merkmals-gruppe, Sprache)
        visual_representations (Union[Unset, List[str]]): Bildliche Darstellung der Merkmalsgruppe durch Skizzen, Fotos,
            Videos oder sonstige Multimedia-Objekte
        country_of_use (Union[Unset, List[str]]): Land, in dem die Merk-malsgruppe verwendet wird
        subdivision_of_use (Union[Unset, List[str]]): Dokumentierte geogra-phische Region, in der die Merkmalsgruppe
            verwendet wird
        country_of_origin (Union[Unset, str]): Land, in dem die An-forderung für diese Merkmalsgruppe fest-gelegt wurde
        category_of_group_of_properties (Union[Unset, str]): Gibt die Kategorie der erstellten Merkmals-gruppe an
        properties (Union[Unset, List['Merkmal']]):
        children_property_groups (Union[Unset, List['MerkmalsgruppeChildrenPropertyGroupsItem']]):
        parent_group (Union[Unset, MerkmalsgruppeParentGroup]): Ermöglicht die Ver-knüpfung einer Unter-gruppe mit einer
            über-geordneten Gruppe über ihre global ein-deutigen Bezeichne(Attribut GA001) jedes einer Gruppe zugehörige
            Merkmal wird von der/den Untergruppe(n) übernommen
        metadata (Union[Unset, MerkmalsgruppeMetadata]):
        bookmarked (Union[Unset, MerkmalsgruppeBookmarked]):
        observed (Union[Unset, MerkmalsgruppeObserved]):
        simple_inherited_properties (Union[Unset, List['MerkmalsgruppeSimpleInheritedPropertiesItem']]):
        organisation_id (Union[Unset, str]):
        organisation_name (Union[Unset, str]):
        tags (Union[Unset, List['MerkmalsgruppeTagsItem']]):
        organisation_type (Union[Unset, str]):
        can_create_new_version (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    property_status: Union[Unset, str] = UNSET
    date_of_creation: Union[Unset, str] = UNSET
    date_of_activation: Union[Unset, str] = UNSET
    date_of_last_change: Union[Unset, str] = UNSET
    date_of_revision: Union[Unset, str] = UNSET
    date_of_version: Union[Unset, str] = UNSET
    date_of_deactivation: Union[Unset, str] = UNSET
    version_number: Union[Unset, int] = UNSET
    revision_number: Union[Unset, int] = UNSET
    replaces: Union[Unset, List["MerkmalsgruppeReplacesItem"]] = UNSET
    replaced_by: Union[Unset, List["MerkmalsgruppeReplacedByItem"]] = UNSET
    deprecation_explanation: Union[Unset, str] = UNSET
    relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries: Union[
        Unset, "MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries"
    ] = UNSET
    creators_language: Union[Unset, "MerkmalsgruppeCreatorsLanguage"] = UNSET
    names_in_language: Union[Unset, List["MerkmalsgruppeNamesInLanguageItem"]] = UNSET
    definitions_in_language: Union[Unset, List["MerkmalsgruppeDefinitionsInLanguageItem"]] = UNSET
    visual_representations: Union[Unset, List[str]] = UNSET
    country_of_use: Union[Unset, List[str]] = UNSET
    subdivision_of_use: Union[Unset, List[str]] = UNSET
    country_of_origin: Union[Unset, str] = UNSET
    category_of_group_of_properties: Union[Unset, str] = UNSET
    properties: Union[Unset, List["Merkmal"]] = UNSET
    children_property_groups: Union[Unset, List["MerkmalsgruppeChildrenPropertyGroupsItem"]] = UNSET
    parent_group: Union[Unset, "MerkmalsgruppeParentGroup"] = UNSET
    metadata: Union[Unset, "MerkmalsgruppeMetadata"] = UNSET
    bookmarked: Union[Unset, "MerkmalsgruppeBookmarked"] = UNSET
    observed: Union[Unset, "MerkmalsgruppeObserved"] = UNSET
    simple_inherited_properties: Union[Unset, List["MerkmalsgruppeSimpleInheritedPropertiesItem"]] = UNSET
    organisation_id: Union[Unset, str] = UNSET
    organisation_name: Union[Unset, str] = UNSET
    tags: Union[Unset, List["MerkmalsgruppeTagsItem"]] = UNSET
    organisation_type: Union[Unset, str] = UNSET
    can_create_new_version: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        guid = self.guid

        status = self.status

        property_status = self.property_status

        date_of_creation = self.date_of_creation

        date_of_activation = self.date_of_activation

        date_of_last_change = self.date_of_last_change

        date_of_revision = self.date_of_revision

        date_of_version = self.date_of_version

        date_of_deactivation = self.date_of_deactivation

        version_number = self.version_number

        revision_number = self.revision_number

        replaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.replaces, Unset):
            replaces = []
            for replaces_item_data in self.replaces:
                replaces_item = replaces_item_data.to_dict()
                replaces.append(replaces_item)

        replaced_by: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.replaced_by, Unset):
            replaced_by = []
            for replaced_by_item_data in self.replaced_by:
                replaced_by_item = replaced_by_item_data.to_dict()
                replaced_by.append(replaced_by_item)

        deprecation_explanation = self.deprecation_explanation

        relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries: Union[Unset, Dict[str, Any]] = (
            UNSET
        )
        if not isinstance(self.relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries, Unset):
            relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries = (
                self.relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries.to_dict()
            )

        creators_language: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.creators_language, Unset):
            creators_language = self.creators_language.to_dict()

        names_in_language: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.names_in_language, Unset):
            names_in_language = []
            for names_in_language_item_data in self.names_in_language:
                names_in_language_item = names_in_language_item_data.to_dict()
                names_in_language.append(names_in_language_item)

        definitions_in_language: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.definitions_in_language, Unset):
            definitions_in_language = []
            for definitions_in_language_item_data in self.definitions_in_language:
                definitions_in_language_item = definitions_in_language_item_data.to_dict()
                definitions_in_language.append(definitions_in_language_item)

        visual_representations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.visual_representations, Unset):
            visual_representations = self.visual_representations

        country_of_use: Union[Unset, List[str]] = UNSET
        if not isinstance(self.country_of_use, Unset):
            country_of_use = self.country_of_use

        subdivision_of_use: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subdivision_of_use, Unset):
            subdivision_of_use = self.subdivision_of_use

        country_of_origin = self.country_of_origin

        category_of_group_of_properties = self.category_of_group_of_properties

        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        children_property_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children_property_groups, Unset):
            children_property_groups = []
            for children_property_groups_item_data in self.children_property_groups:
                children_property_groups_item = children_property_groups_item_data.to_dict()
                children_property_groups.append(children_property_groups_item)

        parent_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_group, Unset):
            parent_group = self.parent_group.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        bookmarked: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bookmarked, Unset):
            bookmarked = self.bookmarked.to_dict()

        observed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.observed, Unset):
            observed = self.observed.to_dict()

        simple_inherited_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.simple_inherited_properties, Unset):
            simple_inherited_properties = []
            for simple_inherited_properties_item_data in self.simple_inherited_properties:
                simple_inherited_properties_item = simple_inherited_properties_item_data.to_dict()
                simple_inherited_properties.append(simple_inherited_properties_item)

        organisation_id = self.organisation_id

        organisation_name = self.organisation_name

        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        organisation_type = self.organisation_type

        can_create_new_version = self.can_create_new_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if status is not UNSET:
            field_dict["status"] = status
        if property_status is not UNSET:
            field_dict["propertyStatus"] = property_status
        if date_of_creation is not UNSET:
            field_dict["dateOfCreation"] = date_of_creation
        if date_of_activation is not UNSET:
            field_dict["dateOfActivation"] = date_of_activation
        if date_of_last_change is not UNSET:
            field_dict["dateOfLastChange"] = date_of_last_change
        if date_of_revision is not UNSET:
            field_dict["dateOfRevision"] = date_of_revision
        if date_of_version is not UNSET:
            field_dict["dateOfVersion"] = date_of_version
        if date_of_deactivation is not UNSET:
            field_dict["dateOfDeactivation"] = date_of_deactivation
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number
        if revision_number is not UNSET:
            field_dict["revisionNumber"] = revision_number
        if replaces is not UNSET:
            field_dict["replaces"] = replaces
        if replaced_by is not UNSET:
            field_dict["replacedBy"] = replaced_by
        if deprecation_explanation is not UNSET:
            field_dict["deprecationExplanation"] = deprecation_explanation
        if relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries is not UNSET:
            field_dict["relationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries"] = (
                relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries
            )
        if creators_language is not UNSET:
            field_dict["creatorsLanguage"] = creators_language
        if names_in_language is not UNSET:
            field_dict["namesInLanguage"] = names_in_language
        if definitions_in_language is not UNSET:
            field_dict["definitionsInLanguage"] = definitions_in_language
        if visual_representations is not UNSET:
            field_dict["visualRepresentations"] = visual_representations
        if country_of_use is not UNSET:
            field_dict["countryOfUse"] = country_of_use
        if subdivision_of_use is not UNSET:
            field_dict["subdivisionOfUse"] = subdivision_of_use
        if country_of_origin is not UNSET:
            field_dict["countryOfOrigin"] = country_of_origin
        if category_of_group_of_properties is not UNSET:
            field_dict["categoryOfGroupOfProperties"] = category_of_group_of_properties
        if properties is not UNSET:
            field_dict["properties"] = properties
        if children_property_groups is not UNSET:
            field_dict["childrenPropertyGroups"] = children_property_groups
        if parent_group is not UNSET:
            field_dict["parentGroup"] = parent_group
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if bookmarked is not UNSET:
            field_dict["bookmarked"] = bookmarked
        if observed is not UNSET:
            field_dict["observed"] = observed
        if simple_inherited_properties is not UNSET:
            field_dict["simpleInheritedProperties"] = simple_inherited_properties
        if organisation_id is not UNSET:
            field_dict["organisationId"] = organisation_id
        if organisation_name is not UNSET:
            field_dict["organisationName"] = organisation_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if organisation_type is not UNSET:
            field_dict["organisationType"] = organisation_type
        if can_create_new_version is not UNSET:
            field_dict["canCreateNewVersion"] = can_create_new_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.merkmal import Merkmal
        from ..models.merkmalsgruppe_bookmarked import MerkmalsgruppeBookmarked
        from ..models.merkmalsgruppe_children_property_groups_item import MerkmalsgruppeChildrenPropertyGroupsItem
        from ..models.merkmalsgruppe_creators_language import MerkmalsgruppeCreatorsLanguage
        from ..models.merkmalsgruppe_definitions_in_language_item import MerkmalsgruppeDefinitionsInLanguageItem
        from ..models.merkmalsgruppe_metadata import MerkmalsgruppeMetadata
        from ..models.merkmalsgruppe_names_in_language_item import MerkmalsgruppeNamesInLanguageItem
        from ..models.merkmalsgruppe_observed import MerkmalsgruppeObserved
        from ..models.merkmalsgruppe_parent_group import MerkmalsgruppeParentGroup
        from ..models.merkmalsgruppe_relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries import (
            MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries,
        )
        from ..models.merkmalsgruppe_replaced_by_item import MerkmalsgruppeReplacedByItem
        from ..models.merkmalsgruppe_replaces_item import MerkmalsgruppeReplacesItem
        from ..models.merkmalsgruppe_simple_inherited_properties_item import MerkmalsgruppeSimpleInheritedPropertiesItem
        from ..models.merkmalsgruppe_tags_item import MerkmalsgruppeTagsItem

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        guid = d.pop("guid", UNSET)

        status = d.pop("status", UNSET)

        property_status = d.pop("propertyStatus", UNSET)

        date_of_creation = d.pop("dateOfCreation", UNSET)

        date_of_activation = d.pop("dateOfActivation", UNSET)

        date_of_last_change = d.pop("dateOfLastChange", UNSET)

        date_of_revision = d.pop("dateOfRevision", UNSET)

        date_of_version = d.pop("dateOfVersion", UNSET)

        date_of_deactivation = d.pop("dateOfDeactivation", UNSET)

        version_number = d.pop("versionNumber", UNSET)

        revision_number = d.pop("revisionNumber", UNSET)

        replaces = []
        _replaces = d.pop("replaces", UNSET)
        for replaces_item_data in _replaces or []:
            replaces_item = MerkmalsgruppeReplacesItem.from_dict(replaces_item_data)

            replaces.append(replaces_item)

        replaced_by = []
        _replaced_by = d.pop("replacedBy", UNSET)
        for replaced_by_item_data in _replaced_by or []:
            replaced_by_item = MerkmalsgruppeReplacedByItem.from_dict(replaced_by_item_data)

            replaced_by.append(replaced_by_item)

        deprecation_explanation = d.pop("deprecationExplanation", UNSET)

        _relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries = d.pop(
            "relationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries", UNSET
        )
        relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries: Union[
            Unset, MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries
        ]
        if isinstance(_relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries, Unset):
            relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries = UNSET
        else:
            relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries = (
                MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries.from_dict(
                    _relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries
                )
            )

        _creators_language = d.pop("creatorsLanguage", UNSET)
        creators_language: Union[Unset, MerkmalsgruppeCreatorsLanguage]
        if isinstance(_creators_language, Unset):
            creators_language = UNSET
        else:
            creators_language = MerkmalsgruppeCreatorsLanguage.from_dict(_creators_language)

        names_in_language = []
        _names_in_language = d.pop("namesInLanguage", UNSET)
        for names_in_language_item_data in _names_in_language or []:
            names_in_language_item = MerkmalsgruppeNamesInLanguageItem.from_dict(names_in_language_item_data)

            names_in_language.append(names_in_language_item)

        definitions_in_language = []
        _definitions_in_language = d.pop("definitionsInLanguage", UNSET)
        for definitions_in_language_item_data in _definitions_in_language or []:
            definitions_in_language_item = MerkmalsgruppeDefinitionsInLanguageItem.from_dict(
                definitions_in_language_item_data
            )

            definitions_in_language.append(definitions_in_language_item)

        visual_representations = cast(List[str], d.pop("visualRepresentations", UNSET))

        country_of_use = cast(List[str], d.pop("countryOfUse", UNSET))

        subdivision_of_use = cast(List[str], d.pop("subdivisionOfUse", UNSET))

        country_of_origin = d.pop("countryOfOrigin", UNSET)

        category_of_group_of_properties = d.pop("categoryOfGroupOfProperties", UNSET)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = Merkmal.from_dict(properties_item_data)

            properties.append(properties_item)

        children_property_groups = []
        _children_property_groups = d.pop("childrenPropertyGroups", UNSET)
        for children_property_groups_item_data in _children_property_groups or []:
            children_property_groups_item = MerkmalsgruppeChildrenPropertyGroupsItem.from_dict(
                children_property_groups_item_data
            )

            children_property_groups.append(children_property_groups_item)

        _parent_group = d.pop("parentGroup", UNSET)
        parent_group: Union[Unset, MerkmalsgruppeParentGroup]
        if isinstance(_parent_group, Unset):
            parent_group = UNSET
        else:
            parent_group = MerkmalsgruppeParentGroup.from_dict(_parent_group)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, MerkmalsgruppeMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = MerkmalsgruppeMetadata.from_dict(_metadata)

        _bookmarked = d.pop("bookmarked", UNSET)
        bookmarked: Union[Unset, MerkmalsgruppeBookmarked]
        if isinstance(_bookmarked, Unset):
            bookmarked = UNSET
        else:
            bookmarked = MerkmalsgruppeBookmarked.from_dict(_bookmarked)

        _observed = d.pop("observed", UNSET)
        observed: Union[Unset, MerkmalsgruppeObserved]
        if isinstance(_observed, Unset):
            observed = UNSET
        else:
            observed = MerkmalsgruppeObserved.from_dict(_observed)

        simple_inherited_properties = []
        _simple_inherited_properties = d.pop("simpleInheritedProperties", UNSET)
        for simple_inherited_properties_item_data in _simple_inherited_properties or []:
            simple_inherited_properties_item = MerkmalsgruppeSimpleInheritedPropertiesItem.from_dict(
                simple_inherited_properties_item_data
            )

            simple_inherited_properties.append(simple_inherited_properties_item)

        organisation_id = d.pop("organisationId", UNSET)

        organisation_name = d.pop("organisationName", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = MerkmalsgruppeTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        organisation_type = d.pop("organisationType", UNSET)

        can_create_new_version = d.pop("canCreateNewVersion", UNSET)

        merkmalsgruppe = cls(
            id=id,
            guid=guid,
            status=status,
            property_status=property_status,
            date_of_creation=date_of_creation,
            date_of_activation=date_of_activation,
            date_of_last_change=date_of_last_change,
            date_of_revision=date_of_revision,
            date_of_version=date_of_version,
            date_of_deactivation=date_of_deactivation,
            version_number=version_number,
            revision_number=revision_number,
            replaces=replaces,
            replaced_by=replaced_by,
            deprecation_explanation=deprecation_explanation,
            relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries=relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries,
            creators_language=creators_language,
            names_in_language=names_in_language,
            definitions_in_language=definitions_in_language,
            visual_representations=visual_representations,
            country_of_use=country_of_use,
            subdivision_of_use=subdivision_of_use,
            country_of_origin=country_of_origin,
            category_of_group_of_properties=category_of_group_of_properties,
            properties=properties,
            children_property_groups=children_property_groups,
            parent_group=parent_group,
            metadata=metadata,
            bookmarked=bookmarked,
            observed=observed,
            simple_inherited_properties=simple_inherited_properties,
            organisation_id=organisation_id,
            organisation_name=organisation_name,
            tags=tags,
            organisation_type=organisation_type,
            can_create_new_version=can_create_new_version,
        )

        merkmalsgruppe.additional_properties = d
        return merkmalsgruppe

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
