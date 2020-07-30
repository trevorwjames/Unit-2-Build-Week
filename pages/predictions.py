# Imports from 3rd party libraries

import dash

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from joblib import load
import pandas as pd

# Imports from this application
from app import app
pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.Div([
        dcc.Markdown('#### Tenure (Months)'),
        dcc.Slider(
            id='tenure',
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
                   70: '70'},
            className='mb-1'
        ),
        ],
        style={'marginTop': 15, 'marginBottom': 15},
        ),
        dcc.Markdown('#### Multiple Lines'),
        dcc.Dropdown(
            id='lines',
            options=[
                {'label': 'Yes', 'value': 'Yes'},
                {'label': 'No', 'value': 'No'},
                {'label': 'No phone service', 'value': 'No Phone Service'}
            ],
            className='mb-2',
            value='Yes'
        ),
        dcc.Markdown('#### Internet Service'),
        dcc.Dropdown(
            id='internet_service',
            options=[
                {'label': 'Fiber Optic', 'value': 'Fiber Optic'},
                {'label': 'DSL', 'value': 'DSL'},
                {'label': 'No', 'value': 'No'}
            ],
            className='mb-3',
            value='Fiber Optic'
        ),
        dcc.Markdown('#### Technical Support'),
        dcc.Dropdown(
            id='tech_support',
            options=[
                {'label': 'Yes', 'value': 'Yes'},
                {'label': 'No', 'value': 'No'},
                {'label': 'No Internet Service', 'value': 'No internet service'}
            ],
            className='mb-4',
            value='Yes'
        ),

    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Div([
        dcc.Markdown('#### Monthly Charges (USD$)'),
        dcc.Slider(
            id='monthlycharges',
            min=15,
            max=120,
            step=15,
            value=15,
            marks={15: '15',
                   30: '30',
                   45: '45',
                   60: '60',
                   75: '75',
                   90: '90',
                   105: '105',
                   120: '120'},
            className='mb-1'
        ),
        ],
        style={'marginTop': 15, 'marginBottom': 15},
),
        dcc.Markdown('#### Contract'),
        dcc.Dropdown(
            id='contract',
            options=[
                {'label': 'Month to Month', 'value': 'Month-to-month'},
                {'label': 'One Year', 'value': 'One year'},
                {'label': 'Two Year', 'value': 'Two Year'}

            ],
            className='mb-2',
            value='Month to Month'
        ),
        dcc.Markdown('#### Payment Method'),
        dcc.Dropdown(
            id='paymentmethod',
            options=[
                {'label': 'Mailed Check', 'value': 'Mailed check'},
                {'label': 'Bank Transfer', 'value': 'Bank transfer (automatic)'},
                {'label': 'Credit Card (Auto)', 'value': 'Credit card (automatic)'},
                {'label': 'Electronic Check', 'value': 'Electronic check'}
            ],
            className='mb-3',
            value='Mailed Check'
        )

    ],
    md=4,
)
column3 = dbc.Col(
    [
        html.H2('Will Customer Churn?', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2, column3])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('tenure', 'value'),
     Input('lines', 'value'),
     Input('internet_service', 'value'),
     Input('tech_support', 'value'),
     Input('contract', 'value'),
     Input('paymentmethod', 'value'),
     Input('monthlycharges', 'value')
     ],
 )
def predict(tenure, MultipleLines, InternetService,
            TechSupport, Contract,
            PaymentMethod, MonthlyCharges):
    # put features in df
    df = pd.DataFrame(
        columns=['tenure', 'MultipleLines', 'InternetService', 'TechSupport',
                 'Contract', 'PaymentMethod', 'MonthlyCharges'],
        data=[[tenure, MultipleLines, InternetService,
               TechSupport, Contract,
               PaymentMethod, MonthlyCharges]]
    )

    # run prediciton
    y_pred = pipeline.predict(df)[0]

    print('Will this customer Churn?', y_pred)
    return 'Yes' if y_pred else 'No'
