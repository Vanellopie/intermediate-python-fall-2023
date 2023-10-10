import matplotlib.pyplot as plt

def scatter_plot(x, y, title="Scatter Plot"):
    """
    Create a scatter plot of two variables.

    Args:
        x (list or pd.Series): Data for the x-axis.
        y (list or pd.Series): Data for the y-axis.
        title (str, optional): Title of the plot. Default is "Scatter Plot".

    Returns:
        None
    """
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()
