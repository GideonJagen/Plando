import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


class AsaWidget:

    STANDARD_VALUE = []  # Basera på data

    @staticmethod
    def asa_widget():
        widget = html.Div(
            id="asa",
            children=[
                html.H4(
                    id="asa_h4",
                    children="ASA-klass",
                    style={
                        # "borderWidth": "1px",
                        # "borderStyle": "solid",
                        # "margin": "0px",
                    },
                ),
                dcc.Checklist(
                    id="asa_checklist",
                    options=[
                        {"label": "ASA 1", "value": 1},
                        {"label": "ASA 2", "value": 2},
                        {"label": "ASA 3", "value": 3},
                        {"label": "ASA 4", "value": 4},
                        {"label": "ASA 5", "value": 5},
                        {"label": "ASA 6", "value": 6},
                        {"label": "Ej specificerat", "value": -1},
                    ],
                    labelStyle={"display": "inline-block"},
                    style={
                        "width": "100%",
                        # "borderWidth": "1px",
                        # "borderStyle": "solid",
                        # "margin": "0px",
                    },
                ),
            ],
            style={
                "width": "15%",
                # "borderWidth": "1px",
                # "borderStyle": "solid",
                # "textAlign": "center",
                # "margin": "5px",
            },
        )
        return widget

    @staticmethod
    def add_asa_callback(app):
        @app.callback(
            Output(component_id="asa_checklist", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_opTime(n_clicks):
            return AsaWidget.STANDARD_VALUE

        return app
