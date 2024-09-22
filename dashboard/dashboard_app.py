import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import sqlite3

# Inicialização do app Dash
app = dash.Dash(__name__)
app.title = "Monitoramento de Vazamento de Gás"

app.layout = html.Div([
    html.H1("Monitoramento de Vazamento de Gás"),
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=5*1000,  # Atualiza a cada 5 segundos
        n_intervals=0
    )
])

@app.callback(Output('live-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    # Conectar ao banco de dados
    conn = sqlite3.connect('../backend/gas_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, value FROM gas_data ORDER BY timestamp DESC LIMIT 20")
    data = cursor.fetchall()
    conn.close()

    # Processar dados
    timestamps = [row[0] for row in data][::-1]
    values = [row[1] for row in data][::-1]

    trace = go.Scatter(
        x=timestamps,
        y=values,
        mode='lines+markers',
        name='Gás Detectado',
        line=dict(color='firebrick', width=2)
    )

    layout = go.Layout(
        title='Níveis de Gás em Tempo Real',
        xaxis=dict(title='Timestamp'),
        yaxis=dict(title='Valor do Sensor', range=[0, 1]),
        template='plotly_dark'
    )

    return {'data': [trace], 'layout': layout}

if __name__ == '__main__':
    app.run_server(debug=True)
