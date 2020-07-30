# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(


        ),

        dcc.Slider(
            id='tenure-slider',
            min=0,
            max=70,
            step=1,
            value=5,
            marks={0: '0',
                   10: '10',
                   20: '20',
                   30: '30',
                   40: '40',
                   50: '50',
                   60: '60',
                   70: '70'}
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='tenure-slider', component_property='value')]
 )
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)