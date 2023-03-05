from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar(
    "T",
    bound="LogProcessStatsForObjectApiV1LogLogObjectStatsProcessGetResponseLogProcessstatsforobjectApiV1LogLogobjectStatsProcessGet",
)


@attr.s(auto_attribs=True)
class LogProcessStatsForObjectApiV1LogLogObjectStatsProcessGetResponseLogProcessstatsforobjectApiV1LogLogobjectStatsProcessGet:
    """ """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        log_process_stats_for_object_api_v1_log_log_object_stats_process_get_response_log_processstatsforobject_api_v1_log_logobject_stats_process_get = (
            cls()
        )

        log_process_stats_for_object_api_v1_log_log_object_stats_process_get_response_log_processstatsforobject_api_v1_log_logobject_stats_process_get.additional_properties = (
            d
        )
        return log_process_stats_for_object_api_v1_log_log_object_stats_process_get_response_log_processstatsforobject_api_v1_log_logobject_stats_process_get

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
