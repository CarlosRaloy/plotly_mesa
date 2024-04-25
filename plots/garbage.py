html.Div(
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
                html.A(dbc.Button("Learn More", color="primary", className="lead"), href="http://localhost:8000/avg/"),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-body-secondary rounded-3",
        style={
            "background": "#e0e0e0",
            "box-shadow": "-20px -20px 60px #bebebe, 20px 20px 60px #ffffff"
        },
    )
