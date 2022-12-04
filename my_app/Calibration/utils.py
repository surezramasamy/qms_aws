import uuid, base64
from .models import *
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

'''Fixturres and templates'''
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph



def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

def get_plot(x,y):
    plt.switch_backend ('AGG')
    plt.figure(figsize=(5,4))
    plt.title("Fixture Verification Status")
    plt.bar(x,y)
    addlabels(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Status')
    plt.tight_layout()
    graph=get_graph()
    return graph

def addlabels1(x1,y1):
    for i in range(len(x1)):
        plt.text(i, y1[i], y1[i], ha = 'center')

def get_plot1(x1,y1):
    plt.switch_backend ('AGG')
    plt.figure(figsize=(5,4))
    plt.title("Locationwise Fixtures")
    plt.bar(x1,y1)
    addlabels1(x1,y1)
    plt.xticks(rotation=45)
    plt.xlabel('Location_used')
    plt.tight_layout()
    graph1=get_graph()
    return graph1



def get_plot2(df4):

    plt.switch_backend ('AGG')
    ax = df4.plot.bar(x='month2',title="Monthwise Plan vs Actual",figsize=(4,4))
    for c in ax.containers:
        ax.bar_label(c, label_type='edge')
    plt.xticks(fontsize=12)
    plt.ylabel('Nos',fontsize=12)
    plt.xlabel('Month',fontsize=12)
    plt.tight_layout()
    graph2=get_graph()
    return graph2

def get_plot3(df7):
    plt.switch_backend ('AGG')
    plt.figure(figsize=(2,1))
    colors = ['steelblue', 'orange', 'green']
    df7.plot.pie(y='count',autopct='%1.0f%%',colors=colors,title="% based on Verification Frequency in Months ")
    plt.tight_layout()
    graph3=get_graph()
    return graph3


def get_plot4(dframe2):
    plt.switch_backend ('AGG')
    ax = dframe2.plot.bar(stacked=True, color =['lightseagreen','Yellow', 'orange'],figsize=(6, 4), rot=0)
    for c in ax.containers:
        ax.bar_label(c, label_type='center')
    ax.legend(title='Location wise status', bbox_to_anchor=(1, 1), loc='upper left')
    plt.tight_layout()
    graph4=get_graph()
    return graph4

'''Instrucments'''
def get_plot5(x,y):
    plt.switch_backend ('AGG')
    plt.figure(figsize=(6,5))
    plt.title("Instrument Calibration Status")
    plt.bar(x,y)
    addlabels(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Status')
    plt.tight_layout()
    graph=get_graph()
    return graph

def get_plot6(df7):
    plt.switch_backend ('AGG')
    plt.figure(figsize=(6,4))
    colors = ['steelblue', 'orange', 'green']
    df7.plot.pie(y='count',autopct='%1.0f%%',colors=colors,title="% Calibration Frequency in Months ")
    plt.tight_layout()
    graph3=get_graph()
    return graph3
