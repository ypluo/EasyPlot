#-*- coding: utf-8 -*-
# Drawing mutli sub bar figures
# CopyRight(c) Yongping Luo, All rights reserved!

import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.ticker as mtick
import numpy as np
import os
import datetime
from matplotlib.transforms import Bbox

mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12

letterfont = {
        'family': 'Times New Roman',
        'style': 'normal',
        'weight': 'normal',
        'color': 'black',
        'size': 10}

hatchlist=['/', '.', '\\', '//\\\\', '*'] # change this to get different bar hatch
group_distance = 0.18 # control the distance between two groups, value in (0, 0.4)
bar_distance   = 0.10 # control the distance between two bars,  value in (0, 0.2)

def plotax(ax, filepath, xlabel, ylabel, xlist, title, legendlist, scaling):
    datalist = np.loadtxt(filepath).transpose()
    
    # the shape of the data is (n, 1), after a transpose, it turn to one dimension, which is not expected
    if len(datalist.shape) == 1:
        datalist = np.array([datalist])

    xcount = len(xlist)
    bar_count = len(datalist)
    x = np.array([i for i in range(xcount)], dtype=np.float32)

    if bar_count == 1:
        bar_width = (1 - group_distance) / bar_count
    else :
        bar_width = (1 - group_distance) / bar_count - bar_distance / (bar_count - 1)

    # plot the bar first
    for i in range(bar_count):
        barcolor = 'blue' if i == bar_count - 1 else 'None'
        hatch = '' if i == bar_count - 1 else hatchlist[i]
        # plot bars
        ax.bar(x, datalist[i] / scaling, width = bar_width, edgecolor="black", color=barcolor, hatch=hatch)
        # update position to plot bar
        x += (1 - group_distance) / bar_count
    
    # plot xticks at the middle of bars, Do not modify here
    x = np.array([i for i in range(xcount)], dtype=np.float32)
    x = x + (1 - group_distance) / 2 - (1 - group_distance) / bar_count / 2
    ax.set_xticks(x)
    ax.set_xticklabels(xlist)

    # plot grid
    ax.grid(which = "major", axis="y", color='grey', linestyle='dotted', linewidth=0.5)

    # set title
    ax.set_title(title, fontdict=letterfont)
    # set label
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


def plotbars(filepaths, xlabel, ylabel, xlist, legendlist, titles, scaling = 1):
    width = 3.25 * len(filepaths)
    height = 2.4
    fig_box = Bbox([[1, 0], [width - 1, height + 0.4]])

    fig, axes = plt.subplots(1, len(filepaths), figsize = (width, height))

    # plot multi sub-figures
    for i in range(len(filepaths)):
        share_ylabel = ylabel if i == 0 else ''
        plotax(axes[i], filepaths[i], xlabel, share_ylabel, xlist, titles[i], legendlist, scaling);

    # set glabol legend and y label
    fig.legend(legendlist, loc = "upper center", bbox_to_anchor=(0.435, 1.15), ncol = 3, frameon=True)
    
    filepath_noext = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    plt.savefig(filepath_noext + ".svg", format="svg",bbox_inches= fig_box )
    plt.savefig(filepath_noext+".png", bbox_inches= fig_box, dpi=600)

if __name__ == "__main__":
    plotbars(
                ['clwb.txt', 'clwb.txt', 'clwb.txt', 'clwb.txt'], 
                'number of operations',
                'clwb number (million)',
                ['200k', '400k', '600k', '800k', '1000k'],
                ["index1", "index2", "index3"],
                ["(a).lookup", "(b).insert", "(c).update", "(d).delete"],
                (1024 * 1024)
            )
