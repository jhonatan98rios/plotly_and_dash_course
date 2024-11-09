import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

import pandas as pd
import numpy as np

class WebGL:
    
    @staticmethod
    def plot():
        
        np.random.seed(1)
        N = 100000
        data = dict(x=np.random.randn(N), y=np.random.randn(N))
        df = pd.DataFrame(data)

        fig = px.scatter(df, x="x", y="y", render_mode='webgl')
        fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))

        fig.show()
        
