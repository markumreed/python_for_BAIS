#data_visualization.py
import matplotlib.pyplot as plt

def plot_sales(data):
    plt.plot(data)
    plt.title("Sales Over Time")
    plt.xlabel("Time")
    plt.ylabel("Sales")
    plt.show()

def plot_bar_chart(data, labels):
    plt.bar(labels, data)
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.show()