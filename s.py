import plotly.express as px
import pandas as pd
import csv
import numpy as np
def Plotfig(datapath):
    with open(datapath) as csvfile:
        df=csv.DictReader(csvfile)
        fig=px.scatter(df,x="Marks",y="Days")
        fig.show()
def Getdatasource(datapath):
    Marks=[]
    Days=[]
    with open(datapath) as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            Marks.append(float(row["Marks"]))
            Days.append(float(row["Days"]))
    return {"x":Marks,"y":Days}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between Marks and Days",correlation[0,1])
datapath="C:/Users/Hp/Desktop/White HAt Junior/PYTHON/Project 106/Student.csv" 
datasource=Getdatasource(datapath)
findcorrelation(datasource)
Plotfig(datapath)                      