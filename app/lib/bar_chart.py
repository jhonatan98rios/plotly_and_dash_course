import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

class BarChart:
    
    @staticmethod
    def plot():
        
        df = pd.read_csv('./data/2018WinterOlympics.csv')
        print(df.head(10))
        
        gold_trace = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold', marker={'color': '#FFD700'})
        silver_trace = go.Bar(x=df['NOC'], y=df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
        bronze_trace = go.Bar(x=df['NOC'], y=df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
        
        data = [gold_trace, silver_trace, bronze_trace]
        layout = go.Layout(title='Medals', barmode='stack') # 'stack', 'group', 'overlay', 'relative'
        fig = go.Figure(data=data, layout=layout)       
        
        pyo.plot(fig)
