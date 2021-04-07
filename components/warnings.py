import dash_bootstrap_components as dbc


class Warnings:
    @staticmethod
    def get_component():
        widget = dbc.Modal(
            id="filetype-warning",
            is_open=False,
            children=[
                dbc.ModalHeader("File not loaded: wrong filetype"),
                dbc.ModalBody("Make sure the file is of type: .csv"),
                dbc.ModalFooter(
                    children=[dbc.Button("Close", id="filetype_warning_close_button")]
                ),
            ],
        )
        return widget