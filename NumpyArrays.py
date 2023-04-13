# Numpy arrays are great alternatives to Python Lists
# they allow math operatoinswit lists

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# Calculating Body Mass Index (BMI) and other handy features of NumpyArrays

BMI = np_weight/np_height

print(f"BMI results \n {BMI}")
print(f"Indexes above 23 \n {BMI > 23}")

# Exercise

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight = np.array(weight_kg)
    
# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight*0.454

# Print out np_weight_lbs
print(np_weight_lbs)
