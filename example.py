from main import *

charges = [(-1, -1, -1), (1, 1, 0.5)]

space = generate_grid(25, 100)

field_components = generate_field(charges, space, 1)

plot_field(space, field_components)