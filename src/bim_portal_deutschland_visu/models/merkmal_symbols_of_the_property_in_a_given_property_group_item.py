from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merkmal_symbols_of_the_property_in_a_given_property_group_item_group_names_item import (
        MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItemGroupNamesItem,
    )


T = TypeVar("T", bound="MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem")


@_attrs_define
class MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItem:
    """
    Attributes:
        symbol (Union[Unset, str]):
        prop_group_id (Union[Unset, str]):
        group_names (Union[Unset, List['MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItemGroupNamesItem']]):
    """

    symbol: Union[Unset, str] = UNSET
    prop_group_id: Union[Unset, str] = UNSET
    group_names: Union[Unset, List["MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItemGroupNamesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        symbol = self.symbol

        prop_group_id = self.prop_group_id

        group_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_names, Unset):
            group_names = []
            for group_names_item_data in self.group_names:
                group_names_item = group_names_item_data.to_dict()
                group_names.append(group_names_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if prop_group_id is not UNSET:
            field_dict["propGroupID"] = prop_group_id
        if group_names is not UNSET:
            field_dict["groupNames"] = group_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.merkmal_symbols_of_the_property_in_a_given_property_group_item_group_names_item import (
            MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItemGroupNamesItem,
        )

        d = src_dict.copy()
        symbol = d.pop("symbol", UNSET)

        prop_group_id = d.pop("propGroupID", UNSET)

        group_names = []
        _group_names = d.pop("groupNames", UNSET)
        for group_names_item_data in _group_names or []:
            group_names_item = MerkmalSymbolsOfThePropertyInAGivenPropertyGroupItemGroupNamesItem.from_dict(
                group_names_item_data
            )

            group_names.append(group_names_item)

        merkmal_symbols_of_the_property_in_a_given_property_group_item = cls(
            symbol=symbol,
            prop_group_id=prop_group_id,
            group_names=group_names,
        )

        merkmal_symbols_of_the_property_in_a_given_property_group_item.additional_properties = d
        return merkmal_symbols_of_the_property_in_a_given_property_group_item

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
