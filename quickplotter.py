import os
import sys
import csv
import matplotlib.pyplot as plt
import pandas as pd
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(
    description='Train Mask R-CNN to detect balloons.')
parser.add_argument('x',
                    help="Header name for desired x variable")
parser.add_argument('y',
                    help="Header name for desired y variable")
parser.add_argument("-f", "--filepath",
                    action='append',
                    help='<Required> Set flag',
                    required=True)
args = parser.parse_args()

# create the plot
plt.figure(figsize = (20, 10))
x = args.x
y = args.y

# plot all the seperate datasets 
for i in range(len(args.filepath)):
    filepath = args.filepath[i]
    df = pd.read_csv(filepath, header = 0)
    plt.plot(df[x], df[y])

# save to local directory & display
plt.savefig("./my_plot")
plt.show()
