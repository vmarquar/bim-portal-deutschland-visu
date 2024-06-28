from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalTextFormat")


@_attrs_define
class MerkmalTextFormat:
    """Paar für den Texttyp (Ver-schlüsselung, Anzahl der Zeichen) die Verschlüsselung wird nach „Name der Codierungsnorm“
    von IANA, RFC 2978 festgelegt

        Attributes:
            encoding (Union[Unset, str]):
            number_of_characters (Union[Unset, str]):
    """

    encoding: Union[Unset, str] = UNSET
    number_of_characters: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        encoding = self.encoding

        number_of_characters = self.number_of_characters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if number_of_characters is not UNSET:
            field_dict["numberOfCharacters"] = number_of_characters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        encoding = d.pop("encoding", UNSET)

        number_of_characters = d.pop("numberOfCharacters", UNSET)

        merkmal_text_format = cls(
            encoding=encoding,
            number_of_characters=number_of_characters,
        )

        merkmal_text_format.additional_properties = d
        return merkmal_text_format

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
