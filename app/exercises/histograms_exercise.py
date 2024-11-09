import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

class HistogramExercise:
    
    @staticmethod
    def plot():
        
        # create a DataFrame from the .csv file:
        df = pd.read_csv('./data/abalone.csv')

        # create a data variable:
        data = [go.Histogram(
            x=df['length'],
            xbins=dict(start=0,end=1,size=.02),
        )]

        # add a layout
        layout = go.Layout(
            title="Shell lengths from the Abalone dataset"
        )

        # create a fig from data & layout, and plot the fig
        fig = go.Figure(data=data, layout=layout)
        pyo.plot(fig, filename='solution6.html')
        
   