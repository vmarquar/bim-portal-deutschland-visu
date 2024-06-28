from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalDigitalFormatItem")


@_attrs_define
class MerkmalDigitalFormatItem:
    """
    Attributes:
        id (Union[Unset, str]):
        version (Union[Unset, int]):
        created_date (Union[Unset, str]):
        precision (Union[Unset, str]):
        unit_of_measure (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    created_date: Union[Unset, str] = UNSET
    precision: Union[Unset, str] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        version = self.version

        created_date = self.created_date

        precision = self.precision

        unit_of_measure = self.unit_of_measure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if precision is not UNSET:
            field_dict["precision"] = precision
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        created_date = d.pop("createdDate", UNSET)

        precision = d.pop("precision", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        merkmal_digital_format_item = cls(
            id=id,
            version=version,
            created_date=created_date,
            precision=precision,
            unit_of_measure=unit_of_measure,
        )

        merkmal_digital_format_item.additional_properties = d
        return merkmal_digital_format_item

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
