from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalPhysicalQuantityItem")


@_attrs_define
class MerkmalPhysicalQuantityItem:
    """
    Attributes:
        id (Union[Unset, str]):
        version (Union[Unset, int]):
        creation_date (Union[Unset, str]):
        si_unit (Union[Unset, str]):
        language (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    creation_date: Union[Unset, str] = UNSET
    si_unit: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        version = self.version

        creation_date = self.creation_date

        si_unit = self.si_unit

        language = self.language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if si_unit is not UNSET:
            field_dict["siUnit"] = si_unit
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        creation_date = d.pop("creationDate", UNSET)

        si_unit = d.pop("siUnit", UNSET)

        language = d.pop("language", UNSET)

        merkmal_physical_quantity_item = cls(
            id=id,
            version=version,
            creation_date=creation_date,
            si_unit=si_unit,
            language=language,
        )

        merkmal_physical_quantity_item.additional_properties = d
        return merkmal_physical_quantity_item

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
