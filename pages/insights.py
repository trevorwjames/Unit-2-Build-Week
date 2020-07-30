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


            """
        ),

    ],
)

layout = dbc.Row([column1])