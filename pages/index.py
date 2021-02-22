# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app.app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## The War Against Churn
            
            If a good customer is one that stays around for a long time and continues to use the product, 
            then churn is the exact opposite of that. 
            
            If we could foresee what makes a customer churn, and delay, or prevent it all together. That would be pretty useful wouldnt it?
        

            """
        ),
        dcc.Link(dbc.Button('TO BATTLE!', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col([html.Img(src='assets/phone-illustration.png', className='img-fluid')],
                  align='center'
)

layout = dbc.Row([column1, column2])