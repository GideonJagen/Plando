import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from components.age import Age
from components.anesthesia import Anesthesia
from components.asa import Asa
from components.care_type import CareType
from components.municipalities import Municipalities
from components.op_code import OpCode
from components.op_time import OpTime
from components.operator import Operator
from components.short_notice import ShortNotice
from components.statistics_code import StatisticsCode
from components.file_upload import FileUpload


class Sidebar:
    SEARCH_FILTER = "Sökfilter"
    OPEN_FILTER = "Öppna filter"
    REQUEST_FILL_FORM = "Var god fyll i relevanta sökfält"

    is_open = True

    @staticmethod
    def get_component():
        component = dbc.Row(
            children=[
                Sidebar._sidebar_content(),
                Sidebar._sidebar_button(),
            ],
            id="sidebar",
            className="p-1",
            style={
                "background-color": "#DCEAEF",
                "height": "inherit",
            },
        )
        return component

    @staticmethod
    def _sidebar_content():
        component = dbc.Col(
            children=[
                html.H2(Sidebar.SEARCH_FILTER),
                FileUpload.get_component(),
                html.P(Sidebar.REQUEST_FILL_FORM),
                html.Hr(style={"border-width": 4, "border-color": "#6ea6cd"}),
                Sidebar._filter_form(),
            ],
            id="sidebar_content",
            className="pl-5",
            style={
                "height": "inherit",
            },
        )
        return component

    @staticmethod
    def _sidebar_button():
        component = dbc.Button(
            children=[
                html.I(
                    id="sidebar_btn_icon",
                    className="fas fa-chevron-left",
                )
            ],
            id="btn_sidebar",
            color="primary",
            style={
                "height": "inherit",
            },
        )
        return component

    @staticmethod
    def _filter_form():
        component = dbc.Form(
            children=[
                CareType.get_component(),
                Municipalities.get_component(),
                Anesthesia.get_component(),
                Age.get_component(),
                StatisticsCode.get_component(),
                Asa.get_component(),
                OpTime.get_component(),
                OpCode.get_component(),
                Operator.get_component(),
                ShortNotice.get_component(),
            ],
            style={
                "width": "24em",
                "overflow": "auto",
                "height": "calc(100% - 8em)",
            },
        )
        return component

    # TODO: Possibly modify such that the class style is not overwritten
    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="sidebar_content", component_property="style"),
            Output(component_id="sidebar_btn_icon", component_property="className"),
            Input(component_id="btn_sidebar", component_property="n_clicks"),
            prevent_initial_call=True,
        )
        def _toggle_sidebar(n_clicks):
            Sidebar.is_open = not Sidebar.is_open
            return (
                {"display": "block"} if Sidebar.is_open else {"display": "none"},
                "fas fa-chevron-left" if Sidebar.is_open else "fas fa-chevron-right",
            )

        return app
