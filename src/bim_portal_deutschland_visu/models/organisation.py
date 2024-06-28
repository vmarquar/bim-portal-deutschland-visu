from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Organisation")


@_attrs_define
class Organisation:
    """
    Attributes:
        name (Union[Unset, str]): Name der Organisation Example: Pflegestelle Bund.
        description (Union[Unset, str]): Beschreibung der Organisation Example: Organisation für die
            Koordinierungsstelle Bund.
        guid (Union[Unset, str]): Global eindeutiger Identifikator der Organisation Example:
            ee6a7af7-650d-499b-8e32-58a52ffdb7bc.
        parent_guid (Union[Unset, str]): Global eindeutiger Identifikator der Elternorganisation des
            Organisationsobjekts Example: 1f1426b8-099e-46cb-b668-6d931bf29d8c.
        bund_organisation_or_child (Union[Unset, bool]): Ein Wahrheitswert der angibt, ob es sich bei dieser
            Organisation um die Pflegestelle Bund oder um eine Kindorganisation der Pflegestelle handelt. Example: True.
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    parent_guid: Union[Unset, str] = UNSET
    bund_organisation_or_child: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        guid = self.guid

        parent_guid = self.parent_guid

        bund_organisation_or_child = self.bund_organisation_or_child

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if guid is not UNSET:
            field_dict["guid"] = guid
        if parent_guid is not UNSET:
            field_dict["parentGuid"] = parent_guid
        if bund_organisation_or_child is not UNSET:
            field_dict["bundOrganisationOrChild"] = bund_organisation_or_child

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        guid = d.pop("guid", UNSET)

        parent_guid = d.pop("parentGuid", UNSET)

        bund_organisation_or_child = d.pop("bundOrganisationOrChild", UNSET)

        organisation = cls(
            name=name,
            description=description,
            guid=guid,
            parent_guid=parent_guid,
            bund_organisation_or_child=bund_organisation_or_child,
        )

        organisation.additional_properties = d
        return organisation

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
