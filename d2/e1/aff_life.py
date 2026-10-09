from load_csv import load
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = load("life_expectancy_years.csv")
    fr_row = df[df["country"] == "France"].iloc[0]
    data = fr_row.drop("country")
    years = data.index.astype(int)
    life_expectancy = data.values
    sns.lineplot(x=years, y=life_expectancy)
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(range(1800, 2100, 40))
    plt.show()
    return

if __name__ == "__main__":
    main()