from .database import times_user
from django_plotly_dash import DjangoDash
from dash import dash_table, html
import dash_bootstrap_components as dbc
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.templatetags.static import static


def plot1d():
    app = DjangoDash('SimpleExample', external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.GRID])

    left_jumbotron = dbc.Col(
        html.Div(
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
                html.A(dbc.Button("Watch Results 📌", color="primary", className="lead"), href=reverse("plots:avg")),
            ],
            className="p-3 bg-body-secondary",
            style={
                "background": "#e0e0e0",
                "box-shadow": "-20px -20px 60px #bebebe, 20px 20px 60px #ffffff"
            },
        ),
        md=12,
    )

    # === Cards ===

    card1 = dbc.Card(
        [
            dbc.CardImg(src=static('img/base.png'), top=True),
            dbc.CardBody(
                [
                    dbc.Button("Tabla 1", color="dark", outline=True, href="#"),
                ], className="d-grid gap-1",
            ),
        ],
        style={"width": "18rem",
               "border-radius": "8px",
               "background": "#fcfcfc",
               "box-shadow": "50px 50px 58px #ebebeb, -50px -50px 58px #ffffff",
               "display": "flex",
               "flex-direction": "column",
               "align-items": "center",
               "justify-content": "center",
               },
    )

    # Card 2
    card2 = dbc.Card(
        [
            dbc.CardImg(src=static('img/base.png'), top=True),
            dbc.CardBody(
                [
                    dbc.Button("Tabla 1", color="dark", outline=True, href="#"),
                ], className="d-grid gap-1",
            ),
        ],
        style={"width": "18rem",
               "border-radius": "8px",
               "background": "#fcfcfc",
               "box-shadow": "50px 50px 58px #ebebeb, -50px -50px 58px #ffffff",
               "display": "flex",
               "flex-direction": "column",
               "align-items": "center",
               "justify-content": "center",
               },
    )

    # Card 3
    card3 = dbc.Card(
        [
            dbc.CardImg(src=static('img/base.png'), top=True),
            dbc.CardBody(
                [
                    dbc.Button("Tabla 1", color="dark", outline=True, href="#"),
                ], className="d-grid gap-1",
            ),
        ],
        style={"width": "18rem",
               "border-radius": "8px",
               "background": "#fcfcfc",
               "box-shadow": "50px 50px 58px #ebebeb, -50px -50px 58px #ffffff",
               "display": "flex",
               "flex-direction": "column",
               "align-items": "center",
               "justify-content": "center",
               },
    )

    right_jumbotron = dbc.Col(
        dbc.Container(
            [
                # Row of cards
                dbc.Row([
                    dbc.Col([card1], width=4),
                    dbc.Col([card2], width=4),
                    dbc.Col([card3], width=4),
                ], className="mt-4"),

            ],
            fluid=False,
            className="p-6",
        ),
        md=12,

    )


    app.layout = dbc.Row(
    [left_jumbotron, right_jumbotron],
    className="align-items-md-stretch",)

    return app


def avg_times():
    app = DjangoDash('avg_time', external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.GRID])

    table = dash_table.DataTable(
        data=times_user.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in times_user.columns],
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


