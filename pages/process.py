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
            It seems as though the fun part only lasts for a short amount of time. Once the pipeline has been built, optimized and trained. 
            The next goal is to understand our results. I used two metrics when evaluating my model. \n 
            
            1. ROC-AUC: This was necessary to obtain the best possible result for the second metric we were looking at
            """
        ),
        html.Img(src='assets/ROC-AUC-curve.png', className='img-fluid'),
        dcc.Markdown(
            """
            2. Recall: The percentage, out of the total predictions, that were correctly identified. 
            """
        ),
        html.Img(src='assets/carbon (2).png', className='img-fluid'),
        dcc.Markdown(
            """
            The inclusive nature of recall bodes well for a situation like this. Our goal is to identify as many at risk customers
            as possible and work to either take care of them, or use their cases in order to better understand the focus of the 
            business.
            
            One of the benefits of using a Logisitic Regression model is the simplicity of it. Refining and tuning our model
            can be easily done to increase recall even further by altering the threshold. The standard threshold on a Logistic Regression 
            model is always at 50%, adjusting the tipping point will allow you include or exclude more based on the goal of the 
            experiement. 
            
            Once we had a model we felt we could make predictions with the probability that we desired - The fun stuff begins;
            predictions! 
            """
        ),
    ],


)

layout = dbc.Row([column1])