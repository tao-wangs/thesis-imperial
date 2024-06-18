import itertools
import jax
import matplotlib.pyplot as plt
import numpy as np 
from pgmax import fgraph, vgroup, factor, infer
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import plotly.io as pio

def compute_marginals(potentials):
    # N = 10
    # nodes = ['A', 'B']
    nodes = list(range(2))
    variables = vgroup.VarDict(num_states=2, variable_names=nodes)
    fg = fgraph.FactorGraph(variable_groups=[variables])   

    # Add pairwise factors e.g:
    # array([[0, 0],
    #        [0, 1],
    #        [1, 0],
    #        [1, 1]])
    unary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=1)))
    binary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=2)))
    ternary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=3)))

    # add factors 

    # A1B
    AB = factor.EnumFactor(
            variables = [variables[0], variables[1]],
            factor_configs = binary_factor_configs, 
            log_potentials=np.log(potentials)
        )

    fg.add_factors([AB])


    bp = infer.BP(fg.bp_state, temperature=1.0)
    bp_arrays = bp.init()
    bp_arrays = bp.run(bp_arrays, num_iters=50, damping=0.5)
    beliefs = bp.get_beliefs(bp_arrays)
    marginals = infer.get_marginals(beliefs)

    result = None 

    for key, array in list(marginals.values())[0].items():
        print(f"Key {key}: {array}")
        result = array[1]
    
    return result


# Define the function Pr(C) as a simple linear combination for demonstration purposes

# Define the data points
pe_values = np.linspace(0, 0.5, 10)
pz_values = np.linspace(0, 0.5, 10)
pe, pz = np.meshgrid(pe_values, pz_values)
marginals = np.zeros(pe.shape)

# Compute the marginals for each pair (pe, pz)
for i in range(pe.shape[0]):
    for j in range(pe.shape[1]):
        pei = pe[i, j]
        pzi = pz[i, j]
        pl = 1 - (1 - pei) * (1 - pzi)
        potentials = np.array([0., 0., (1 - pl) * 0.14, 1 - (1 - pl) * 0.14], dtype=np.float32)
        prob = compute_marginals(potentials)
        marginals[i, j] = prob

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(pe, pz, marginals, cmap='sunsetdark')

# Add labels
ax.set_xlabel('p_e')
ax.set_ylabel('p_z')
ax.set_zlabel('Pr(B)')

# Show the plot
plt.show()
plt.savefig('3d_axes_plot.png')

# Plot using Plotly
# fig = go.Figure(data=[go.Surface(z=marginals, x=pe, y=pz, colorscale='sunsetdark')])


# camera = dict(
#     eye=dict(x=2, y=2, z=0.1)  # Adjust these values to set the view angle
# )


# # Add labels
# fig.update_layout(
#     scene=dict(
#         xaxis_title='p_e',
#         yaxis_title='p_z',
#         zaxis_title='Pr(B)',
#         camera=camera
#     )
# )

# fig.update_layout(scene_camera=camera, autosize=False,
#                   width=500, height=500,
#                   margin=dict(l=65, r=50, b=65, t=90))
# # fig.show()
# # # Show the plot
# # fig.show()
# pio.write_image(fig, 'marginals_surface_plot.svg')

# Create the surface plot
# surface = go.Surface(z=marginals, x=pe, y=pz, colorscale='Viridis', showscale=True)

# # Create the wireframe grid
# mesh_x, mesh_y = np.meshgrid(pe_values, pz_values)
# wireframe = go.Scatter3d(
#     x=mesh_x.flatten(),
#     y=mesh_y.flatten(),
#     z=marginals.flatten(),
#     mode='lines',
#     line=dict(color='black', width=2)
# )

# # Combine the surface and wireframe in one plot
# fig = go.Figure(data=[surface, wireframe])

# # Adjust camera view
# camera = dict(
#     eye=dict(x=2.0, y=2.0, z=0.1)  # Adjust these values to set the view angle
# )

# # Add labels and update layout with grid structure
# fig.update_layout(
#     title='Marginals as a function of $p_e$ and $p_z$',
#     scene=dict(
#         xaxis=dict(title='$p_e$', showgrid=True, gridcolor='white', gridwidth=2),
#         yaxis=dict(title='$p_z$', showgrid=True, gridcolor='white', gridwidth=2),
#         zaxis=dict(title='Pr(B)', showgrid=True, gridcolor='white', gridwidth=2),
#         camera=camera,
#         bgcolor='rgba(0,0,0,0)'
#     )
# )

# # Save as a static image
# # pio.write_image(fig, 'marginals_surface_plot.png')

# # Save as an interactive HTML file
# # fig.write_html('marginals_surface_plot.html')

# # Show the plot
# # fig.show()

# pio.write_image(fig, 'marginals_surface_plot2.svg')