from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalsgruppeBookmarked")


@_attrs_define
class MerkmalsgruppeBookmarked:
    """
    Attributes:
        bookmark_id (Union[Unset, str]):
    """

    bookmark_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bookmark_id = self.bookmark_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bookmark_id is not UNSET:
            field_dict["bookmarkId"] = bookmark_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bookmark_id = d.pop("bookmarkId", UNSET)

        merkmalsgruppe_bookmarked = cls(
            bookmark_id=bookmark_id,
        )

        merkmalsgruppe_bookmarked.additional_properties = d
        return merkmalsgruppe_bookmarked

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
