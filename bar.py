#-*- coding: utf-8 -*-
# Drawing a single bar figure
# CopyRight(c) Yongping Luo, All rights reserved!

import matplotlib as mpl
import matplotlib.pylab as plt
import os
import matplotlib.ticker as mtick
import numpy as np
import datetime

# set global font family and size
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12

letterfont = {
        'family': 'Times New Roman',
        'style': 'normal',
        'weight': 'bold',
        'color': 'black',
        'size': 12
}

FigureSize=(4, 3.2)
hatchlist=['/', 'o', '\\', '//\\\\', '*'] # change this to get different bar hatch
group_distance = 0.18 # control the distance between two groups, suggest value in (0, 0.4)
bar_distance   = 0.15 # control the distance between two bars, suggest value in [0, 0.2)
 
def plotbars(filepath, xlabel, ylabel, title, xlist, legendlist, scaling = 1):
    datalist = np.loadtxt(filepath).transpose()
    xcount = len(xlist)
    bar_count = len(datalist)
    x = np.array([i for i in range(xcount)], dtype=np.float32)

    # plot the bar first
    plt.figure(figsize=FigureSize)
    for i in range(bar_count):
        barcolor = 'blue' if i == bar_count - 1 else 'None'
        hatch = '' if i == bar_count - 1 else hatchlist[i]
        # plot bars
        bar_width = (1 - group_distance) / bar_count - bar_distance / (bar_count - 1)
        plt.bar(x, datalist[i] / scaling, width = bar_width, label=legendlist[i], edgecolor="black", color=barcolor, hatch=hatch)
        # update position to plot bar
        x += (1 - group_distance) / bar_count
    
    # plot xticks at the middle of bars, Do not modify here
    x = np.array([i for i in range(xcount)], dtype=np.float32)
    x = x + (1 - group_distance) / 2 - (1 - group_distance) / bar_count / 2
    plt.xticks(x, xlist)

    # plot grid
    plt.grid(which = "major", axis="y", color='grey', linestyle='dotted', linewidth=0.5)

    # plot the legend
    plt.legend()

    # set title
    plt.title(title)
    # set label
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # save the figure
    filepath_noext = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    plt.savefig(filepath_noext + ".svg", format = "svg", bbox_inches='tight')
    plt.savefig(filepath_noext + ".png", dpi=600, bbox_inches='tight')

if __name__ == "__main__":
    plotbars( 'clwb.txt',
              'number of operations (100k)',
              'clwb number (million)',
              '',
              ['200k', '400k', '600k', '800k', '1000k'],
              ["index1", "index2", "index3"],
              (1024 * 1024)
            )