# GOAL: this code has the goal to compute and visualize the electric field (E) for two point charges in 2D space by 
# fieldlines, since vector-field visualization with normal vectors become very very polluted very very fast. 
# NOTE: This is a code that it's main objective is numpy and physics study - do not expect smart things here. 

# LIBRARIES
import numpy as np                  # numpy for computations
import matplotlib.pyplot as plt     # matplotlib for viewing

def generate_grid(gridsize : int, grid_subdivisions : int) -> tuple:
    """generates the 2d space for the electric field

    Args:
        gridsize (int): the size of the 2d space
        grid_subdivions (int): the amount of "subdivisions" of the space - more subdivions = more precise 

    Returns:
        tuple: coordinate grid of the 2d space
    """

    # coordinate axis for the 2d space 
    x, y = np.linspace(-gridsize, gridsize, grid_subdivisions), np.linspace(-gridsize, gridsize, grid_subdivisions)
    # creates the coordinates and store them into variables 
    X, Y = np.meshgrid(x, y)
    coordinate_grid = (X, Y)

    return coordinate_grid

def generate_field(charges : list[tuple], coordinate_grid : tuple, k : float) -> tuple:
    """generates the electric field on the 2d space for multiple charges

    Args:
        charges (list[tuple]): each charge is represented by a tuple (x0, y0, q) where the first two entries are the 
        charge's coordinates and the third entry is it's strength (+ or - matters)

        coordinate_grid (tuple): the coordinate grid created by the 'generate grid' function

        k (float): electrostatic constant 

    Returns: 
        tuple: the electric field components 
    """

    # assigns the coordinate grid tuple to normal variables for ease computation
    X, Y = coordinate_grid

    # initializing the field components 
    Ex, Ey = np.zeros_like(X), np.zeros_like(Y)

    # computes the field components for each charge for every point in the space with numpy's array computation
    for (x0, y0, q) in charges:
        r = np.sqrt((X - x0)**2 + (Y - y0)**2)
        r3 = r**3
        Ex += k * q * (X - x0) / r3
        Ey += k * q * (Y - y0) / r3

    ef_components = (Ex, Ey)
    return ef_components

def plot_field(coordinate_grid : tuple, ef_components : tuple) -> None:
    """plots the generated field

    Args:
        coordinate_grid (tuple): the 2d space coordinate grid
        ef_components (tuple): the electric field components
    """

    # assign them to variables for ease manipulation
    X, Y = coordinate_grid
    Ex, Ey = ef_components

    # plots the streamlines 
    plt.figure(figsize=(8, 6))
    plt.streamplot(X, Y, Ex, Ey, color=np.sqrt(Ex**2 + Ey**2), cmap='coolwarm', linewidth=1, density=7)
    plt.title('Electric Field for Multiple Charges')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.colorbar(label='$|E|$')
    plt.grid(True)
    plt.show()