"""gr.ScatterPlot() component."""

from __future__ import annotations

from typing import Callable, Literal

import altair as alt
import pandas as pd
from gradio_client.documentation import document, set_documentation_group
from pandas.api.types import is_numeric_dtype

from gradio.blocks import Default, get
from gradio.components.plot import AltairPlot, Plot

set_documentation_group("component")


@document()
class ScatterPlot(Plot):
    """
    Create a scatter plot.

    Preprocessing: this component does *not* accept input.
    Postprocessing: expects a pandas dataframe with the data to plot.

    Demos: scatter_plot
    Guides: creating-a-dashboard-from-bigquery-data
    """

    def __init__(
        self,
        value: pd.DataFrame | Callable | None | Default = Default(None),
        x: str | None | Default = Default(None),
        y: str | None | Default = Default(None),
        *,
        color: str | None | Default = Default(None),
        size: str | None | Default = Default(None),
        shape: str | None | Default = Default(None),
        title: str | None | Default = Default(None),
        tooltip: list[str] | str | None | Default = Default(None),
        x_title: str | None | Default = Default(None),
        y_title: str | None | Default = Default(None),
        color_legend_title: str | None | Default = Default(None),
        size_legend_title: str | None | Default = Default(None),
        shape_legend_title: str | None | Default = Default(None),
        color_legend_position: Literal[
            "left",
            "right",
            "top",
            "bottom",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "none",
        ]
        | None = None,
        size_legend_position: Literal[
            "left",
            "right",
            "top",
            "bottom",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "none",
        ]
        | None = None,
        shape_legend_position: Literal[
            "left",
            "right",
            "top",
            "bottom",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "none",
        ]
        | None = None,
        height: int | None | Default = Default(None),
        width: int | None | Default = Default(None),
        x_lim: list[int | float] | None | Default = Default(None),
        y_lim: list[int | float] | None | Default = Default(None),
        caption: str | None | Default = Default(None),
        interactive: bool | None | Default = Default(True),
        label: str | None | Default = Default(None),
        every: float | None | Default = Default(None),
        show_label: bool | None | Default = Default(None),
        container: bool | None | Default = Default(True),
        scale: int | None | Default = Default(None),
        min_width: int | None | Default = Default(160),
        visible: bool |  Default = Default(True),
        elem_id: str | None | Default = Default(None),
        elem_classes: list[str] | str | None | Default = Default(None),
    ):
        """
        Parameters:
            value: The pandas dataframe containing the data to display in a scatter plot, or a callable. If callable, the function will be called whenever the app loads to set the initial value of the component.
            x: Column corresponding to the x axis.
            y: Column corresponding to the y axis.
            color: The column to determine the point color. If the column contains numeric data, gradio will interpolate the column data so that small values correspond to light colors and large values correspond to dark values.
            size: The column used to determine the point size. Should contain numeric data so that gradio can map the data to the point size.
            shape: The column used to determine the point shape. Should contain categorical data. Gradio will map each unique value to a different shape.
            title: The title to display on top of the chart.
            tooltip: The column (or list of columns) to display on the tooltip when a user hovers a point on the plot.
            x_title: The title given to the x axis. By default, uses the value of the x parameter.
            y_title: The title given to the y axis. By default, uses the value of the y parameter.
            color_legend_title: The title given to the color legend. By default, uses the value of color parameter.
            size_legend_title: The title given to the size legend. By default, uses the value of the size parameter.
            shape_legend_title: The title given to the shape legend. By default, uses the value of the shape parameter.
            color_legend_position: The position of the color legend. If the string value 'none' is passed, this legend is omitted. For other valid position values see: https://vega.github.io/vega/docs/legends/#orientation.
            size_legend_position: The position of the size legend. If the string value 'none' is passed, this legend is omitted. For other valid position values see: https://vega.github.io/vega/docs/legends/#orientation.
            shape_legend_position: The position of the shape legend. If the string value 'none' is passed, this legend is omitted. For other valid position values see: https://vega.github.io/vega/docs/legends/#orientation.
            height: The height of the plot in pixels.
            width: The width of the plot in pixels.
            x_lim: A tuple or list containing the limits for the x-axis, specified as [x_min, x_max].
            y_lim: A tuple of list containing the limits for the y-axis, specified as [y_min, y_max].
            caption: The (optional) caption to display below the plot.
            interactive: Whether users should be able to interact with the plot by panning or zooming with their mouse or trackpad.
            label: The (optional) label to display on the top left corner of the plot.
            every:  If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: Whether the label should be displayed.
            visible: Whether the plot should be visible.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
        """
        self.x = get(x)
        self.y = get(y)
        self.color = get(color)
        self.size = get(size)
        self.shape = get(shape)
        self.tooltip = get(tooltip)
        self.title = get(title)
        self.x_title = get(x_title)
        self.y_title = get(y_title)
        self.color_legend_title = get(color_legend_title)
        self.color_legend_position = get(color_legend_position)
        self.size_legend_title = get(size_legend_title)
        self.size_legend_position = get(size_legend_position)
        self.shape_legend_title = get(shape_legend_title)
        self.shape_legend_position = get(shape_legend_position)
        self.caption = get(caption)
        self.interactive_chart = get(interactive)
        self.width = get(width)
        self.height = get(height)
        self.x_lim = get(x_lim)
        self.y_lim = get(y_lim)
        super().__init__(
            value=value,
            label=label,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
        )

    def get_block_name(self) -> str:
        return "plot"

    @staticmethod
    def create_plot(
        value: pd.DataFrame,
        x: str,
        y: str,
        color: str | None = None,
        size: str | None = None,
        shape: str | None = None,
        title: str | None = None,
        tooltip: list[str] | str | None = None,
        x_title: str | None = None,
        y_title: str | None = None,
        color_legend_title: str | None = None,
        size_legend_title: str | None = None,
        shape_legend_title: str | None = None,
        color_legend_position: Literal[
            "left",
            "right",
            "top",
            "bottom",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "none",
        ]
        | None = None,
        size_legend_position: Literal[
            "left",
            "right",
            "top",
            "bottom",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "none",
        ]
        | None = None,
        shape_legend_position: Literal[
            "left",
            "right",
            "top",
            "bottom",
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
            "none",
        ]
        | None = None,
        height: int | None = None,
        width: int | None = None,
        x_lim: list[int | float] | None = None,
        y_lim: list[int | float] | None = None,
        interactive: bool | None = True,
    ):
        """Helper for creating the scatter plot."""
        interactive = True if interactive is None else interactive
        encodings = {
            "x": alt.X(
                x,  # type: ignore
                title=x_title or x,  # type: ignore
                scale=AltairPlot.create_scale(x_lim),  # type: ignore
            ),  # ignore: type
            "y": alt.Y(
                y,  # type: ignore
                title=y_title or y,  # type: ignore
                scale=AltairPlot.create_scale(y_lim),  # type: ignore
            ),
        }
        properties = {}
        if title:
            properties["title"] = title
        if height:
            properties["height"] = height
        if width:
            properties["width"] = width
        if color:
            if is_numeric_dtype(value[color]):
                domain = [value[color].min(), value[color].max()]
                range_ = [0, 1]
                type_ = "quantitative"
            else:
                domain = value[color].unique().tolist()
                range_ = list(range(len(domain)))
                type_ = "nominal"

            encodings["color"] = {
                "field": color,
                "type": type_,
                "legend": AltairPlot.create_legend(
                    position=color_legend_position, title=color_legend_title or color
                ),
                "scale": {"domain": domain, "range": range_},
            }
        if tooltip:
            encodings["tooltip"] = tooltip
        if size:
            encodings["size"] = {
                "field": size,
                "type": "quantitative" if is_numeric_dtype(value[size]) else "nominal",
                "legend": AltairPlot.create_legend(
                    position=size_legend_position, title=size_legend_title or size
                ),
            }
        if shape:
            encodings["shape"] = {
                "field": shape,
                "type": "quantitative" if is_numeric_dtype(value[shape]) else "nominal",
                "legend": AltairPlot.create_legend(
                    position=shape_legend_position, title=shape_legend_title or shape
                ),
            }
        chart = (
            alt.Chart(value)  # type: ignore
            .mark_point(clip=True)  # type: ignore
            .encode(**encodings)
            .properties(background="transparent", **properties)
        )
        if interactive:
            chart = chart.interactive()

        return chart

    def postprocess(self, y: pd.DataFrame | dict | None) -> dict[str, str] | None:
        # if None or update
        if y is None or isinstance(y, dict):
            return y
        if self.x is None or self.y is None:
            raise ValueError("No value provided for required parameters `x` and `y`.")
        chart = self.create_plot(
            value=y,
            x=self.x,
            y=self.y,
            color=self.color,
            size=self.size,
            shape=self.shape,
            title=self.title,
            tooltip=self.tooltip,
            x_title=self.x_title,
            y_title=self.y_title,
            color_legend_title=self.color_legend_title,
            size_legend_title=self.size_legend_title,
            shape_legend_title=self.size_legend_title,
            color_legend_position=self.color_legend_position,  # type: ignore
            size_legend_position=self.size_legend_position,  # type: ignore
            shape_legend_position=self.shape_legend_position,  # type: ignore
            interactive=self.interactive_chart,
            height=self.height,
            width=self.width,
            x_lim=self.x_lim,
            y_lim=self.y_lim,
        )

        return {"type": "altair", "plot": chart.to_json(), "chart": "scatter"}
