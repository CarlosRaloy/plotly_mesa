from .database import times_user , improve, data, group_company
from django_plotly_dash import DjangoDash
from dash import dash_table, html, dcc
import dash_bootstrap_components as dbc
from django.urls import reverse
from django.templatetags.static import static
from dash.dependencies import Input, Output
import plotly.express as px 


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
                html.A(dbc.Button("Watch Results 📌", color="primary", className="lead"), href=reverse("plots:dash")),
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
                    html.A(dbc.Button("Improve", color="dark", outline=True), href=reverse("plots:improve")),
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
                    html.A(dbc.Button("Average Response", color="dark", outline=True), href=reverse("plots:avg")),
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
                    html.A(dbc.Button("Average Response", color="dark", outline=True), href=reverse("plots:company")),
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


def calculate_improve():
     table = dash_table.DataTable(
        data=improve.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in improve.columns],
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
     
     app = DjangoDash('improve', external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.GRID])
     app.layout = html.Div([
        html.Div(
            children='Calculo de Eficiencia y eficacia',
            className="lead text-center font-weight-bold text-primary",
            style={'padding': '20px'}
        ),
        table
    ])
     

     return app

     
def dashboard():



    app = DjangoDash('TicketDashboard', external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.GRID])

    # Layout del dashboard
    app.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Dropdown(
                            id='site-dropdown',
                            options=[{'label': site, 'value': site} for site in data['site'].unique()],
                            value=[],
                            multi=True,
                            placeholder='Select Site'
                        ),
                        width=4
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='technician-dropdown',
                            options=[{'label': technician, 'value': technician} for technician in data['technician_name'].unique()],
                            value=[],
                            multi=True,
                            placeholder='Select Technician'
                        ),
                        width=4
                    ),
                ],
                className='mb-4',
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Total de Tickets", className="card-title", style={'text-align': 'center'}),
                                    html.P(id="ticket-count", className="card-text", style={'font-size': '1.5em', 'text-align': 'center'}),
                                ]
                            ),
                            className="mt-2",
                            style={"border": "none", "width": "100%"}
                        ),
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(id='category-bar')),
                    dbc.Col(dcc.Graph(id='service-category-bar')),
                    dbc.Col(
                        dcc.Graph(id='priority-pie'),
                    ),
                ]
            )
        ],
        fluid=True,
    )

    # Agregar los gráficos con Plotly
    @app.callback(
        [Output('category-bar', 'figure'),
            Output('service-category-bar', 'figure'),
            Output('priority-pie', 'figure'),
            Output('ticket-count', 'children')],
        [Input('site-dropdown', 'value'),
            Input('technician-dropdown', 'value')]
    )
    def update_graphs(selected_sites, selected_technicians):
        if not selected_sites:
            selected_sites = data['site'].unique()
        if not selected_technicians:
            selected_technicians = data['technician_name'].unique()

        filtered_data = data[
            (data['site'].isin(selected_sites)) & 
            (data['technician_name'].isin(selected_technicians))
        ]

        ticket_count = filtered_data.shape[0]

        if filtered_data.empty:
            return {}, {}, {}, f"{ticket_count}"

        try:
            # Gráfico de barras de category
            category_data = filtered_data.groupby('category').size().reset_index(name='Count')
            category_fig = px.bar(category_data,
                                    x='category',
                                    y='Count',
                                    title='Tickets por Categoría',
                                    labels={'category': 'Categoría', 'Count': 'Número de Tickets'})

            # Gráfico de barras de service_category
            service_category_data = filtered_data.groupby('service_category').size().reset_index(name='Count')
            service_category_fig = px.bar(service_category_data,
                                            x='service_category',
                                            y='Count',
                                            title='Tickets por Service Category',
                                            labels={'service_category': 'Service Category', 'Count': 'Número de Tickets'})

            # Gráfico de pastel de priority
            priority_data = filtered_data.groupby('priority').size().reset_index(name='Count')
            priority_fig = px.pie(priority_data,
                                    names='priority',
                                    values='Count',
                                    title='Tickets por Prioridad')

            return category_fig, service_category_fig, priority_fig, f"{ticket_count}"

        except Exception as e:
            print(f"Error: {e}")
            return {}, {}, {}, f"{ticket_count}"
        

def company():
    app = DjangoDash('company', external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.themes.GRID])

    table = dash_table.DataTable(
        data=group_company.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in group_company.columns],
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
            children='Tickets por empresa',
            className="lead text-center font-weight-bold text-primary",
            style={'padding': '20px'}
        ),
        table
    ])

    return app

