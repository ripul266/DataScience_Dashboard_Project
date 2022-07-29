#importing required libraries
import dash
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

#reading the csv file from a dataset downloaded from kaggle
df = pd.read_csv("myntra_products_catalog.csv")

#creating  a dash app
app = dash.Dash(__name__)
# creating layout of dash app
app.layout=html.Div([
    #putting headline to our app
    html.H1("Myntra Gender Based Product Range",style={'text-align':'center'}), #adding header of html
    #creating a dropdown for gender selection
    dcc.Dropdown(id='gender-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df.Gender.unique())],
                 value='Men',
                 style={'width':'50%'}
                 ),
  # creating graph 1 i.e. histogram
    dcc.Graph(id='my-graph',
              figure={}),
    #creating scattered graph
    dcc.Graph(id='my-graph1',
              figure={}),

])
#first callback for histogram
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='gender-choice', component_property='value'),
)
#function for histogram
def interactive_graphs(value_gender):
    dff = df[df.Gender==value_gender] #here picking datavalues where gender is selected one
    fig = px.histogram(data_frame=dff, x='ProductBrand', y='NumImages')

    return fig
#callback for scatter graph
@app.callback(
    Output(component_id='my-graph1', component_property='figure'),
    Input(component_id='gender-choice', component_property='value'),
)
def interactive_graphs(value_gender):
    dff = df[df.Gender==value_gender]
    fig1 = px.scatter(data_frame=dff, x='ProductBrand', y='NumImages')

    return fig1


#running the app server
if __name__=='__main__':
    app.run_server()
