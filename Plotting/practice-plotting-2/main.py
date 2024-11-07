import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def main():
    df = pd.read_csv('iris_missing.csv')

    df = df.fillna(0)

    sns.regplot(x ='petal_length', y ='sepal_length', data = df, color='g')
   
    plt.title('Petal Length vs Sepal Length')
    plt.ylabel('Sepal Length (cm)')
    plt.xlabel('Petal Length (cm)')
   
    plt.savefig('plot.png', bbox_inches='tight')

if __name__ == '__main__':
    main()

