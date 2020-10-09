#-*- coding: utf-8 -*-
# Drawing mutli sub line figures
# CopyRight(c) Yongping Luo, All rights reserved!

import matplotlib as mpl
import matplotlib.pylab as plt
import matplotlib.ticker as mtick
import numpy as np
import os
import datetime


mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 12

letterfont = {
        'family': 'Times New Roman',
        'style': 'normal',
        'weight': 'normal',
        'color': 'black',
        'size': 12}

markers = ['o', 'v', 's', '+']


def plotax(ax, filepath, xlabel, ylabel, xlist, title, scaling):
    datalist = np.loadtxt(filepath).transpose()
    
    for i in range(len(datalist)): # the last one has solid line and full filling style
        ls =  'solid' if i == len(datalist) - 1 else 'dashed'
        cl = 'blue' if i == len(datalist) - 1 else 'black'
        fs = 'full' if i == len(datalist) - 1 else 'none'
        ax.plot(xlist, datalist[i]/scaling, c=cl, marker=markers[i], fillstyle = fs, linestyle=ls)

    # plot grid
    ax.grid(which = "major", axis="y", color='grey', linestyle='dotted', linewidth=0.5)
    
    # set sub-figure title
    ax.set_title(title, fontdict = letterfont)

    # set labels
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    # set ticks
    ax.set_xticklabels(xlist)


def plotlines(filepaths, xlabel, ylabel, xlist, legendlist, titles, scaling = 1):
    FigureSize=(3.25 * len(filepaths), 2.4)
    fig, axes = plt.subplots(1, len(filepaths), figsize = FigureSize)

    # plot multi sub-figures
    for i in range(len(filepaths)):
        share_ylabel = ylabel if i == 0 else ''
        plotax(axes[i], filepaths[i], xlabel, share_ylabel, xlist, titles[i], scaling);

    # set glabol legend and y label
    lg = fig.legend(legendlist, loc = "upper center", bbox_to_anchor=(0.435, 1.25), ncol = 3, frameon=False)
    
    filepath_noext = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    plt.savefig(filepath_noext + ".svg", format="svg", bbox_inches='tight')
    plt.savefig(filepath_noext+".png", bbox_inches='tight', dpi=600)

if __name__ == "__main__":
    plotlines(
                ['lookup.txt', 'lookup.txt', 'lookup.txt', 'lookup.txt'], 
                'number of operations (100k)',
                'Excution time (s)', 
                ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                ["index1", "index2", "index3"],
                ["(a).lookup", "(b).insert", "(c).update", "(d).delete"],
            )
