from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalsgruppeCreatorsLanguage")


@_attrs_define
class MerkmalsgruppeCreatorsLanguage:
    """Sprache des Erstellers der Merkmalsgruppe

    Attributes:
        code (Union[Unset, str]):
        language (Union[Unset, str]):
        country (Union[Unset, str]):
    """

    code: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        language = self.language

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if language is not UNSET:
            field_dict["language"] = language
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        language = d.pop("language", UNSET)

        country = d.pop("country", UNSET)

        merkmalsgruppe_creators_language = cls(
            code=code,
            language=language,
            country=country,
        )

        merkmalsgruppe_creators_language.additional_properties = d
        return merkmalsgruppe_creators_language

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
