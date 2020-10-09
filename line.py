#-*- coding: utf-8 -*-
# Drawing a single line figure
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
        'size': 10}

FigureSize=(4, 3.2)
markers = ['o', 'v', 's']


def plotlines(filepath, xlabel, ylabel, xlist, legendlist, scaling=1):#比较的柱状图,datalist包含一组list数据,xnamelist是横坐标值,legendlist为各组数据的名称
    plt.figure(figsize=FigureSize)
    # read data
    datalist = np.loadtxt(filepath).transpose()
    if len(datalist.shape) == 1:
        datalist = np.array([datalist])
    
    for i in range(len(datalist)): # the last one has solid line and full filling style
        ls =  'solid' if i == len(datalist) - 1 else 'dashed'
        cl = 'blue' if i == len(datalist) - 1 else 'black'
        fs = 'full' if i == len(datalist) - 1 else 'none'
        plt.plot(xlist, datalist[i] / scaling, c=cl, marker=markers[i], fillstyle = fs, linestyle=ls)

    # set legends
    plt.legend(legendlist)

    # set grid
    plt.grid(which = "major", axis="y", color='grey', linestyle='dotted', linewidth=0.5)
    
    # set labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # set ticks to rotate
    # plt.xticks(fontname = "Times New Roman", fontsize=10, rotation=45)
    
    # save the figure
    filepath_noext = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    plt.savefig(filepath_noext + ".svg", format="svg", bbox_inches='tight')
    plt.savefig(filepath_noext + ".png", dpi=600, bbox_inches='tight')


if __name__ == "__main__":
    plotlines('lookup.txt', 
              'number of operations (100k)', 
              'Excution time / (s)', 
              ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
              ["index1", "index2", "index3"],
            )