import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def main():
    # Read iris.csv file using pandas library
    df = pd.read_csv('iris.csv')

    # TODO: Plot petal_width vs petal_length
    sns.relplot(data=df, x='petal_width', y='petal_length', hue='species')
    # TODO: Change the axis labels and title of the graph
    plt.title('Petal Width vs Length')
    plt.xlabel('Petal Width (cm)')
    plt.ylabel('Petal Length (cm)')

    # Save the plot to a file
    # For this problem, we need an extra parameter for a better layout.
    plt.savefig('plot.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
