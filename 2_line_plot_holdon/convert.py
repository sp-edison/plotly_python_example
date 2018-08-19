import sys
import os
import getopt

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



if __name__ == "__main__": 
	try:
		otps, args = getopt.getopt(sys.argv[1:], "i:")
	except getopt.GetoptError as err:
		print(str(err))
		sys.exit(1)

	for opt, arg in otps:
		if opt in "-i":
			f_input = open(arg, "r")
			output_name = arg.split('/')[-1].split('.')[0];

	xy_data = pd.read_csv(f_input, header=None, delimiter=r"\s+");

	f_input.close();

	trace1 = go.Scatter (
		x = xy_data[0],
		y = xy_data[1],
		name = 'S11',
	)
	trace2 = go.Scatter (
		x = xy_data[0],
		y = xy_data[2],
		name = 'S112',			
	)
	data = [trace1, trace2];


	layout = go.Layout(
		showlegend=True,
		title="S11",
		xaxis=dict(
			title='Frequency [GHz]',	
		),
		yaxis=dict(
			title='Magnitude of S11',
		),
	);

	fig = go.Figure(data=data, layout=layout);

	if not os.path.exists('result'):
		os.makedirs('result');

	plotlyfig2json(fig, 'result/' + output_name + '.ply');

