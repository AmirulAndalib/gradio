"""gr.HTML() component."""

from __future__ import annotations

from typing import Any, Callable, Literal

from gradio_client.documentation import document, set_documentation_group
from gradio_client.serializing import StringSerializable

from gradio.blocks import Default, get
from gradio.components.base import IOComponent
from gradio.events import Changeable

set_documentation_group("component")


@document()
class HTML(Changeable, IOComponent, StringSerializable):
    """
    Used to display arbitrary HTML output.
    Preprocessing: this component does *not* accept input.
    Postprocessing: expects a valid HTML {str}.

    Demos: text_analysis
    Guides: key-features
    """

    def __init__(
        self,
        value: str | Callable | None | Default = Default(""),
        *,
        label: str | None | Default = Default(None),
        every: float | None | Default = Default(None),
        show_label: bool | None | Default = Default(None),
        visible: bool |  Default = Default(True),
        elem_id: str | None | Default = Default(None),
        elem_classes: list[str] | str | None | Default = Default(None),
        **kwargs,
    ):
        """
        Parameters:
            value: Default value. If callable, the function will be called whenever the app loads to set the initial value of the component.
            label: component name in interface.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
        """
        IOComponent.__init__(
            self,
            label=label,
            every=every,
            show_label=show_label,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            **kwargs,
        )

