from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Suchkriterium")


@_attrs_define
class Suchkriterium:
    """
    Attributes:
        organisation_guids (Union[Unset, List[str]]): Diese Liste ermöglicht es, GUIDs von Organisationen als
            Suchkriterium zu übergeben. Die zurückgelierten Ergebnisse einer Anfrage enthalten dann nur die öffentlich
            sichtbaren Merkmalsgruppen oder Merkmale aus den angegebenen Organisationen.
        search_string (Union[Unset, str]): Teilstring, nach dem die Namen der öffentlich verfügabren Merkmalsgruppen
            oder Merkmale durchsucht werden. Enthält eine Merkmalsgruppe oder ein Merkmal, den Teilstring wird es der
            Ergebnismenge hinzugefügt Example: Ausstattung.
        filter_guids (Union[Unset, List[str]]): Diese Liste ermöglicht es, GUIDs von Filtern als Suchkriterium zu
            übergeben. Die zurückgelierten Ergebnisse einer Anfrage enthalten dann nur öffentlich sichtbare Merkmalsgruppen
            oder Merkmale, die den angegebenen Filtern untergeordnet sind.
        parent_guid (Union[Unset, str]): Hier kann eine GUID angegeben werden, in denen angefragten Merkmalsgruppen oder
            Merkmale enthalten sein müssen. Example: b0032e13-49f4-4dae-861c-cd9c5dcdb824.
        include_deprecated (Union[Unset, bool]): Ein Wahrheitswert, der angibt, ob bei der Suche nach öffentlich
            sichtbaren Merkmalsgruppen auch veraltete Merkmalsgruppen oder Merkmale zurückgeliefert werden sollen
        page_number (Union[Unset, int]): Mit diesem Parameter kann übermittelt werden, welche Seite der Suchergebnisse
            zurückgegeben wird. Per Default wird der Wert 0 übergeben.
    """

    organisation_guids: Union[Unset, List[str]] = UNSET
    search_string: Union[Unset, str] = UNSET
    filter_guids: Union[Unset, List[str]] = UNSET
    parent_guid: Union[Unset, str] = UNSET
    include_deprecated: Union[Unset, bool] = UNSET
    page_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organisation_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.organisation_guids, Unset):
            organisation_guids = self.organisation_guids

        search_string = self.search_string

        filter_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.filter_guids, Unset):
            filter_guids = self.filter_guids

        parent_guid = self.parent_guid

        include_deprecated = self.include_deprecated

        page_number = self.page_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organisation_guids is not UNSET:
            field_dict["organisationGuids"] = organisation_guids
        if search_string is not UNSET:
            field_dict["searchString"] = search_string
        if filter_guids is not UNSET:
            field_dict["filterGuids"] = filter_guids
        if parent_guid is not UNSET:
            field_dict["parentGuid"] = parent_guid
        if include_deprecated is not UNSET:
            field_dict["includeDeprecated"] = include_deprecated
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        organisation_guids = cast(List[str], d.pop("organisationGuids", UNSET))

        search_string = d.pop("searchString", UNSET)

        filter_guids = cast(List[str], d.pop("filterGuids", UNSET))

        parent_guid = d.pop("parentGuid", UNSET)

        include_deprecated = d.pop("includeDeprecated", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        suchkriterium = cls(
            organisation_guids=organisation_guids,
            search_string=search_string,
            filter_guids=filter_guids,
            parent_guid=parent_guid,
            include_deprecated=include_deprecated,
            page_number=page_number,
        )

        suchkriterium.additional_properties = d
        return suchkriterium

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
