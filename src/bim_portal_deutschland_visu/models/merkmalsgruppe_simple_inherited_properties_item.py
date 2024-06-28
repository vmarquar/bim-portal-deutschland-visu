from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merkmalsgruppe_simple_inherited_properties_item_names_item import (
        MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem,
    )


T = TypeVar("T", bound="MerkmalsgruppeSimpleInheritedPropertiesItem")


@_attrs_define
class MerkmalsgruppeSimpleInheritedPropertiesItem:
    """
    Attributes:
        id (Union[Unset, str]):
        names (Union[Unset, List['MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem']]):
        version_number (Union[Unset, int]):
        revision_number (Union[Unset, int]):
        property_status (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    names: Union[Unset, List["MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem"]] = UNSET
    version_number: Union[Unset, int] = UNSET
    revision_number: Union[Unset, int] = UNSET
    property_status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.names, Unset):
            names = []
            for names_item_data in self.names:
                names_item = names_item_data.to_dict()
                names.append(names_item)

        version_number = self.version_number

        revision_number = self.revision_number

        property_status = self.property_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if names is not UNSET:
            field_dict["names"] = names
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number
        if revision_number is not UNSET:
            field_dict["revisionNumber"] = revision_number
        if property_status is not UNSET:
            field_dict["propertyStatus"] = property_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.merkmalsgruppe_simple_inherited_properties_item_names_item import (
            MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        names = []
        _names = d.pop("names", UNSET)
        for names_item_data in _names or []:
            names_item = MerkmalsgruppeSimpleInheritedPropertiesItemNamesItem.from_dict(names_item_data)

            names.append(names_item)

        version_number = d.pop("versionNumber", UNSET)

        revision_number = d.pop("revisionNumber", UNSET)

        property_status = d.pop("propertyStatus", UNSET)

        merkmalsgruppe_simple_inherited_properties_item = cls(
            id=id,
            names=names,
            version_number=version_number,
            revision_number=revision_number,
            property_status=property_status,
        )

        merkmalsgruppe_simple_inherited_properties_item.additional_properties = d
        return merkmalsgruppe_simple_inherited_properties_item

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
