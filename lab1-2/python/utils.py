import numpy as np

def estimate_pose(x, X):
    """
    Args:
        x: 2D points with shape [2, N]
        X: 3D points with shape [3, N]
    Output:
        P: Camera matrix with shape [3, 4]
    """
    ###############################################################################################################
    ## TODO : You need to find Camera matrix P given 2D and 3D points x and X.
    # Hint: use linear regression for elements of P (assuming that P[2, 3] = 1)
    return P

def estimate_params(P):
    """
    Args:
        P: Camera matrix with shape [3,4]
    Output:
        (K, R, t) : intrinsic matrix K with shape [3,3],
                    rotation matrix R with shape[3,3],
                    translation t with shape [3,1]
    """
    ###############################################################################################################
    ## TODO : You need to estimate intrinsic matrix K, rotation matrix R, and translation t from given camera matrix P.

    return (K, R, t)

def project(P, X):
    N = X.shape[1]
    xProj = np.matmul(P, np.concatenate((X, np.ones((1, N))), axis=0))
    xProj[0, :] = xProj[0, :] / xProj[2, :]
    xProj[1, :] = xProj[1, :] / xProj[2, :]
    return xProj[:2, :]