from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalBoundaryValuesItem")


@_attrs_define
class MerkmalBoundaryValuesItem:
    """
    Attributes:
        id (Union[Unset, str]):
        version (Union[Unset, int]):
        created_date (Union[Unset, str]):
        boundary_value_pairs (Union[Unset, List[str]]):
        unit (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    created_date: Union[Unset, str] = UNSET
    boundary_value_pairs: Union[Unset, List[str]] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        version = self.version

        created_date = self.created_date

        boundary_value_pairs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.boundary_value_pairs, Unset):
            boundary_value_pairs = self.boundary_value_pairs

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if boundary_value_pairs is not UNSET:
            field_dict["boundaryValuePairs"] = boundary_value_pairs
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        created_date = d.pop("createdDate", UNSET)

        boundary_value_pairs = cast(List[str], d.pop("boundaryValuePairs", UNSET))

        unit = d.pop("unit", UNSET)

        merkmal_boundary_values_item = cls(
            id=id,
            version=version,
            created_date=created_date,
            boundary_value_pairs=boundary_value_pairs,
            unit=unit,
        )

        merkmal_boundary_values_item.additional_properties = d
        return merkmal_boundary_values_item

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
