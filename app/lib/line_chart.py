import plotly.offline as pyo
import numpy as np
import plotly.graph_objs as go

class LineChart:
    
    @staticmethod
    def plot():
        np.random.seed(56)
        
        # Generating random data
        x_values = np.linspace(0,1,100)
        y_values = np.random.randn(100)
        
        # Structuing data on Plotly scatter graph
        markers_trace = go.Scatter(x=x_values, y=y_values+5, mode='markers', name='markers')
        
        line_trace =  go.Scatter(x=x_values, y=y_values, mode='lines', name='lines')
        
        mixed_trace =  go.Scatter(x=x_values, y=y_values-5, mode='lines+markers', name='lines+markers')
        
        data = [markers_trace, line_trace, mixed_trace]
        
         # Apply the layout atttributes such as title, and subtitles
        layout = go.Layout(title='Line Charts')
        
        # Create a image
        fig = go.Figure(data=data, layout=layout)
        
        # Run plotly on browser
        pyo.plot(fig)