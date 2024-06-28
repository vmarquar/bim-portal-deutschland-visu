from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merkmal_connected_properties_item_names_in_language_item import (
        MerkmalConnectedPropertiesItemNamesInLanguageItem,
    )


T = TypeVar("T", bound="MerkmalConnectedPropertiesItem")


@_attrs_define
class MerkmalConnectedPropertiesItem:
    """
    Attributes:
        id (Union[Unset, str]):
        names_in_language (Union[Unset, List['MerkmalConnectedPropertiesItemNamesInLanguageItem']]):
        version_number (Union[Unset, int]):
        revision_number (Union[Unset, int]):
        property_status (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    names_in_language: Union[Unset, List["MerkmalConnectedPropertiesItemNamesInLanguageItem"]] = UNSET
    version_number: Union[Unset, int] = UNSET
    revision_number: Union[Unset, int] = UNSET
    property_status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        names_in_language: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.names_in_language, Unset):
            names_in_language = []
            for names_in_language_item_data in self.names_in_language:
                names_in_language_item = names_in_language_item_data.to_dict()
                names_in_language.append(names_in_language_item)

        version_number = self.version_number

        revision_number = self.revision_number

        property_status = self.property_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if names_in_language is not UNSET:
            field_dict["namesInLanguage"] = names_in_language
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number
        if revision_number is not UNSET:
            field_dict["revisionNumber"] = revision_number
        if property_status is not UNSET:
            field_dict["propertyStatus"] = property_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.merkmal_connected_properties_item_names_in_language_item import (
            MerkmalConnectedPropertiesItemNamesInLanguageItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        names_in_language = []
        _names_in_language = d.pop("namesInLanguage", UNSET)
        for names_in_language_item_data in _names_in_language or []:
            names_in_language_item = MerkmalConnectedPropertiesItemNamesInLanguageItem.from_dict(
                names_in_language_item_data
            )

            names_in_language.append(names_in_language_item)

        version_number = d.pop("versionNumber", UNSET)

        revision_number = d.pop("revisionNumber", UNSET)

        property_status = d.pop("propertyStatus", UNSET)

        merkmal_connected_properties_item = cls(
            id=id,
            names_in_language=names_in_language,
            version_number=version_number,
            revision_number=revision_number,
            property_status=property_status,
        )

        merkmal_connected_properties_item.additional_properties = d
        return merkmal_connected_properties_item

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
