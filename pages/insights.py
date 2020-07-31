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
            
            
        ## What makes a "Sticky" Customer

        The term sticky is just like it sounds. Someone that stays around and sticks to the subscription for a long time. 
        In the battle of LCV (Lifetime Client Value) The goal is to earn customers that buy and keep on buying. 
        This idea comes from the old addage "I would Rather make 10k/week for the rest of my life than a Million dollars once". 
        For Businesses that sell a subscription based service LCV and ACV (Average Client Value) are the two biggest ways they evaluate how the business is running.
        For the purpose of this project we are going to stay focused on LCV. 
        
        In order to understand LCV you need two numbers. 1. Monthy Revenue from that customer(Montly Charges), 
        2. Number of months (Tenure). That yeilds the total amount of money that customer brings in (Total Charges). 
        We have two options in order to increase LCV, increase monthly charges or increase the number of months the customer pays. 
        For the purpose of this project we will focus on an idea called "Churn"
        
        ## What is Churn?
        
        Churn is also known as attrition, this is when a customer "falls off" or cancels service. 
        In the fight for High LCV, attrition is the #1 Enemy. Here is where we find our useful target for prediction. 
        Can we predict, based on a description of the customer, if they are going to "Churn". 
        In order to have a starting point that will allow us to prove our model is better than just guessing the average, We use a baseline. 
        First and formost our goal is predicting one of two outcomes - if the customer will discontinue service or remain with the service. 
        This means that if churn is "True" the customer will terminate or cancel service. If "Fasle" the customer will remain with the service. 
        A little confusing at first. Although we can break it down to saying True is bad and False is good!. 
        
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