from .database import hola
from django_plotly_dash import DjangoDash
from dash import dash_table, html
import dash_bootstrap_components as dbc
from django.urls import reverse


def plot1d():
    app = DjangoDash('SimpleExample', external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.GRID])

    app.layout = html.Div(
        dbc.Container(
            [
                html.H1("Oxirus System Ticket Analysis", className="display-3"),
                html.P(
                    "Welcome !!, System is a dedicated platform for managing and resolving support requests, including Corporativo Nova and Raloy Lubricantes.",
                    className="lead", ),
                html.P(
                    "This system aims to facilitate smooth communication and efficient issue resolution without overwhelming the user.",
                    className="lead", ),
                html.Hr(className="my-2"),
                html.P("Click Here , Times for technican"),
                html.A(dbc.Button("Learn More", color="primary", className="lead"), href=reverse('main:avg')),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-body-secondary rounded-3",
        style={
            "background": "#e0e0e0",
            "box-shadow": "-20px -20px 60px #bebebe, 20px 20px 60px #ffffff"
        }
    )

    return app


def avg_times():
    app = DjangoDash('avg_time', external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.GRID])

    table = dash_table.DataTable(
        data=hola.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in hola.columns],
        page_size=100,
        style_table={'overflowX': 'auto'},
        sort_action="native",  # Ordenamiento nativo en las cabeceras
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        style_cell={
            'textAlign': 'center',
            'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
        }
    )

    app.layout = html.Div([
        html.Div(
            children='Tiempos de respuesta',
            className="lead text-center font-weight-bold text-primary",
            style={'padding': '20px'}
        ),
        table
    ])

    return app


