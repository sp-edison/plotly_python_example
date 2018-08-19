# -*- coding: utf-8 -*-
import sys, os, getopt

import json
from plotly.utils import PlotlyJSONEncoder
from plotly.offline import download_plotlyjs
import plotly.graph_objs as go
import pandas as pd

def plotlyfig2json(fig, fpath=None):
    redata = json.loads(json.dumps(fig.data, cls=PlotlyJSONEncoder))
    relayout = json.loads(json.dumps(fig.layout, cls=PlotlyJSONEncoder))
    fig_json=json.dumps({'data': redata,'layout': relayout})
    if fpath:
        with open(fpath, 'wb') as f:
            f.write(fig_json)
    else:
        return fig_json


if __name__ == "__main__" :
    try:
        otps, args = getopt.getopt(sys.argv[1:], "i:")
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(-1)

    for opt, arg in otps :
        if opt in "-i" :
            f_input = open(arg, "r")
            output_name = arg.split('/')[-1].split('.')[0]

    row_data = pd.read_csv(f_input, header=None, delimiter=r"\s+")

    data = [
        go.Heatmap(
            z=row_data.transpose().as_matrix(),
            zsmooth = 'best',
            showscale = True,
            connectgaps = True
        )
    ]

    axis_layout = dict(
        showgrid = True,
        zeroline = False,
        showticklabels = False,
        ticks = ''
    )

    layout = go.Layout(
        autosize = False,
        xaxis = axis_layout,
        yaxis = axis_layout,
    )

    fig = go.Figure(data=data, layout=layout)

    if not os.path.exists('result'):
        os.makedirs('result')

    plotlyfig2json(fig, 'result/' + output_name + '.ply')
