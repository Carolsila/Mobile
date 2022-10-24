#!/usr/bin/env python
# coding: utf-8

# In[442]:


import pandas as pd


# In[443]:


df5=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/Laundry.csv")


# In[444]:
df5.set_index("Washers",inplace=True)
df5.rename(index={'Steam Sterilizer CO2 Per cycles(KGs)':'Steam Sterilizer CO2 per cycles(KGs)'},inplace=True)
df1=df5.reset_index()




df=df1.melt(id_vars='Washers',value_vars=list(df1.columns[1:]))
df


# In[445]:


df.rename({'variable':'Factors','value':'Values'},axis=1,inplace=True)


# In[446]:


DF=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/cotton.csv")

DF.rename(columns={'50/50 double sheet':'50/50 Double Sheet','50/50 sheet':'50/50 Sheet','100% cotton sheet':'100% Sheet'},inplace=True)




# In[447]:


DF1=DF.melt(id_vars='Factors',value_vars=list(DF.columns[1:]))



# In[448]:


DF1.rename({'variable':'Materials','value':'Values'},axis=1,inplace=True)



# In[449]:


Df=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/Fabric.csv")
Df.rename(columns={'Terry towels':'Terry Towels'},inplace=True)


# In[450]:


Df1=Df.melt(id_vars='Factors',value_vars=list(Df.columns[1:]))




# In[451]:


Df1.rename({'variable':'Materials','value':'Values'},axis=1,inplace=True)


# In[452]:


dF=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/lca.csv")
dF


# In[453]:


dF1=dF.melt(id_vars='Factors',value_vars=list(dF.columns[1:]))
dF1




# In[454]:


dF1.rename({'variable':'Materials','value':'Values'},axis=1,inplace=True)


# In[455]:


dp=pd.read_csv("C:/Users/CAROL/Desktop/Revolution Zero/Polyester.csv")
dp



# In[456]:


dp.dropna(axis=1,inplace=True)


# In[457]:


dp1=dp.melt(id_vars='Process',value_vars=list(dp.columns[1:]))





# In[458]:


dp1.rename({'variable':'Factors','value':'Values'},axis=True, inplace=True)


# In[482]:


import plotly.express as px
import dash
from dash import dcc
from dash import  html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import plotly.express as px

# Iris bar figure
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="Washers", y="Values", color="Factors",
                        color_discrete_map={'Detergents':'#d62728','Energy(MJ)':'#ED9121','Water(L)':'#00FFF5'})
                        
                    .update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(8, 73, 123, 2)',
                        #paper_bgcolor= 'rgba(0,0,0,0)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

# Text field
def drawFigure1():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(DF1,x="Materials",y="Values",color="Factors",
                                  color_discrete_map={'CO2(KGs)':'#d62728','Energy(MJ)':'#ED9121','Water(L)':'#00FFF5'})
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(8, 73, 123, 2)',
                        #paper_bgcolor= 'rgba(9, 74, 123, 1)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])


def drawFigure2():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        Df1,x="Materials",y="Values",color="Factors",
                        
                        color_discrete_map={'CO2(KGs)':'#d62728','Energy(MJ)':'#ED9121','Water(L)':'#00FFF5'})
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(6, 72, 120, 4)',
                        #paper_bgcolor= 'rgba(9, 74, 122, 1)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])

def drawFigure3():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        dF1,x="Materials",y="Values",color="Factors",
                        color_discrete_map={'CO2(KGs)':'#d62728','Energy(MJ)':'#ED9121','Water(L)':'#00FFF5'})
                                 
                    .update_layout( 
                        template='plotly_dark',
                         plot_bgcolor= 'rgba(5, 72, 119, 5)',
                        #paper_bgcolor= 'rgba(0,0,0,0)',
                        #color_discrete_sequence = ['purple','blue','red'],
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])

def drawFigure4():
    return html.Div([ 
        dbc.Card( 
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(                        
                        dp1,x="Process",y="Values",color="Factors",                        
                        color_discrete_map={'CO2(KGs)':'#d62728','Energy(MJ)':'#ED9121','Water(L)':'#00FFF5'})
                    
                    .update_layout( 
                        template='plotly_dark',
                        
                        plot_bgcolor='rgba(9, 74, 122, 1)',
                        #paper_bgcolor='rgba(9, 74, 122, 1)',
                        
                    ),
                    config={ 
                         'displayModeBar': False
                        
                    }
                                  
                    
                    )
                    
                
            ])
        ),
    ])
#draw text1
def drawText1():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Re-Usable Surgical Instruments"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])


# Drawtext2
def drawText2():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("LCA for Cotton Sheets"),
                ], style={'textAlign': 'center','font':12}) 
            ])
        ),
    ])


def drawText3():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("LCA for Cotton  Fabric Production"),
                    
                ], style={'textAlign': 'center','font':12,})
            ])
        ),
    ])



def drawText4():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("LCA for Polyester/Cotton Shirts "),
                ], style={'textAlign': 'center','font':12}) 
            ])
        ),
    ])

def drawText5():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("LCA for Fibre Production"),
                ], style={'textAlign': 'center','font':9}) 
            ])
        ),
    ])

def drawText6():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2(""),
                ], style={'textAlign': 'center','color':'red'})
            ])
        ),
    ])




# Build App
app = dash.Dash(__name__,
                  
    external_stylesheets=[dbc.themes.BOOTSTRAP],
                  meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                 )
server=app.server
                 
colors={'background':'#000000','text':'#000000'}

app.layout = html.Div(style={'backgroundColor':colors['background']},children=[
    
    html.Div([ 
        html.H1(" Revolution-ZEROs Collection of  Life Cycle Analysis(LCA) Data from Reports")
        
    ],style={'textAlign':'center','color':'#FFFFFF'}),
    
    
    dbc.Card(         
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText1()
                ],style={"color":"dark"},xs=12,md=6, lg=4),
                dbc.Col([
                    drawText2()
                ],xs=12,md=6, lg=4),
                dbc.Col([
                    drawText3()
                ],style={},xs=12,md=6, lg=4),
                ],align='center'),            
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure() 
                ],style={'background':'#000000'}, xs=12,md=6, lg=4),
                dbc.Col([
                    drawFigure1()
                ], xs=12, md=6,lg=4),
                dbc.Col([
                    drawFigure2() 
                ], xs=12,md=6, lg=4),
                
               ],align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([ 
                    drawText4()                  
                    
                ],xs=12,md=6, lg=4),
                dbc.Col([
                    drawText5()
                ],xs=12,md=6, lg=4),
                dbc.Col([ 
                    drawText6()
                
                ],xs=12,md=6, lg=4)
                ],align='center'), 
             html.Br(),
            dbc.Row([
                dbc.Col([ 
                    drawFigure4()       
                    
                ],xs=12,md=6, lg=4),
                
                dbc.Col([
                    drawFigure3()
                
                ],style={'color':'dark'},xs=12,md=6, lg=4),
                 dbc.Col([ 

                   html.Img(src = app.get_asset_url('logo.jpg'),style={'height':'100%','width':'100%'}),
                    
                ],style={'textAlign':'bottom'},xs=12,md=6, lg=4),
                              
               
            ],align='center'), 
                 
        ]), color = 'dark'
    )
])

# Run app and display result inline in the notebook
app.run_server(port='8055',debug=True)


# In[ ]:




