import open3d as o3d
import numpy as np
import trimesh
import cv2
from matplotlib import pyplot as plt

"""
1) make cube with triangle mesh
"""

# mesh data consists of vertices and triangles
# Fill the appropriate values in the vertices array and triangles array to make a zero-centered cube
# with length 2.

cube = o3d.geometry.TriangleMesh()
###############################################################
##########################  TODO  #############################
###############################################################
vertices = np.array([[],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     []])

triangles = np.array([[],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      []], dtype=np.int32)
###############################################################
###############################################################
cube.vertices = o3d.utility.Vector3dVector(vertices)
cube.triangles = o3d.utility.Vector3iVector(triangles)
cube = cube.compute_vertex_normals()
o3d.visualization.draw_geometries([cube])

"""
2) Add texture to a mesh
"""
text = cv2.imread('../data/cube_texture.png')

###############################################################
##########################  TODO  #############################
###############################################################
v_uv = np.array([[],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 []])
###############################################################
###############################################################

cube.triangle_uvs = o3d.utility.Vector2dVector(v_uv)
cube.textures = [o3d.geometry.Image(text)]
o3d.io.write_triangle_mesh('../data/cube_texture.obj', cube)
