from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalMetadata")


@_attrs_define
class MerkmalMetadata:
    """
    Attributes:
        status (Union[Unset, str]):
        visibility (Union[Unset, str]):
        external (Union[Unset, bool]):
        organisation_id (Union[Unset, str]):
        transferred (Union[Unset, bool]):
    """

    status: Union[Unset, str] = UNSET
    visibility: Union[Unset, str] = UNSET
    external: Union[Unset, bool] = UNSET
    organisation_id: Union[Unset, str] = UNSET
    transferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        visibility = self.visibility

        external = self.external

        organisation_id = self.organisation_id

        transferred = self.transferred

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if external is not UNSET:
            field_dict["external"] = external
        if organisation_id is not UNSET:
            field_dict["organisationId"] = organisation_id
        if transferred is not UNSET:
            field_dict["transferred"] = transferred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        visibility = d.pop("visibility", UNSET)

        external = d.pop("external", UNSET)

        organisation_id = d.pop("organisationId", UNSET)

        transferred = d.pop("transferred", UNSET)

        merkmal_metadata = cls(
            status=status,
            visibility=visibility,
            external=external,
            organisation_id=organisation_id,
            transferred=transferred,
        )

        merkmal_metadata.additional_properties = d
        return merkmal_metadata

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
