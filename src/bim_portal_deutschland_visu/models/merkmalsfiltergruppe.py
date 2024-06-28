from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="Merkmalsfiltergruppe")


@_attrs_define
class Merkmalsfiltergruppe:
    """
    Attributes:
        name (Union[Unset, str]): Name der Merkmalsfiltergruppe Example: Leistungsphasen.
        guid (Union[Unset, str]): Global eindeutiger Identifikator der Merkmalsfiltergruppe Example:
            8e9b9ed6-9704-461b-97af-05e3d61a97f2.
        filter_ (Union[Unset, List['Filter']]):
    """

    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    filter_: Union[Unset, List["Filter"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        guid = self.guid

        filter_: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_ import Filter

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        filter_ = []
        _filter_ = d.pop("filter", UNSET)
        for filter_item_data in _filter_ or []:
            filter_item = Filter.from_dict(filter_item_data)

            filter_.append(filter_item)

        merkmalsfiltergruppe = cls(
            name=name,
            guid=guid,
            filter_=filter_,
        )

        merkmalsfiltergruppe.additional_properties = d
        return merkmalsfiltergruppe

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
