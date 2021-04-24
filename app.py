import plotly_express as px
import csv
import numpy as np


def getDataSource():
    icecream = []
    temperature = []
    with open("csv/data.csv") as f:
        df = csv.DictReader(f)
        for row in df:
            temperature.append(float(row["Temperature"]))
            icecream.append(float(row["Ice-cream Sales"]))
    return {"x": temperature, "y": icecream}


def findCorrelation(source):
    corr_coeff = np.corrcoef(source["x"], source["y"])
    correlation = corr_coeff[0, 1]
    print("Correlation is: ", correlation)


def plotFigure():
    with open("csv/data.csv") as f:
        df = csv.DictReader(f)
        px.scatter(df, x="Temperature", y="Ice-cream Sales").show()


def main():
    findCorrelation(getDataSource())
    plotFigure()


if __name__ == "__main__":
    main()
