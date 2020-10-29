import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import json

def show_points(data):
  data = np.array(data)
  x=data[:,0]
  y=data[:,1]
  z=data[:,2]
  fig = plt.figure(figsize=(12, 8))
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(x,y,z)
  fig = plt.figure(figsize=(12, 8))
  ax = fig.add_subplot(111, projection='3d')
  pnt3d=ax.scatter(x,y,z,c=z)
  cbar=plt.colorbar(pnt3d)
  cbar.set_label("Values (units)")
  plt.show()

def show3D(x,y,z):
  fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
  fig.update_traces(marker=dict(size=2,
                                line=dict(width=2,
                                          color='DarkSlateGrey')),
                    selector=dict(mode='markers'))
  fig.update_layout(
      autosize=False,
      width=1200,
      height=800,)
  fig.show()

def getXYZ(data):
  res = np.array(data)

  #res = res[res[:,2] < 0]
  #res = res[res[:,2].argsort()]
  center = [248, -120, -40]
  """
  res = res[
            (res[:,0] > center[0] - 10) &
            (res[:,0] < center[0] + 10) &
            (res[:,1] > center[1] - 10) &
            (res[:,1] < center[1] + 10) 
            ]
  """
  x=res[:,0]
  y=res[:,1]
  z=res[:,2]
  return x, y, z

def getFromJson(json_name):
  with open(json_name) as json_file:
    return json.load(json_file)
