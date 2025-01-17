import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np


class BoxExercise:
    
    @staticmethod
    def plot():
        
        df = pd.read_csv('./data/abalone.csv')

        # take two random samples of different sizes:
        a = np.random.choice(df['rings'],30,replace=False)
        b = np.random.choice(df['rings'],100,replace=False)

        # create a data variable with two Box plots:
        data = [
            go.Box(
                y=a,
                name='A'
            ),
            go.Box(
                y=b,
                name='B'
            )
        ]

        # add a layout
        layout = go.Layout(
            title = 'Comparison of two samples taken from the same population'
        )

        # create a fig from data & layout, and plot the fig
        fig = go.Figure(data=data, layout=layout)
        pyo.plot(fig, filename='solution5.html')
        