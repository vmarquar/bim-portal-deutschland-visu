from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merkmalsgruppe_tags_item_tag import MerkmalsgruppeTagsItemTag


T = TypeVar("T", bound="MerkmalsgruppeTagsItem")


@_attrs_define
class MerkmalsgruppeTagsItem:
    """
    Attributes:
        tag (Union[Unset, MerkmalsgruppeTagsItemTag]):
        organisation_id (Union[Unset, str]):
    """

    tag: Union[Unset, "MerkmalsgruppeTagsItemTag"] = UNSET
    organisation_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        organisation_id = self.organisation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag is not UNSET:
            field_dict["tag"] = tag
        if organisation_id is not UNSET:
            field_dict["organisationId"] = organisation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.merkmalsgruppe_tags_item_tag import MerkmalsgruppeTagsItemTag

        d = src_dict.copy()
        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, MerkmalsgruppeTagsItemTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = MerkmalsgruppeTagsItemTag.from_dict(_tag)

        organisation_id = d.pop("organisationId", UNSET)

        merkmalsgruppe_tags_item = cls(
            tag=tag,
            organisation_id=organisation_id,
        )

        merkmalsgruppe_tags_item.additional_properties = d
        return merkmalsgruppe_tags_item

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
