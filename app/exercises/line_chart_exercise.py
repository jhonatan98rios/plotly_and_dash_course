import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

class LineChartExercise:
    
    @staticmethod
    def plot():
        
        df = pd.read_csv('./data/2010YumaAZ.csv')
        
        # go.Scatter retorna um dataframe simples
        
        # data = [go.Scatter(
        #     x=df['LST_TIME'], 
        #     y=df[df['DAY'] == day]['T_HR_AVG'], 
        #     mode='lines', 
        #     name=day
        # ) for day in df['DAY'].unique()]
        
        data = [{
            'x': df['LST_TIME'], 
            'y': df[df['DAY'] == day]['T_HR_AVG'], 
            'mode': 'lines', 
            'name': day
        } for day in df['DAY'].unique()]
        
        
        layout = go.Layout(title="Daily temp avgs")
        fig = go.Figure(data=data, layout=layout)
        
        pyo.plot(fig)
