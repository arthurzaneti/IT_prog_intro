import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def write_data():
    poly = lambda x: x**8 -3*x**4 + 2*x**3 - 2*x**2 - x + 2
    x = np.linspace(-3/2, 3/2, 1000)
    y = poly(x)

    file = open("poly_graph_data.txt", "w")
    for i in range(len(x)):
        file.write(str((x[i], y[i])) + "\n")

def read_data():
    file = open("poly_graph_data.txt", "r")
    data = file.readlines()
    x = np.array()
    y = np.array()
    for i in range(len(data)):
        point = data[i][0:len(data[i]) - 1].split(",")
        print(point)
read_data()
print(np.array())



