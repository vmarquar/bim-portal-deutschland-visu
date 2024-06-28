from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalsgruppeReplacedByItemNamesInLanguageItem")


@_attrs_define
class MerkmalsgruppeReplacedByItemNamesInLanguageItem:
    """
    Attributes:
        name (Union[Unset, str]):
        language (Union[Unset, str]):
        language_name (Union[Unset, str]):
        country_name (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    language_name: Union[Unset, str] = UNSET
    country_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        language = self.language

        language_name = self.language_name

        country_name = self.country_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if language is not UNSET:
            field_dict["language"] = language
        if language_name is not UNSET:
            field_dict["languageName"] = language_name
        if country_name is not UNSET:
            field_dict["countryName"] = country_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        language = d.pop("language", UNSET)

        language_name = d.pop("languageName", UNSET)

        country_name = d.pop("countryName", UNSET)

        merkmalsgruppe_replaced_by_item_names_in_language_item = cls(
            name=name,
            language=language,
            language_name=language_name,
            country_name=country_name,
        )

        merkmalsgruppe_replaced_by_item_names_in_language_item.additional_properties = d
        return merkmalsgruppe_replaced_by_item_names_in_language_item

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
