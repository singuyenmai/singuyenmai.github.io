#!/usr/bin/env python
def lorenz_system(state, t, sigma, rho, beta):
    
    # system state depends on three variables: x, y, z
    X, Y, Z = state
    
    # define the three ODEs describing the rates of change of the above three variables
    dX_dt = sigma * (Y - X)
    dY_dt = X * (rho - Z) - Y
    dZ_dt = X * Y - beta * Z
    
    # return a list of the ODEs
    return [dX_dt, dY_dt, dZ_dt]

# Define the system parameters sigma, rho, and beta
sigma = 10.
rho   = 28.
beta  = 8./3.

# Define the initial system state - a list of X, Y, Z values at the initial time point, respectively
initial_state = [2., 4., 5.5]

# Solve the ODE system with `odeint`
from scipy.integrate import odeint
import numpy as np

tps = np.linspace(0, 50, 50*100)
XYZp = odeint(lorenz_system, initial_state, tps, args=(sigma, rho, beta))
Xp = XYZp[:, 0]
Yp = XYZp[:, 1]
Zp = XYZp[:, 2]

import plotly.express as px
import plotly.graph_objects as go

import PIL
import io
# import plotly.express as px
# import pandas as pd
# import numpy as np
# r = np.random.RandomState(42)

# # sample data
# df = pd.DataFrame(
#     {
#         "step": np.repeat(np.arange(0, 8), 10),
#         "x": np.tile(np.linspace(0, 9, 10), 8),
#         "y": r.uniform(0, 5, 80),
#     }
# )

# # smaple plotly animated figure
# fig = px.bar(df, x="x", y="y", animation_frame="step")

fig = go.Figure(
        frames=[go.Frame(
        data=[
              go.Scatter3d(x=Xp, y=Yp, z=Zp,
                     mode="lines",
                     line=dict(width=4., color=tps, 
                               colorscale='Spectral', showscale=True,
                               colorbar=dict(lenmode='fraction', len=0.5, title="Time")
                               )),
              go.Scatter3d(x=[Xp[i]], y=[Yp[i]], z=[Zp[i]], marker=dict(color='black', size=4.), 
                           mode="markers")
             ])
            # for i in np.round(np.linspace(0, 1000-1, 50)).astype(int)]
            for i in np.round(np.linspace(0, 1000-1, 200)).astype(int)]
)
eps = 5
fig.update_layout(
    template="plotly_white", width=520, height=500, 
    margin=dict(l=0.5, r=0.5, t=0, b=0),
    showlegend=False,
    scene_camera=dict(eye=dict(x = 1.2, y = -1.2, z = 0.1)),
    scene_aspectratio=dict(x=0.5, y=0.7, z=0.7)
)

# generate images for each step in animation
frames = []
for s, fr in enumerate(fig.frames):
    # if len(frames) < 2:
    # set main traces to appropriate traces within plotly frame
    fig.update(data=fr.data)
    # generate image of current state
    im = PIL.Image.open(io.BytesIO(fig.to_image(format="png", scale=2)))
    frames.append(im.quantize(colors=250, method=PIL.Image.FASTOCTREE, dither=0))
    # else:
    #     break

# append duplicated last image more times, to keep animation stop at last status
for i in range(3):
    frames.append(frames[-1])
for i in range(3):
    frames.append(frames[0])

# create animated GIF
frames[0].save(
        "butterfly_fly.gif",
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=50,
        loop=0,
    )
