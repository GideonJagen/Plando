import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output


class OpCode:
    STANDARD_VALUE_DD = None
    STANDARD_VALUE_OPT = "Visa alla"
    STANDARD_OP_CODES = []  # Made up for testing purposes

    @staticmethod
    def get_component():
        """
        Highest hierarcy widget of opCode_selection function
        """
        widget = dbc.FormGroup(
            id="opCode_selection",
            children=[dbc.Label("Operationskod"), OpCode._op_code_dropdown()],
        )
        return widget

    @staticmethod
    def _op_code_options():
        """
        Check buttons of top hierarcy widget
        """

        options = ["Visa alla", "Exkludera", "Visa endast"]
        widget = dbc.RadioItems(
            id="opCode_options",
            options=[{"label": opt, "value": opt} for opt in options],
            labelStyle={"display": "inline-block"},
        )
        return widget

    @staticmethod
    def _op_code_dropdown():
        """
        Dropdown list of top hierarcy widget
        """

        widget = dcc.Dropdown(
            id="opCode_dropdown",
            placeholder="Välj operationskod",
            multi=True,
            value=[],
            options=[
                {"label": code, "value": code} for code in OpCode.STANDARD_OP_CODES
            ],  # list builder to create dropdown options,
        )
        return widget

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="opCode_dropdown", component_property="value"),
            Input(component_id="reset_filter_button", component_property="n_clicks"),
        )
        def reset_component(n_clicks):
            return OpCode.STANDARD_VALUE_DD

        return app

    @staticmethod
    def value_to_string(value):
        return f"Operationskod: {value if value else 'Alla'}"