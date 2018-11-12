import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('../data/sp500_px.csv')
df = df[['CVX','XOM','AAPL']]

app = dash.Dash()

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
  
  html.H1(children='Dash Demo'),

  dcc.Graph(
    id='scatter3d',
    figure={
      'data': [go.Scatter3d(x=df['CVX'],y=df['XOM'],z=df['AAPL'],
                            mode='markers',
                            marker=dict(size=5,opacity=0.2))],
      'layout': go.Layout(scene = dict(xaxis=dict(title='CVX'),
                                       yaxis=dict(title='XOM'),
                                       zaxis=dict(title='AAPL')))
                                       }
                                       )
  ]
  )


if __name__ == '__main__':
    app.run_server()
