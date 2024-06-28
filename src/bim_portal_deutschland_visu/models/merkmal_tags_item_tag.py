from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalTagsItemTag")


@_attrs_define
class MerkmalTagsItemTag:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        organisation_id (Union[Unset, str]):
        global_ (Union[Unset, bool]):
        assignment_count (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    organisation_id: Union[Unset, str] = UNSET
    global_: Union[Unset, bool] = UNSET
    assignment_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        organisation_id = self.organisation_id

        global_ = self.global_

        assignment_count = self.assignment_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if organisation_id is not UNSET:
            field_dict["organisationId"] = organisation_id
        if global_ is not UNSET:
            field_dict["global"] = global_
        if assignment_count is not UNSET:
            field_dict["assignmentCount"] = assignment_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        organisation_id = d.pop("organisationId", UNSET)

        global_ = d.pop("global", UNSET)

        assignment_count = d.pop("assignmentCount", UNSET)

        merkmal_tags_item_tag = cls(
            id=id,
            name=name,
            organisation_id=organisation_id,
            global_=global_,
            assignment_count=assignment_count,
        )

        merkmal_tags_item_tag.additional_properties = d
        return merkmal_tags_item_tag

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
