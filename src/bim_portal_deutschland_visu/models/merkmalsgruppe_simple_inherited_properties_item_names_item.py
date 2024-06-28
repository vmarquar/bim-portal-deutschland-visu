from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem")


@_attrs_define
class MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem:
    """
    Attributes:
        id (Union[Unset, str]):
        version (Union[Unset, int]):
        created_date (Union[Unset, str]):
        name (Union[Unset, str]):
        language (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    created_date: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        version = self.version

        created_date = self.created_date

        name = self.name

        language = self.language

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if name is not UNSET:
            field_dict["name"] = name
        if language is not UNSET:
            field_dict["language"] = language
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        created_date = d.pop("createdDate", UNSET)

        name = d.pop("name", UNSET)

        language = d.pop("language", UNSET)

        value = d.pop("value", UNSET)

        merkmalsgruppe_simple_inherited_properties_item_names_item = cls(
            id=id,
            version=version,
            created_date=created_date,
            name=name,
            language=language,
            value=value,
        )

        merkmalsgruppe_simple_inherited_properties_item_names_item.additional_properties = d
        return merkmalsgruppe_simple_inherited_properties_item_names_item

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
