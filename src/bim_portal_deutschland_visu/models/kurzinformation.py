from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Kurzinformation")


@_attrs_define
class Kurzinformation:
    """
    Attributes:
        name (Union[Unset, str]): Name des Informationslements
        definition (Union[Unset, str]): Defintion des Informationslements
        guid (Union[Unset, str]): Global eindeutiger Identifikator des Informationslements
        version_number (Union[Unset, int]): Versionsnummer des Informationslements
        revision_number (Union[Unset, int]): Revisionsnummer des Informationslements.
        parent_guids (Union[Unset, List[str]]): Liste der Elterngruppe(n) des Informationslements. Im Falle eines
            Merkmals kann dise Liste mehrere Elemente enthalten. Im Fall einer Merkmalsgruppe enthält diese Liste maximal
            ein Element.
        organisation_name (Union[Unset, str]): Name der Organisation zu dem das Informationslement gehört
        data_type (Union[Unset, str]): Datentyp des Merkmals. Im Falle einer Merkmalsgruppe ist dieser Wert leer.
        units (Union[Unset, List[str]]): Einheit(en) des Merkmals. Im Falle einer Merkmalsgruppe ist dieser Wert leer.
        category (Union[Unset, str]): Kategorie der Merkmalsgruppe. Im Falle eines Merkmals ist dieser Wert leer.
        deprecated (Union[Unset, bool]): Ein Wahrheitswert der angibt, ob das zurückgelieferte Informationselement
            veraltet ist oder nicht.
    """

    name: Union[Unset, str] = UNSET
    definition: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    version_number: Union[Unset, int] = UNSET
    revision_number: Union[Unset, int] = UNSET
    parent_guids: Union[Unset, List[str]] = UNSET
    organisation_name: Union[Unset, str] = UNSET
    data_type: Union[Unset, str] = UNSET
    units: Union[Unset, List[str]] = UNSET
    category: Union[Unset, str] = UNSET
    deprecated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        definition = self.definition

        guid = self.guid

        version_number = self.version_number

        revision_number = self.revision_number

        parent_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parent_guids, Unset):
            parent_guids = self.parent_guids

        organisation_name = self.organisation_name

        data_type = self.data_type

        units: Union[Unset, List[str]] = UNSET
        if not isinstance(self.units, Unset):
            units = self.units

        category = self.category

        deprecated = self.deprecated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if definition is not UNSET:
            field_dict["definition"] = definition
        if guid is not UNSET:
            field_dict["guid"] = guid
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number
        if revision_number is not UNSET:
            field_dict["revisionNumber"] = revision_number
        if parent_guids is not UNSET:
            field_dict["parentGuids"] = parent_guids
        if organisation_name is not UNSET:
            field_dict["organisationName"] = organisation_name
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if units is not UNSET:
            field_dict["units"] = units
        if category is not UNSET:
            field_dict["category"] = category
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        definition = d.pop("definition", UNSET)

        guid = d.pop("guid", UNSET)

        version_number = d.pop("versionNumber", UNSET)

        revision_number = d.pop("revisionNumber", UNSET)

        parent_guids = cast(List[str], d.pop("parentGuids", UNSET))

        organisation_name = d.pop("organisationName", UNSET)

        data_type = d.pop("dataType", UNSET)

        units = cast(List[str], d.pop("units", UNSET))

        category = d.pop("category", UNSET)

        deprecated = d.pop("deprecated", UNSET)

        kurzinformation = cls(
            name=name,
            definition=definition,
            guid=guid,
            version_number=version_number,
            revision_number=revision_number,
            parent_guids=parent_guids,
            organisation_name=organisation_name,
            data_type=data_type,
            units=units,
            category=category,
            deprecated=deprecated,
        )

        kurzinformation.additional_properties = d
        return kurzinformation

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
