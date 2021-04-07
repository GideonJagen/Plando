import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

from data_handling import LoadedData


# Todo to avoid an even more massive callback (search_result) i decided to add a button with the functionality
# of actually loading the file. When a file is selected, the widget stores it but it is not acctually loaded until
# the load button is pressed, this way we can also avoid loading incorrect file and display messages at the same time.
#


class FileUpload:
    @staticmethod
    def get_component():
        upload = dbc.FormGroup(
            style={"padding": "1em"},
            children=[
                dcc.Upload(
                    id="upload",
                    children=[dbc.Label(id="file-label", children=["Välj ny fil"])],
                ),
                dbc.Collapse(
                    id="load_collapse",
                    # TODO gör typ grön när datan visas, dvs när knappen klickas
                    children=[dbc.Button(id="load_button", children=["Visa data"])],
                ),
            ],
        )
        return upload

    @staticmethod
    def add_callback(app):
        @app.callback(
            Output(component_id="load_collapse", component_property="is_open"),
            Output(component_id="file-label", component_property="children"),
            Output(component_id="filetype-warning", component_property="is_open"),
            Input(component_id="upload", component_property="filename"),
            Input(
                component_id="filetype_warning_close_button",
                component_property="n_clicks",
            ),
            prevent_initial_call=True,
        )
        def valid_upload(filename, n_clicks):
            """
            :param filename: name of the loaded file
            :param n_clicks: not used, only there because button is input for callback
            :return: Bool, String, Bool representing load_collapse property is_open, file_label, filetype-warning
            """

            if isinstance(filename, str) and filename.endswith(".csv"):
                return True, filename, False  # if csv file, show load button
            context = dash.callback_context
            if (
                context.triggered[0]["prop_id"].split(".")[0]
                == "filetype_warning_close_button"
            ):
                return (
                    False,
                    "Välj ny fil",
                    False,
                )  # if close button in warning, close warning
            return False, "Välj ny fil", True  # if invalid file, display warning

        return app

    @staticmethod
    def add_load_button_callback(app):
        @app.callback(
            Output(component_id="load_button", component_property="n_clicks"),
            Input(component_id="load_button", component_property="n_clicks"),
            Input(component_id="upload", component_property="filename"),
            Input(component_id="upload", component_property="contents"),
            prevent_initial_call=True,
        )
        def load_data(n_clicks, filename, contents):
            context = dash.callback_context
            if context.triggered[0]["prop_id"].split(".")[0] == "load_button":
                LoadedData.load_data(filename, contents)

        return app