from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries")


@_attrs_define
class MerkmalsgruppeRelationOfThePropertyGroupIdentifiersInTheInterconnectedDictionaries:
    """Liste von Paaren (inter-ner Bezeichner der Merkmalsgruppe, ent-sprechender Daten-katalog-Bezeichner) dieses Attribut
    sollte für die Kompatibilität zwischen bereits vorhandenen Merk-malsgruppen verwen-det werden

        Attributes:
            id (Union[Unset, str]):
            version (Union[Unset, int]):
            created_date (Union[Unset, str]):
            prop_group_id (Union[Unset, str]):
            inter_con_dict_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    created_date: Union[Unset, str] = UNSET
    prop_group_id: Union[Unset, str] = UNSET
    inter_con_dict_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        version = self.version

        created_date = self.created_date

        prop_group_id = self.prop_group_id

        inter_con_dict_id = self.inter_con_dict_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if prop_group_id is not UNSET:
            field_dict["propGroupID"] = prop_group_id
        if inter_con_dict_id is not UNSET:
            field_dict["interConDictID"] = inter_con_dict_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        created_date = d.pop("createdDate", UNSET)

        prop_group_id = d.pop("propGroupID", UNSET)

        inter_con_dict_id = d.pop("interConDictID", UNSET)

        merkmalsgruppe_relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries = cls(
            id=id,
            version=version,
            created_date=created_date,
            prop_group_id=prop_group_id,
            inter_con_dict_id=inter_con_dict_id,
        )

        merkmalsgruppe_relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries.additional_properties = d
        return merkmalsgruppe_relation_of_the_property_group_identifiers_in_the_interconnected_dictionaries

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
