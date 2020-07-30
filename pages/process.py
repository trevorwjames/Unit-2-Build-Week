# Imports from 3rd party libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Imports from this application

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [


        dcc.Markdown(
            """
        
            ## Process
            
            Lucky for me upon my first exploratory analysis of this dataset, it turned out it was realtively "Clean"  
            meaning my first task of setting it up for use in modeling was pretty straight forward. My First goal was 
            to make sure that I inspected the columns for possible leakage, and split the set into features(X) and target(y). 
            
            Once that was done my method for modeling is using three splits of the data: Train, Validation, and Test. \n
            70% of the data for training the model - allowing it to see where the correlations lie and create a model based off of them \n
            15% will be used for validation - checking the scores as it compare to the training \n
            15% will be used for testing - our data will never see this information until we are sure we can run it to see its real applicability.
            
            After running a few iterations of my model. Turns out the simplest one is the best. Logistic Regression
            - The pipeline code is below

            """
        ),
        html.Img(src='assets/lin model.png', className='img-fluid'),

        dcc.Markdown(
            """
            
            """
        )
    ],


)

layout = dbc.Row([column1])