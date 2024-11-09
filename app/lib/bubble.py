import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

class Bubble:
    
    @staticmethod
    def plot():
        
        df = pd.read_csv('./data/mpg.csv')
        
        # Dataframe bugfix
        df['horsepower'] = df['horsepower'].replace(['?'], np.nan).astype('float32')
        
        data = [go.Scatter(
            x=df['horsepower'], 
            y=df['mpg'], 
            text=df['name'], 
            mode='markers', 
            marker=dict(size=df['weight']/100, color=df['cylinders'], showscale=True)
        )]
        
        layout = go.Layout(title="Bubble Chart", hovermode='closest')
        
        fig = go.Figure(data=data, layout=layout)
        pyo.plot(fig)
