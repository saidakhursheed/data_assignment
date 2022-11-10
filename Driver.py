import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def display_line_plot():
    df = pd.read_csv("data/spotify.csv")

    # pick every 5th row in order to improve readability of visualization
    df = df[df.index % 5 == 0]

    plt.plot(df["Date"], df["Shape of You"],)
    plt.plot(df["Date"], df["Despacito"])
    plt.plot(df["Date"], df["Something Just Like This"])
    plt.plot(df["Date"], df["HUMBLE."])
    plt.plot(df["Date"], df["Unforgettable"])
    plt.legend(["Shape of You", "Despacito",
               "Something Just Like This", "HUMBLE.", "Unforgettable"])
    plt.xlabel("Dates")
    plt.ylabel("Global Daily Streams")
    plt.title("Streaming of Songs on Spotify")
    plt.xticks(rotation=90)
    plt.show()


def display_bar_plot_util(x, height, xLabel="", yLabel="", title=""):
    plt.bar(x, height)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()


def display_bar_plot():
    df = pd.read_csv("data/spotify.csv")
    x = df.columns.values.tolist()[1:]
    df = df.dropna()
    height = df.iloc[1].values.tolist()[1:]
    xLabel = "Songs"
    yLabel = "Hits"
    title = "Songs Streamed on Spotify on " + df.iloc[1].values.tolist()[0]
    display_bar_plot_util(x, height, xLabel, yLabel, title)

def display_scatter_plot():
    df = pd.read_csv("data/spotify.csv")
    # pick every 4th row in order to improve readability of visualization
    columns = df.columns.values.tolist()
    df = df[df.index % 4 == 0]
    plt.scatter(df[columns[0]], df[columns[2]])
    plt.xlabel(columns[0])
    plt.ylabel("Streams")
    plt.xticks(rotation=90)
    plt.title(columns[2] + " Global Streams on Spotify")
    plt.show()

def main():
    choice = input(
        "Choose 1 of the following: \n1.Line Plot\n2.Bar Plot\n3.Scatter Plot\nChoice: ")
    if choice == "1":
        display_line_plot()
    elif choice == "2":
        display_bar_plot()
    elif choice == "3":
        display_scatter_plot()
    else:
        print("Invalid Choice!")


if __name__ == "__main__":
    main()



# Data set
# https://www.kaggle.com/code/alexisbcook/line-charts/data?select=spotify.csv
