'''import sys
import os
sys.path.append(os.path.dirname(__file__))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CovidAnalysis import ExportableCovidAnalysis   # Import your existing class


class CovidVisualization(ExportableCovidAnalysis):
    """Class to extend analysis with EDA and Matplotlib charts."""

    def __init__(self, csv_path="country_wise_latest.csv"):
        super().__init__(csv_path)

    # 1. Bar Chart of Top 10 Countries by Confirmed Cases
    def plot_top10_countries(self):
        data = self.top_countries(10)
        plt.figure(figsize=(10,6))
        plt.bar(data["Country/Region"], data["Confirmed"], color="skyblue")
        plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
        plt.xticks(rotation=45)
        plt.xlabel("Country")
        plt.ylabel("Confirmed Cases")
        plt.tight_layout()
        plt.show()

    # 2. Pie Chart of Global Death Distribution by Region
    def pie_death_distribution(self):
        deaths = self.df.groupby("WHO Region")["Deaths"].sum()
        plt.figure(figsize=(7,7))
        plt.pie(deaths, labels=deaths.index, autopct="%1.1f%%", startangle=90) # type: ignore
        plt.title("Global Death Distribution by Region")
        plt.show()

    # 3. Line Chart comparing Confirmed vs Deaths for Top 5 Countries
    def line_confirmed_vs_deaths(self):
        top5 = self.top_countries(5)["Country/Region"].values
        subset = self.df[self.df["Country/Region"].isin(top5)]
        plt.figure(figsize=(8,6))
        plt.plot(subset["Country/Region"], subset["Confirmed"], label="Confirmed", marker='o')
        plt.plot(subset["Country/Region"], subset["Deaths"], label="Deaths", marker='x')
        plt.title("Confirmed vs Deaths for Top 5 Countries")
        plt.legend()
        plt.xlabel("Country")
        plt.ylabel("Case Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 4. Scatter Plot of Confirmed vs Recovered
    def scatter_confirmed_vs_recovered(self):
        plt.figure(figsize=(8,6))
        plt.scatter(self.df["Confirmed"], self.df["Recovered"], alpha=0.7, color="teal")
        plt.title("Confirmed vs Recovered Cases (All Countries)")
        plt.xlabel("Confirmed")
        plt.ylabel("Recovered")
        plt.tight_layout()
        plt.show()

    # 5. Histogram of Death Counts across all Regions
    def hist_death_counts(self):
        plt.figure(figsize=(8,6))
        plt.hist(self.df["Deaths"], bins=20, color="salmon", edgecolor="black")
        plt.title("Distribution of Death Counts Across Regions")
        plt.xlabel("Deaths")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

    # 6. Stacked Bar Chart of Confirmed, Deaths, and Recovered for 5 Selected Countries
    def stacked_bar_cases(self):
        top5 = self.top_countries(5)["Country/Region"]
        subset = self.df[self.df["Country/Region"].isin(top5)]
        subset = subset.groupby("Country/Region")[["Confirmed", "Deaths", "Recovered"]].sum()

        subset.plot(
            kind="bar", stacked=True, figsize=(10,6),
            color=["#3498db","#e74c3c","#2ecc71"]
        )
        plt.title("Confirmed, Deaths, and Recovered for Top 5 Countries")
        plt.xlabel("Country")
        plt.ylabel("Number of Cases")
        plt.legend()
        plt.tight_layout()
        plt.show()

    # 7. Box Plot of Confirmed Cases across Regions
    def boxplot_confirmed_by_region(self):
        region_data = [self.df[self.df["WHO Region"]==region]["Confirmed"]
                       for region in self.df["WHO Region"].unique()]
        plt.figure(figsize=(10,6))
        plt.boxplot(region_data, labels=self.df["WHO Region"].unique()) # type: ignore
        plt.title("Boxplot of Confirmed Cases by Region")
        plt.xlabel("WHO Region")
        plt.ylabel("Confirmed Cases")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # 8. Trend Comparison: India vs Another Country
    def compare_trend(self, country1="India", country2="United States"):
        subset = self.df[self.df["Country/Region"].isin([country1, country2])]
        plt.figure(figsize=(8,6))
        plt.bar(subset["Country/Region"], subset["Confirmed"], color=["orange","steelblue"])
        plt.title(f"Confirmed Cases Comparison: {country1} vs {country2}")
        plt.ylabel("Confirmed Cases")
        plt.show()


if __name__ == "__main__":
    viz = CovidVisualization("country_wise_latest.csv")

    viz.plot_top10_countries()
    viz.pie_death_distribution()
    viz.line_confirmed_vs_deaths()
    viz.scatter_confirmed_vs_recovered()
    viz.hist_death_counts()
    viz.stacked_bar_cases()
    viz.boxplot_confirmed_by_region()
    viz.compare_trend("India", "United States")

'''
import sys
import os
sys.path.append(os.path.dirname(__file__))

import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend to avoid display issues

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CovidAnalysis import ExportableCovidAnalysis   # Make sure this is correct


class CovidVisualization(ExportableCovidAnalysis):
    """Class to extend analysis with EDA and Matplotlib charts."""

    def __init__(self, csv_path="country_wise_latest.csv"):
        super().__init__(csv_path)

    def plot_top10_countries(self, ax):
        data = self.top_countries(10)
        ax.bar(data["Country/Region"], data["Confirmed"], color="skyblue")
        ax.set_title("Top 10 Countries by Confirmed COVID-19 Cases", fontsize=14)
        ax.set_xlabel("Country", fontsize=12)
        ax.set_ylabel("Confirmed Cases", fontsize=12)
        ax.set_xticks(np.arange(len(data["Country/Region"])))
        ax.set_xticklabels(data["Country/Region"], rotation=45, ha="right", fontsize=10)

    def pie_death_distribution(self, ax):
        deaths = self.df.groupby("WHO Region")["Deaths"].sum()
        ax.pie(deaths, labels=deaths.index, autopct="%1.1f%%", startangle=90)
        ax.set_title("Global Death Distribution by Region", fontsize=14)

    def line_confirmed_vs_deaths(self, ax):
        top5 = self.top_countries(5)["Country/Region"].values
        subset = self.df[self.df["Country/Region"].isin(top5)]
        ax.plot(subset["Country/Region"], subset["Confirmed"], label="Confirmed", marker='o')
        ax.plot(subset["Country/Region"], subset["Deaths"], label="Deaths", marker='x')
        ax.set_title("Confirmed vs Deaths for Top 5 Countries", fontsize=14)
        ax.set_xlabel("Country", fontsize=12)
        ax.set_ylabel("Case Count", fontsize=12)
        ax.legend(fontsize=10)
        ax.set_xticks(np.arange(len(subset["Country/Region"])))
        ax.set_xticklabels(subset["Country/Region"], rotation=45, ha="right", fontsize=10)

    def scatter_confirmed_vs_recovered(self, ax):
        ax.scatter(self.df["Confirmed"], self.df["Recovered"], alpha=0.7, color="teal")
        ax.set_title("Confirmed vs Recovered Cases (All Countries)", fontsize=14)
        ax.set_xlabel("Confirmed", fontsize=12)
        ax.set_ylabel("Recovered", fontsize=12)

    def hist_death_counts(self, ax):
        ax.hist(self.df["Deaths"], bins=20, color="salmon", edgecolor="black")
        ax.set_title("Distribution of Death Counts Across Regions", fontsize=14)
        ax.set_xlabel("Deaths", fontsize=12)
        ax.set_ylabel("Frequency", fontsize=12)

    def stacked_bar_cases(self, ax):
        top5 = self.top_countries(5)["Country/Region"]
        subset = self.df[self.df["Country/Region"].isin(top5)]
        subset = subset.groupby("Country/Region")[["Confirmed", "Deaths", "Recovered"]].sum()
        subset.plot(kind="bar", stacked=True, ax=ax, color=["#3498db", "#e74c3c", "#2ecc71"])
        ax.set_title("Confirmed, Deaths, and Recovered for Top 5 Countries", fontsize=14)
        ax.set_xlabel("Country", fontsize=12)
        ax.set_ylabel("Number of Cases", fontsize=12)
        ax.tick_params(axis='x', rotation=45)

    def boxplot_confirmed_by_region(self, ax):
        regions = self.df["WHO Region"].unique()
        region_data = [self.df[self.df["WHO Region"] == region]["Confirmed"] for region in regions]
        ax.boxplot(region_data, tick_labels=regions)  # ✅ fixed deprecated 'labels'
        ax.set_title("Boxplot of Confirmed Cases by Region", fontsize=14)
        ax.set_xlabel("WHO Region", fontsize=12)
        ax.set_ylabel("Confirmed Cases", fontsize=12)
        ax.tick_params(axis='x', rotation=45)

    def compare_trend(self, country1="India", country2="United States", ax=None):
        subset = self.df[self.df["Country/Region"].isin([country1, country2])]
        ax.bar(subset["Country/Region"], subset["Confirmed"], color=["orange", "steelblue"]) # pyright: ignore[reportOptionalMemberAccess]
        ax.set_title(f"Confirmed Cases Comparison: {country1} vs {country2}", fontsize=14) # type: ignore
        ax.set_ylabel("Confirmed Cases", fontsize=12) # type: ignore

    def save_all_charts(self):
        # 📄 Page 1 - First 4 plots
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        plt.subplots_adjust(hspace=0.4, wspace=0.3)

        self.plot_top10_countries(axes[0, 0])
        self.pie_death_distribution(axes[0, 1])
        self.line_confirmed_vs_deaths(axes[1, 0])
        self.scatter_confirmed_vs_recovered(axes[1, 1])

        plt.savefig("page_1.png", dpi=300, bbox_inches="tight")
        plt.close()

        # 📄 Page 2 - Next 4 plots
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        plt.subplots_adjust(hspace=0.4, wspace=0.3)

        self.hist_death_counts(axes[0, 0])
        self.stacked_bar_cases(axes[0, 1])
        self.boxplot_confirmed_by_region(axes[1, 0])
        self.compare_trend("India", "United States", axes[1, 1])

        plt.savefig("page_2.png", dpi=300, bbox_inches="tight")
        plt.close()

        print("✅ Charts saved successfully as 'page_1.png' and 'page_2.png'.")


if __name__ == "__main__":
    viz = CovidVisualization("country_wise_latest.csv")
    viz.save_all_charts()
