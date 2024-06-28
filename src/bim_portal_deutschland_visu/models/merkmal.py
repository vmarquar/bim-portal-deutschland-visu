from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merkmal_bookmarked import MerkmalBookmarked
    from ..models.merkmal_boundary_values_item import MerkmalBoundaryValuesItem
    from ..models.merkmal_connected_properties_item import MerkmalConnectedPropertiesItem
    from ..models.merkmal_creators_language import MerkmalCreatorsLanguage
    from ..models.merkmal_definitions_in_language_item import MerkmalDefinitionsInLanguageItem
    from ..models.merkmal_descriptions_in_language_item import MerkmalDescriptionsInLanguageItem
    from ..models.merkmal_digital_format_item import MerkmalDigitalFormatItem
    from ..models.merkmal_examples_in_language_item import MerkmalExamplesInLanguageItem
    from ..models.merkmal_group_of_properties_item import MerkmalGroupOfPropertiesItem
    from ..models.merkmal_list_of_possible_values_in_language_item import MerkmalListOfPossibleValuesInLanguageItem
    from ..models.merkmal_metadata import MerkmalMetadata
    from ..models.merkmal_names_in_language_item import MerkmalNamesInLanguageItem
    from ..models.merkmal_names_of_the_defining_values_item import MerkmalNamesOfTheDefiningValuesItem
    from ..models.merkmal_observed import MerkmalObserved
    from ..models.merkmal_parameters_of_the_dynamic_property_item import MerkmalParametersOfTheDynamicPropertyItem
    from ..models.merkmal_physical_quantity_item import MerkmalPhysicalQuantityItem
    from ..models.merkmal_relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item import (
        MerkmalRelationOfThePropertyIdentifiersInTheInterconnectedDictionariesItem,
    )
    from ..models.merkmal_replaced_by_item import MerkmalReplacedByItem
    from ..models.merkmal_replaces_item import MerkmalReplacesItem
    from ..models.merkmal_symbols_of_the_property_in_a_given_property_group_item import (
        MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem,
    )
    from ..models.merkmal_tags_item import MerkmalTagsItem
    from ..models.merkmal_text_format import MerkmalTextFormat


T = TypeVar("T", bound="Merkmal")


@_attrs_define
class Merkmal:
    """
    Attributes:
        id (Union[Unset, str]):
        guid (Union[Unset, str]): Global eindeutiger Bezeichner
        status (Union[Unset, str]): Status des Merkmals während seines Lebenszyklus
        property_status (Union[Unset, str]): Global eindeutiger Bezeichner
        date_of_creation (Union[Unset, str]): Datum der Validierung der An-frage zur Erstellung des Merkmals durch
            Sachverständige
        date_of_activation (Union[Unset, str]): Datum, nach dem das Merkmal verwendet werden kann
        date_of_last_change (Union[Unset, str]): Datum der Validierung der letzten Änderungsanfrage durch
            Sachverständige
        date_of_revision (Union[Unset, str]): Datum der Überarbeitung
        date_of_version (Union[Unset, str]): Datum der Version
        date_of_deactivation (Union[Unset, str]): Datum, ab dem das Merkmal veraltet ist; das Merkmal wird im
            Datenkatalog behalten
        version_number (Union[Unset, int]): Diese Versionsnummer ermöglicht die Verfolgung größerer Änderungen.
            Sachverständige entscheiden, ob eine neue Versionsnummer angewendet wer-den muss.
        revision_number (Union[Unset, int]): Diese Nummer der Überarbeitung ermöglicht die Verfolgung kleinerer
            Änderungen, z. B. neue Übersetzung, Korrekturen von Tippfehlern: wenn sich die Versionsnummer ändert, beginnt
            die Nummer der Überarbeitung wieder bei 1. Sachverständige entscheiden, ob eine neue Nummer der Überarbeitung
            angewendet werden kann oder ob eine neue Überarbeitung erforderlich ist.
        replaces (Union[Unset, List['MerkmalReplacesItem']]): Global eindeutiger Bezeichner (Attribut PA001) des
            ersetzten Merkmals (oder der Merkmale)
        replaced_by (Union[Unset, List['MerkmalReplacedByItem']]): Global eindeutiger Bezeichner (Attribut PA001) des
            ersetzenden Merkmals (oder der Merkmale)
        deprecation_explanation (Union[Unset, str]): Satz, der den Grund für die Ab-lehnung erläutert, der erklären
            kann, wie Werte umzurechnen sind, damit sie dem neuen Merkmal entsprechen
        relation_of_the_property_identifiers_in_the_interconnected_dictionaries (Union[Unset,
            List['MerkmalRelationOfThePropertyIdentifiersInTheInterconnectedDictionariesItem']]): Liste von Paaren (interner
            Merk-malsbezeichner, entsprechender Datenkatalog-Bezeichner) dieses Attribut sollte für die Verträglichkeit
            zwischen bereits vorhandenen Merkmalen verwendet werden
        creators_language (Union[Unset, MerkmalCreatorsLanguage]): Sprache des Erstellers des Merkmals
        names_in_language (Union[Unset, List['MerkmalNamesInLanguageItem']]): Liste von Paaren (Name des Merkmals und
            Sprache) dieses Attribut kann verwendet werden, um Synonyme für verschiedene Domänen hinzuzufügen
        definitions_in_language (Union[Unset, List['MerkmalDefinitionsInLanguageItem']]): Liste von Paaren (Definition
            des Merkmals, Sprache)
        descriptions_in_language (Union[Unset, List['MerkmalDescriptionsInLanguageItem']]): Liste von Paaren
            (Beschreibung des Merkmals, Sprache) dieses Attribut wird verwendet, um eine Beschreibung des Merkmals als
            Klartext bereitzustellen
        examples_in_language (Union[Unset, List['MerkmalExamplesInLanguageItem']]): Liste von Paaren (Beispielwerte,
            Sprache) dieses Attribut kann zur Veranschaulichung der möglichen Werte des Merkmals verwendet werden
        connected_properties (Union[Unset, List['MerkmalConnectedPropertiesItem']]): Liste der global eindeutigen Be-
            zeichner der verbundenen Merkmale (Attribut PA001); der Wert eines Merkmals steht zu den Werten der anderen in
            einer Beziehung. Beispielsweise ist ein Schallabsorptionsgrad für eine bestimmte Frequenz gegeben, in diesem
            Fall sind Schallabsorp-tionsgrad und Frequenz ver-bundene Merkmale.
        group_of_properties (Union[Unset, List['MerkmalGroupOfPropertiesItem']]): Liste von global eindeutigen Be-
            zeichnern von Merkmalsgruppen (Attribut GA001), denen das Merkmal angehört
        symbols_of_the_property_in_a_given_property_group (Union[Unset,
            List['MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem']]): Liste von Paaren (Symbol des Merkmals, global
            eindeutiger Bezeichner der Merkmalsgruppe (Attribut GA001))
        visual_representations (Union[Unset, List[str]]): bildliche Darstellung des Merkmals durch Skizzen, Fotos,
            Videos oder sonstige Multimedia-Objekte
        country_of_use (Union[Unset, List[str]]): Land (Gruppe von Ländern, Kon-tinent), in dem das Merkmal für den
            Markt, auf dem die Betei-ligten arbeiten, relevant ist Zum Beispiel: ISOLE (das Nutzungsprofil „ISOLE“ ist dafür
            bestimmt, die Angabe der Eignung von Wär-medämmprodukten in Bezug auf die Bedürfnisse von Nutzern zu
            vereinfachen, und wie in einer Reihe von kodifizierten Texten dargelegt) hat es ein Land der Verwendung: Europa
        subdivision_of_use (Union[Unset, List[str]]): dokumentierte geographische Region der Verwendung des Merkmals
        country_of_origin (Union[Unset, str]): Land, aus dem die Anforderung an dieses Merkmal stammt
        physical_quantity (Union[Unset, List['MerkmalPhysicalQuantityItem']]): Liste von Paaren (physikalische Größe |
            Sprache) Physikalische Größen werden in Einheiten des Internationalen Einheitensystems (SI) angegeben
        dimension (Union[Unset, str]): Im Falle einer physikalischen Größe, Dimension nach ISO 80000 (alle Teile) dieses
            Attribut ermöglicht, dass die Dimension maschinenlesbar ist; da alle physikalischen Größen von 7 Basisgrößen
            abgeleitet sind, wird es durch Angabe der Basisdimensionen mit zugehöriger Potenz (als rationale Zahl) in der
            folgenden Reihenfolge und mit jeweils einem Leerzeichen dazwischen angegeben: L M T I θ N J
        method_of_measurement (Union[Unset, str]): Beurteilung von Bauprodukten, um ihre Tauglichkeit entspre-chend den
            Anforderungen in harmonisierten technischen Spezifikationen sicherzustellen
        data_type (Union[Unset, str]): Format für die Angabe des Wertes des Merkmals dies kann aus einer Soft-ware-
            Perspektive als Speiche-rungsart verstanden werden im Falle eines dynamischen Merkmals ist der Wert dieses
            Attributs der Datentyp des Er-gebnisses der Berechnung mit der Gleichung
        dynamic_property (Union[Unset, str]): Wenn es sich um ein dynamisches Merkmal handelt, hängt der Wert von den im
            Attribut PA032 bereitgestellten Parametern ab
        parameters_of_the_dynamic_property (Union[Unset, List['MerkmalParametersOfTheDynamicPropertyItem']]): Liste von
            GUIDs von Merkmalen, welche Parameter der Funktion für ein dynamisches Merkmal sind
        units (Union[Unset, List[str]]): eine Einheit zur Darstellung einer Skala, die es ermöglicht, einen Wert zu
            messen es ist möglich, dieses Attribut zu verwenden, um zu erläutern, dass dem Merkmal keine Einheit zugeordnet
            ist, indem „ein-heitslos“ verwendet wird
        names_of_the_defining_values (Union[Unset, List['MerkmalNamesOfTheDefiningValuesItem']]): Im Falle eines Feldes
            liefert dieses Attribut die Namen der Spaltenköpfe, festgelegt als Liste von Paaren (Name, Sprache)
        defining_values (Union[Unset, List[str]]): Im Falle eines Feldes liefert dieses Attribut die definierenden
            Werte, sofern zutreffend, der Datentyp wird durch das Attribut PA030 angegeben
        tolerance (Union[Unset, List[int]]): Für numerische Werte; der Ge-samtbetrag, um den eine be-stimmte Einheit
            schwanken darf; sie ist die Differenz zwischen dem Höchstwert und dem Mindestwert für die Einheit
        digital_format (Union[Unset, List['MerkmalDigitalFormatItem']]): Paar für den digitalen Texttyp (Präzision,
            Maßeinheit) Präzision ist die Anzahl signifi-kanter Stellen
        text_format (Union[Unset, MerkmalTextFormat]): Paar für den Texttyp (Ver-schlüsselung, Anzahl der Zeichen) die
            Verschlüsselung wird nach „Name der Codierungsnorm“ von IANA, RFC 2978 festgelegt
        list_of_possible_values_in_language (Union[Unset, List['MerkmalListOfPossibleValuesInLanguageItem']]): Liste von
            Paaren (möglicher Wert für das Merkmal und Sprache) Werte können String oder Zahlen sein
        boundary_values (Union[Unset, List['MerkmalBoundaryValuesItem']]): Paar (Liste von Grenz-wert-Intervallen
            möglicher Werte für das Merkmal, Einheit)
        metadata (Union[Unset, MerkmalMetadata]):
        bookmarked (Union[Unset, MerkmalBookmarked]):
        observed (Union[Unset, MerkmalObserved]):
        organisation_id (Union[Unset, str]):
        organisation_name (Union[Unset, str]):
        tags (Union[Unset, List['MerkmalTagsItem']]):
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
    replaces: Union[Unset, List["MerkmalReplacesItem"]] = UNSET
    replaced_by: Union[Unset, List["MerkmalReplacedByItem"]] = UNSET
    deprecation_explanation: Union[Unset, str] = UNSET
    relation_of_the_property_identifiers_in_the_interconnected_dictionaries: Union[
        Unset, List["MerkmalRelationOfThePropertyIdentifiersInTheInterconnectedDictionariesItem"]
    ] = UNSET
    creators_language: Union[Unset, "MerkmalCreatorsLanguage"] = UNSET
    names_in_language: Union[Unset, List["MerkmalNamesInLanguageItem"]] = UNSET
    definitions_in_language: Union[Unset, List["MerkmalDefinitionsInLanguageItem"]] = UNSET
    descriptions_in_language: Union[Unset, List["MerkmalDescriptionsInLanguageItem"]] = UNSET
    examples_in_language: Union[Unset, List["MerkmalExamplesInLanguageItem"]] = UNSET
    connected_properties: Union[Unset, List["MerkmalConnectedPropertiesItem"]] = UNSET
    group_of_properties: Union[Unset, List["MerkmalGroupOfPropertiesItem"]] = UNSET
    symbols_of_the_property_in_a_given_property_group: Union[
        Unset, List["MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem"]
    ] = UNSET
    visual_representations: Union[Unset, List[str]] = UNSET
    country_of_use: Union[Unset, List[str]] = UNSET
    subdivision_of_use: Union[Unset, List[str]] = UNSET
    country_of_origin: Union[Unset, str] = UNSET
    physical_quantity: Union[Unset, List["MerkmalPhysicalQuantityItem"]] = UNSET
    dimension: Union[Unset, str] = UNSET
    method_of_measurement: Union[Unset, str] = UNSET
    data_type: Union[Unset, str] = UNSET
    dynamic_property: Union[Unset, str] = UNSET
    parameters_of_the_dynamic_property: Union[Unset, List["MerkmalParametersOfTheDynamicPropertyItem"]] = UNSET
    units: Union[Unset, List[str]] = UNSET
    names_of_the_defining_values: Union[Unset, List["MerkmalNamesOfTheDefiningValuesItem"]] = UNSET
    defining_values: Union[Unset, List[str]] = UNSET
    tolerance: Union[Unset, List[int]] = UNSET
    digital_format: Union[Unset, List["MerkmalDigitalFormatItem"]] = UNSET
    text_format: Union[Unset, "MerkmalTextFormat"] = UNSET
    list_of_possible_values_in_language: Union[Unset, List["MerkmalListOfPossibleValuesInLanguageItem"]] = UNSET
    boundary_values: Union[Unset, List["MerkmalBoundaryValuesItem"]] = UNSET
    metadata: Union[Unset, "MerkmalMetadata"] = UNSET
    bookmarked: Union[Unset, "MerkmalBookmarked"] = UNSET
    observed: Union[Unset, "MerkmalObserved"] = UNSET
    organisation_id: Union[Unset, str] = UNSET
    organisation_name: Union[Unset, str] = UNSET
    tags: Union[Unset, List["MerkmalTagsItem"]] = UNSET
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

        relation_of_the_property_identifiers_in_the_interconnected_dictionaries: Union[Unset, List[Dict[str, Any]]] = (
            UNSET
        )
        if not isinstance(self.relation_of_the_property_identifiers_in_the_interconnected_dictionaries, Unset):
            relation_of_the_property_identifiers_in_the_interconnected_dictionaries = []
            for (
                relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item_data
            ) in self.relation_of_the_property_identifiers_in_the_interconnected_dictionaries:
                relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item = (
                    relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item_data.to_dict()
                )
                relation_of_the_property_identifiers_in_the_interconnected_dictionaries.append(
                    relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item
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

        descriptions_in_language: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.descriptions_in_language, Unset):
            descriptions_in_language = []
            for descriptions_in_language_item_data in self.descriptions_in_language:
                descriptions_in_language_item = descriptions_in_language_item_data.to_dict()
                descriptions_in_language.append(descriptions_in_language_item)

        examples_in_language: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.examples_in_language, Unset):
            examples_in_language = []
            for examples_in_language_item_data in self.examples_in_language:
                examples_in_language_item = examples_in_language_item_data.to_dict()
                examples_in_language.append(examples_in_language_item)

        connected_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.connected_properties, Unset):
            connected_properties = []
            for connected_properties_item_data in self.connected_properties:
                connected_properties_item = connected_properties_item_data.to_dict()
                connected_properties.append(connected_properties_item)

        group_of_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_of_properties, Unset):
            group_of_properties = []
            for group_of_properties_item_data in self.group_of_properties:
                group_of_properties_item = group_of_properties_item_data.to_dict()
                group_of_properties.append(group_of_properties_item)

        symbols_of_the_property_in_a_given_property_group: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.symbols_of_the_property_in_a_given_property_group, Unset):
            symbols_of_the_property_in_a_given_property_group = []
            for (
                symbols_of_the_property_in_a_given_property_group_item_data
            ) in self.symbols_of_the_property_in_a_given_property_group:
                symbols_of_the_property_in_a_given_property_group_item = (
                    symbols_of_the_property_in_a_given_property_group_item_data.to_dict()
                )
                symbols_of_the_property_in_a_given_property_group.append(
                    symbols_of_the_property_in_a_given_property_group_item
                )

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

        physical_quantity: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.physical_quantity, Unset):
            physical_quantity = []
            for physical_quantity_item_data in self.physical_quantity:
                physical_quantity_item = physical_quantity_item_data.to_dict()
                physical_quantity.append(physical_quantity_item)

        dimension = self.dimension

        method_of_measurement = self.method_of_measurement

        data_type = self.data_type

        dynamic_property = self.dynamic_property

        parameters_of_the_dynamic_property: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters_of_the_dynamic_property, Unset):
            parameters_of_the_dynamic_property = []
            for parameters_of_the_dynamic_property_item_data in self.parameters_of_the_dynamic_property:
                parameters_of_the_dynamic_property_item = parameters_of_the_dynamic_property_item_data.to_dict()
                parameters_of_the_dynamic_property.append(parameters_of_the_dynamic_property_item)

        units: Union[Unset, List[str]] = UNSET
        if not isinstance(self.units, Unset):
            units = self.units

        names_of_the_defining_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.names_of_the_defining_values, Unset):
            names_of_the_defining_values = []
            for names_of_the_defining_values_item_data in self.names_of_the_defining_values:
                names_of_the_defining_values_item = names_of_the_defining_values_item_data.to_dict()
                names_of_the_defining_values.append(names_of_the_defining_values_item)

        defining_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.defining_values, Unset):
            defining_values = self.defining_values

        tolerance: Union[Unset, List[int]] = UNSET
        if not isinstance(self.tolerance, Unset):
            tolerance = self.tolerance

        digital_format: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.digital_format, Unset):
            digital_format = []
            for digital_format_item_data in self.digital_format:
                digital_format_item = digital_format_item_data.to_dict()
                digital_format.append(digital_format_item)

        text_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.text_format, Unset):
            text_format = self.text_format.to_dict()

        list_of_possible_values_in_language: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.list_of_possible_values_in_language, Unset):
            list_of_possible_values_in_language = []
            for list_of_possible_values_in_language_item_data in self.list_of_possible_values_in_language:
                list_of_possible_values_in_language_item = list_of_possible_values_in_language_item_data.to_dict()
                list_of_possible_values_in_language.append(list_of_possible_values_in_language_item)

        boundary_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.boundary_values, Unset):
            boundary_values = []
            for boundary_values_item_data in self.boundary_values:
                boundary_values_item = boundary_values_item_data.to_dict()
                boundary_values.append(boundary_values_item)

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        bookmarked: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bookmarked, Unset):
            bookmarked = self.bookmarked.to_dict()

        observed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.observed, Unset):
            observed = self.observed.to_dict()

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
        if relation_of_the_property_identifiers_in_the_interconnected_dictionaries is not UNSET:
            field_dict["relationOfThePropertyIdentifiersInTheInterconnectedDictionaries"] = (
                relation_of_the_property_identifiers_in_the_interconnected_dictionaries
            )
        if creators_language is not UNSET:
            field_dict["creatorsLanguage"] = creators_language
        if names_in_language is not UNSET:
            field_dict["namesInLanguage"] = names_in_language
        if definitions_in_language is not UNSET:
            field_dict["definitionsInLanguage"] = definitions_in_language
        if descriptions_in_language is not UNSET:
            field_dict["descriptionsInLanguage"] = descriptions_in_language
        if examples_in_language is not UNSET:
            field_dict["examplesInLanguage"] = examples_in_language
        if connected_properties is not UNSET:
            field_dict["connectedProperties"] = connected_properties
        if group_of_properties is not UNSET:
            field_dict["groupOfProperties"] = group_of_properties
        if symbols_of_the_property_in_a_given_property_group is not UNSET:
            field_dict["symbolsOfThePropertyInAGivenPropertyGroup"] = symbols_of_the_property_in_a_given_property_group
        if visual_representations is not UNSET:
            field_dict["visualRepresentations"] = visual_representations
        if country_of_use is not UNSET:
            field_dict["countryOfUse"] = country_of_use
        if subdivision_of_use is not UNSET:
            field_dict["subdivisionOfUse"] = subdivision_of_use
        if country_of_origin is not UNSET:
            field_dict["countryOfOrigin"] = country_of_origin
        if physical_quantity is not UNSET:
            field_dict["physicalQuantity"] = physical_quantity
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if method_of_measurement is not UNSET:
            field_dict["methodOfMeasurement"] = method_of_measurement
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if dynamic_property is not UNSET:
            field_dict["dynamicProperty"] = dynamic_property
        if parameters_of_the_dynamic_property is not UNSET:
            field_dict["parametersOfTheDynamicProperty"] = parameters_of_the_dynamic_property
        if units is not UNSET:
            field_dict["units"] = units
        if names_of_the_defining_values is not UNSET:
            field_dict["namesOfTheDefiningValues"] = names_of_the_defining_values
        if defining_values is not UNSET:
            field_dict["definingValues"] = defining_values
        if tolerance is not UNSET:
            field_dict["tolerance"] = tolerance
        if digital_format is not UNSET:
            field_dict["digitalFormat"] = digital_format
        if text_format is not UNSET:
            field_dict["textFormat"] = text_format
        if list_of_possible_values_in_language is not UNSET:
            field_dict["listOfPossibleValuesInLanguage"] = list_of_possible_values_in_language
        if boundary_values is not UNSET:
            field_dict["boundaryValues"] = boundary_values
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if bookmarked is not UNSET:
            field_dict["bookmarked"] = bookmarked
        if observed is not UNSET:
            field_dict["observed"] = observed
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
        from ..models.merkmal_bookmarked import MerkmalBookmarked
        from ..models.merkmal_boundary_values_item import MerkmalBoundaryValuesItem
        from ..models.merkmal_connected_properties_item import MerkmalConnectedPropertiesItem
        from ..models.merkmal_creators_language import MerkmalCreatorsLanguage
        from ..models.merkmal_definitions_in_language_item import MerkmalDefinitionsInLanguageItem
        from ..models.merkmal_descriptions_in_language_item import MerkmalDescriptionsInLanguageItem
        from ..models.merkmal_digital_format_item import MerkmalDigitalFormatItem
        from ..models.merkmal_examples_in_language_item import MerkmalExamplesInLanguageItem
        from ..models.merkmal_group_of_properties_item import MerkmalGroupOfPropertiesItem
        from ..models.merkmal_list_of_possible_values_in_language_item import MerkmalListOfPossibleValuesInLanguageItem
        from ..models.merkmal_metadata import MerkmalMetadata
        from ..models.merkmal_names_in_language_item import MerkmalNamesInLanguageItem
        from ..models.merkmal_names_of_the_defining_values_item import MerkmalNamesOfTheDefiningValuesItem
        from ..models.merkmal_observed import MerkmalObserved
        from ..models.merkmal_parameters_of_the_dynamic_property_item import MerkmalParametersOfTheDynamicPropertyItem
        from ..models.merkmal_physical_quantity_item import MerkmalPhysicalQuantityItem
        from ..models.merkmal_relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item import (
            MerkmalRelationOfThePropertyIdentifiersInTheInterconnectedDictionariesItem,
        )
        from ..models.merkmal_replaced_by_item import MerkmalReplacedByItem
        from ..models.merkmal_replaces_item import MerkmalReplacesItem
        from ..models.merkmal_symbols_of_the_property_in_a_given_property_group_item import (
            MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem,
        )
        from ..models.merkmal_tags_item import MerkmalTagsItem
        from ..models.merkmal_text_format import MerkmalTextFormat

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
            replaces_item = MerkmalReplacesItem.from_dict(replaces_item_data)

            replaces.append(replaces_item)

        replaced_by = []
        _replaced_by = d.pop("replacedBy", UNSET)
        for replaced_by_item_data in _replaced_by or []:
            replaced_by_item = MerkmalReplacedByItem.from_dict(replaced_by_item_data)

            replaced_by.append(replaced_by_item)

        deprecation_explanation = d.pop("deprecationExplanation", UNSET)

        relation_of_the_property_identifiers_in_the_interconnected_dictionaries = []
        _relation_of_the_property_identifiers_in_the_interconnected_dictionaries = d.pop(
            "relationOfThePropertyIdentifiersInTheInterconnectedDictionaries", UNSET
        )
        for relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item_data in (
            _relation_of_the_property_identifiers_in_the_interconnected_dictionaries or []
        ):
            relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item = (
                MerkmalRelationOfThePropertyIdentifiersInTheInterconnectedDictionariesItem.from_dict(
                    relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item_data
                )
            )

            relation_of_the_property_identifiers_in_the_interconnected_dictionaries.append(
                relation_of_the_property_identifiers_in_the_interconnected_dictionaries_item
            )

        _creators_language = d.pop("creatorsLanguage", UNSET)
        creators_language: Union[Unset, MerkmalCreatorsLanguage]
        if isinstance(_creators_language, Unset):
            creators_language = UNSET
        else:
            creators_language = MerkmalCreatorsLanguage.from_dict(_creators_language)

        names_in_language = []
        _names_in_language = d.pop("namesInLanguage", UNSET)
        for names_in_language_item_data in _names_in_language or []:
            names_in_language_item = MerkmalNamesInLanguageItem.from_dict(names_in_language_item_data)

            names_in_language.append(names_in_language_item)

        definitions_in_language = []
        _definitions_in_language = d.pop("definitionsInLanguage", UNSET)
        for definitions_in_language_item_data in _definitions_in_language or []:
            definitions_in_language_item = MerkmalDefinitionsInLanguageItem.from_dict(definitions_in_language_item_data)

            definitions_in_language.append(definitions_in_language_item)

        descriptions_in_language = []
        _descriptions_in_language = d.pop("descriptionsInLanguage", UNSET)
        for descriptions_in_language_item_data in _descriptions_in_language or []:
            descriptions_in_language_item = MerkmalDescriptionsInLanguageItem.from_dict(
                descriptions_in_language_item_data
            )

            descriptions_in_language.append(descriptions_in_language_item)

        examples_in_language = []
        _examples_in_language = d.pop("examplesInLanguage", UNSET)
        for examples_in_language_item_data in _examples_in_language or []:
            examples_in_language_item = MerkmalExamplesInLanguageItem.from_dict(examples_in_language_item_data)

            examples_in_language.append(examples_in_language_item)

        connected_properties = []
        _connected_properties = d.pop("connectedProperties", UNSET)
        for connected_properties_item_data in _connected_properties or []:
            connected_properties_item = MerkmalConnectedPropertiesItem.from_dict(connected_properties_item_data)

            connected_properties.append(connected_properties_item)

        group_of_properties = []
        _group_of_properties = d.pop("groupOfProperties", UNSET)
        for group_of_properties_item_data in _group_of_properties or []:
            group_of_properties_item = MerkmalGroupOfPropertiesItem.from_dict(group_of_properties_item_data)

            group_of_properties.append(group_of_properties_item)

        symbols_of_the_property_in_a_given_property_group = []
        _symbols_of_the_property_in_a_given_property_group = d.pop("symbolsOfThePropertyInAGivenPropertyGroup", UNSET)
        for symbols_of_the_property_in_a_given_property_group_item_data in (
            _symbols_of_the_property_in_a_given_property_group or []
        ):
            symbols_of_the_property_in_a_given_property_group_item = (
                MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem.from_dict(
                    symbols_of_the_property_in_a_given_property_group_item_data
                )
            )

            symbols_of_the_property_in_a_given_property_group.append(
                symbols_of_the_property_in_a_given_property_group_item
            )

        visual_representations = cast(List[str], d.pop("visualRepresentations", UNSET))

        country_of_use = cast(List[str], d.pop("countryOfUse", UNSET))

        subdivision_of_use = cast(List[str], d.pop("subdivisionOfUse", UNSET))

        country_of_origin = d.pop("countryOfOrigin", UNSET)

        physical_quantity = []
        _physical_quantity = d.pop("physicalQuantity", UNSET)
        for physical_quantity_item_data in _physical_quantity or []:
            physical_quantity_item = MerkmalPhysicalQuantityItem.from_dict(physical_quantity_item_data)

            physical_quantity.append(physical_quantity_item)

        dimension = d.pop("dimension", UNSET)

        method_of_measurement = d.pop("methodOfMeasurement", UNSET)

        data_type = d.pop("dataType", UNSET)

        dynamic_property = d.pop("dynamicProperty", UNSET)

        parameters_of_the_dynamic_property = []
        _parameters_of_the_dynamic_property = d.pop("parametersOfTheDynamicProperty", UNSET)
        for parameters_of_the_dynamic_property_item_data in _parameters_of_the_dynamic_property or []:
            parameters_of_the_dynamic_property_item = MerkmalParametersOfTheDynamicPropertyItem.from_dict(
                parameters_of_the_dynamic_property_item_data
            )

            parameters_of_the_dynamic_property.append(parameters_of_the_dynamic_property_item)

        units = cast(List[str], d.pop("units", UNSET))

        names_of_the_defining_values = []
        _names_of_the_defining_values = d.pop("namesOfTheDefiningValues", UNSET)
        for names_of_the_defining_values_item_data in _names_of_the_defining_values or []:
            names_of_the_defining_values_item = MerkmalNamesOfTheDefiningValuesItem.from_dict(
                names_of_the_defining_values_item_data
            )

            names_of_the_defining_values.append(names_of_the_defining_values_item)

        defining_values = cast(List[str], d.pop("definingValues", UNSET))

        tolerance = cast(List[int], d.pop("tolerance", UNSET))

        digital_format = []
        _digital_format = d.pop("digitalFormat", UNSET)
        for digital_format_item_data in _digital_format or []:
            digital_format_item = MerkmalDigitalFormatItem.from_dict(digital_format_item_data)

            digital_format.append(digital_format_item)

        _text_format = d.pop("textFormat", UNSET)
        text_format: Union[Unset, MerkmalTextFormat]
        if isinstance(_text_format, Unset):
            text_format = UNSET
        else:
            text_format = MerkmalTextFormat.from_dict(_text_format)

        list_of_possible_values_in_language = []
        _list_of_possible_values_in_language = d.pop("listOfPossibleValuesInLanguage", UNSET)
        for list_of_possible_values_in_language_item_data in _list_of_possible_values_in_language or []:
            list_of_possible_values_in_language_item = MerkmalListOfPossibleValuesInLanguageItem.from_dict(
                list_of_possible_values_in_language_item_data
            )

            list_of_possible_values_in_language.append(list_of_possible_values_in_language_item)

        boundary_values = []
        _boundary_values = d.pop("boundaryValues", UNSET)
        for boundary_values_item_data in _boundary_values or []:
            boundary_values_item = MerkmalBoundaryValuesItem.from_dict(boundary_values_item_data)

            boundary_values.append(boundary_values_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, MerkmalMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = MerkmalMetadata.from_dict(_metadata)

        _bookmarked = d.pop("bookmarked", UNSET)
        bookmarked: Union[Unset, MerkmalBookmarked]
        if isinstance(_bookmarked, Unset):
            bookmarked = UNSET
        else:
            bookmarked = MerkmalBookmarked.from_dict(_bookmarked)

        _observed = d.pop("observed", UNSET)
        observed: Union[Unset, MerkmalObserved]
        if isinstance(_observed, Unset):
            observed = UNSET
        else:
            observed = MerkmalObserved.from_dict(_observed)

        organisation_id = d.pop("organisationId", UNSET)

        organisation_name = d.pop("organisationName", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = MerkmalTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        organisation_type = d.pop("organisationType", UNSET)

        can_create_new_version = d.pop("canCreateNewVersion", UNSET)

        merkmal = cls(
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
            relation_of_the_property_identifiers_in_the_interconnected_dictionaries=relation_of_the_property_identifiers_in_the_interconnected_dictionaries,
            creators_language=creators_language,
            names_in_language=names_in_language,
            definitions_in_language=definitions_in_language,
            descriptions_in_language=descriptions_in_language,
            examples_in_language=examples_in_language,
            connected_properties=connected_properties,
            group_of_properties=group_of_properties,
            symbols_of_the_property_in_a_given_property_group=symbols_of_the_property_in_a_given_property_group,
            visual_representations=visual_representations,
            country_of_use=country_of_use,
            subdivision_of_use=subdivision_of_use,
            country_of_origin=country_of_origin,
            physical_quantity=physical_quantity,
            dimension=dimension,
            method_of_measurement=method_of_measurement,
            data_type=data_type,
            dynamic_property=dynamic_property,
            parameters_of_the_dynamic_property=parameters_of_the_dynamic_property,
            units=units,
            names_of_the_defining_values=names_of_the_defining_values,
            defining_values=defining_values,
            tolerance=tolerance,
            digital_format=digital_format,
            text_format=text_format,
            list_of_possible_values_in_language=list_of_possible_values_in_language,
            boundary_values=boundary_values,
            metadata=metadata,
            bookmarked=bookmarked,
            observed=observed,
            organisation_id=organisation_id,
            organisation_name=organisation_name,
            tags=tags,
            organisation_type=organisation_type,
            can_create_new_version=can_create_new_version,
        )

        merkmal.additional_properties = d
        return merkmal

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
