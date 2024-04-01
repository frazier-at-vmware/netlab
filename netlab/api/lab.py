from typing import Optional, List, Any, Dict
from typing_extensions import Literal

from ._client_protocol import ClientProtocol


class LabApiMixin(ClientProtocol):
    "Methods for working with labs."

    async def lab_exercise_list(
        self,
        *,
        properties: Optional[List[str]] = None,
        sort_property: Literal["ex_id", "ex_index", "ex_name", "ex_con_id"] = "ex_id",
        con_id: Optional[str] = None,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        This method allows you to retrieve a list of lab exercises installed on the system.

        :param con_id: If specified, only return exercises within for the lab designed with identifier of con_id.
        :param sort_property: Property to sort results by.
        :param properties: List of properties to retrieve. See Properties section for list of available properties.

        :return: On success, returns an object with the requested properties:

        **Properties**

        ex_id
            Lab exercise identifier.
        ex_con_id
            Lab design identifier.
        ex_index
            Exercise index number in lab design.
        ex_name
            Exercise name.
        ex_content_url
            Lab document relative URL.
        ex_minutes
            Exercise minimum time in minutes.
        ex_topology_image
            Lab topology image relative URL.
        ex_im_id
            Internal image map identifier for clickable hotspots.
        ex_vlan_map
            Alternate VLAN map for real equipment pods, overrides pod design.
        ex_pt_id
            Exercise pod type identifier.
        ex_tabs
            Exercise tabs enabled.
        ex_actions
            Exercise actions enabled.
        ex_fs_id
            Root node of folder containing configuration files for this exercise.
        ex_content_no_preview
            If true, user cannot preview this exercise.
        ex_ilt_no_select
            If true, exercise is disabled in ILT.
        cls_ids
            Array of class identifiers using this content.
        hotspots
            Array of image_map objects (for clickable hotspots).
        """
        method = "lab.exercise.list"

        return await self.call(
            method,
            con_id=con_id,
            sort_property=sort_property,
            properties=properties,
            **kwargs
        )
