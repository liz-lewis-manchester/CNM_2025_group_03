import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# encoding latin1 to avoid error when reading mu
initial_conditions = pd.read_csv("initial_conditions.csv",encoding="latin1");

Distance=initial_conditions["Distance (m)"]
Concentration=initial_conditions["Concentration (µg/m_ )"]

# test that the file contents are read correctly
assert Distance[5] == 5
assert Concentration[5] == 8

# test that the columns in the file are equal length
assert len(Distance) == len(Concentration)
