# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
        ## What is Churn?
        
        Churn is also known as attrition, this is when a customer "falls off" or cancels service. 
        In the fight for High Lifetime Client Value (LCV), attrition is the #1 Enemy. Here is where we find our useful target for prediction. 
        Can we predict, based on a description of the customer, if they are going to "Churn". 
        In order to have a starting point that will allow us to prove our model is better than just guessing the average, We use a baseline. 
        Our baseline is the simplest form of prediction, if we cant beat the average, then the model is a waste of time. 
        """
        ),
    html.Img(src='assets/carbon (1).png', className='img-fluid'),

        dcc.Markdown(
            """
        Our goal is to predict one of two outcomes - if the customer will discontinue service or remain a customer. 
        This means that if churn is "True" the customer will terminate or cancel service.
        If "False" they will remain with the service. The "True" predictions are the ones in which we care about the most.
        Just like feedback, positive is good, although constructive feedback is where we grow!
         
        
        ## What makes Churn Happen? 
        
        We only have access to so much information, and only so much of that information is useful to us. 
        Below is a Permutation Importance chart of all the features used to train our original model - because of the amount of 
        importance of certain features on the predicted outcome, they were left out of the prediction portion. 
                    """
        ),

html.Img(src='assets/PIchart.png', className='img-fluid'),

        dcc.Markdown(
            """
        #### Tenure
        From the chart we can see the massive impact "Tenure" has on the outcome of the prediction. We can look at this one of two ways \n
        1. Tenure is leakage: If you have a high tenure you are not churning - this could be seen as s direct link \n
        2. Tenure is indicative of behavior: Once something is a habit, you are more likely to continue with that habit. \n
        I decided to look at in the the second lens. This is useful information to use in the business in which the data originiated. 
        Should they push to sell longer term contracts? Would selling long term incentives keep people around for longer? \n
        
        #### Total Charges
        The next most important feature is "Total Charges". Which is a function of Tenure * Monthly Charges. (A Build in Engineered feature! Sweet!)
        In order to better understand how these features interact we will look at a Partial Dependence Interaction between them. 
        What you're seeing below is a breakdown of how the combination of the two impact the outcome of the model. 
        The lighter the color - and higher number - the more likely that person is to Churn. 
        
        You can see that a **higher** monthly charger and **shorter** tenure has a significantly higher chance of churning. 
        Much different than the opposite corner of a **longer** tenure and **lower** monthly charges. 
        
    
            """
        ),

html.Img(src='assets/pdpinteract.png', className='img-fluid', sizes='small'),

        dcc.Markdown(
            """
         ## Conclusion  
        Number 1. The more information, the better. At the start when we created the baseline we were at risk of having
        some imbalanced classes with 73% of the training data already resulting in a false churn outcome. If we were able to 
        have a large sample with more even distribution we could have had an even more accurate model. 
        
        Number 2. More Information again... Having more specific insight from the business you're working with can be essential 
        to generalize the findings and help gear the Product Manager, Sales Team, or Executive team. 
            """
        )

    ],
)

layout = dbc.Row([column1])