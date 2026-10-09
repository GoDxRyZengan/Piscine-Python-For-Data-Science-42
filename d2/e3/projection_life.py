from load_csv import load
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    df = load("life_expectancy_years.csv")
    df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
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

    df = load("population_total.csv")
    fr_row = df[df["country"] == "China"].iloc[0]
    fr_data = fr_row.drop("country")
    be_row = df[df["country"] == "Benin"].iloc[0]
    be_data = be_row.drop("country")
    fr_years = fr_data.index.astype(int)
    fr_population = fr_data.apply(convert_population)
    be_years = be_data.index.astype(int)
    be_population = be_data.apply(convert_population)
    fr_mask = fr_years <= 2060
    be_mask = be_years <= 2060
    fr_years = fr_years[fr_mask]
    fr_population = fr_population[fr_mask]
    be_years = be_years[be_mask]
    be_population = be_population[be_mask]
    sns.lineplot(x=fr_years, y=fr_population, label="China", color="green")
    sns.lineplot(x=be_years, y=be_population, label="Benin  ", color="blue")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda value, pos: f"{value:g}M"))
    plt.xticks(range(1800, 2060, 40))
    plt.yticks(range(0, 70, 20))
    plt.legend(loc='lower right')
    plt.show()
    return
if __name__ == "__main__":
    main()