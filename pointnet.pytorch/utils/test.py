import numpy as np
from plyfile import PlyData

ply_file = '/home/vanttec/PointNet/Convert2ply/test/airplane/airplane_0711.ply'

# Read the .ply file
plydata = PlyData.read(ply_file)

# Extract vertex data
vertex_data = plydata['vertex']

# Get x, y, z coordinates
x = vertex_data['x']
y = vertex_data['y']
z = vertex_data['z']
vertices_array = np.vstack((vertex_data['x'], vertex_data['y'], vertex_data['z'])).T

print(f"{vertices_array.shape}")

