# Paste this into a notebook cell and run
import pandas as pd
import numpy as np

CSV_PATH = "country_wise_latest.csv"  # adjust path if needed

class CovidAnalysis:
    """Core analysis methods for the COVID dataset."""
    def __init__(self, csv_path=CSV_PATH):
        self.df = pd.read_csv(csv_path)
        # normalize column names if necessary
        self.df.columns = [c.strip() for c in self.df.columns]
        # ensure numeric columns are typed correctly
        for col in ["Confirmed", "Deaths", "Recovered", "Active", "New cases", "New deaths", "New recovered"]:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors="coerce").fillna(0).astype(int)
    
    # 1. Summarize Case Counts by Region
    def summary_by_region(self):
        grp = self.df.groupby("WHO Region")[["Confirmed","Deaths","Recovered"]].sum()
        return grp.sort_values("Confirmed", ascending=False)
    
    # 2. Filter Low Case Records (confirmed < 10 removed)
    def filter_low_cases(self, threshold=10, column="Confirmed"):
        return self.df[self.df[column] >= threshold].copy()
    
    # 3. Region with Highest Confirmed Cases
    def region_with_highest_confirmed(self):
        s = self.df.groupby("WHO Region")["Confirmed"].sum()
        top_region = s.idxmax()
        return top_region, s.loc[top_region]
    
    # 4. Sort Data by Confirmed Cases (descending)
    def sorted_by_confirmed(self):
        return self.df.sort_values("Confirmed", ascending=False).reset_index(drop=True)
    
    # 5. Top N countries by case count
    def top_countries(self, n=5):
        return self.sorted_by_confirmed()[["Country/Region","Confirmed"]].head(n)
    
    # 6. Region with Lowest Death Count
    def region_with_lowest_deaths(self):
        s = self.df.groupby("WHO Region")["Deaths"].sum()
        bottom_region = s.idxmin()
        return bottom_region, s.loc[bottom_region]
    
    # 7. India's Case Summary
    def country_summary(self, country_name="India"):
        print("Inside q7 ---- comparison=======================")
        row = self.df[self.df["Country/Region"].str.lower() == country_name.lower()]
        if row.empty:
            return None
        # return as dict
        return row.iloc[0].to_dict()
    
    # 8. Mortality Rate by Region (Deaths / Confirmed)
    def mortality_rate_by_region(self):
        grp = self.df.groupby("WHO Region")[["Confirmed","Deaths"]].sum()
        grp["MortalityRate"] = grp["Deaths"] / grp["Confirmed"].replace(0, np.nan)
        return grp[["Confirmed","Deaths","MortalityRate"]].sort_values("MortalityRate", ascending=False)
    
    # 9. Recovery rate by Region (Recovered / Confirmed)
    def recovery_rate_by_region(self):
        print("Inside the question 9")
        grp = self.df.groupby("WHO Region")[["Confirmed","Recovered"]].sum()
        grp["RecoveryRate"] = grp["Recovered"] / grp["Confirmed"].replace(0, np.nan)
        return grp[["Confirmed","Recovered","RecoveryRate"]].sort_values("RecoveryRate", ascending=False)
    
    # 10. Detect outliers in Confirmed using mean ± 2*std (region-level or country-level)
    def detect_outliers(self, column="Confirmed", by="Country/Region"):
        values = self.df[[by, column]].copy()
        mu = values[column].mean()
        sigma = values[column].std()
        lower = mu - 2*sigma
        upper = mu + 2*sigma
        outliers = values[(values[column] < lower) | (values[column] > upper)].sort_values(column, ascending=False)
        return {"mean": mu, "std": sigma, "lower": lower, "upper": upper, "outliers": outliers}
    
    # 11. Group data by Country and Region
    def group_country_region(self):
        if "WHO Region" in self.df.columns:
            return self.df.groupby(["Country/Region","WHO Region"])[["Confirmed","Deaths","Recovered"]].sum()
        else:
            return self.df.groupby("Country/Region")[["Confirmed","Deaths","Recovered"]].sum()
    
    # 12. Regions with Zero Recovered Cases
    def regions_with_zero_recovered(self):
        grp = self.df.groupby("WHO Region")["Recovered"].sum()
        return grp[grp == 0]
    

# Subclass to implement export/save functionality (demonstrates inheritance)
class ExportableCovidAnalysis(CovidAnalysis):
    def save_sorted_csv(self, out_path="sorted_by_confirmed.csv"):
        df_sorted = self.sorted_by_confirmed()
        df_sorted.to_csv(out_path, index=False)
        return out_path
    
    def save_region_summary(self, out_path="summary_by_region.csv"):
        summary = self.summary_by_region().reset_index()
        summary.to_csv(out_path, index=False)
        return out_path

# Example usage
analysis = ExportableCovidAnalysis(CSV_PATH)

print("=== Summary by Region ===")
print(analysis.summary_by_region().head())

print("\n=== Filtered (confirmed >= 10) sample ===")
filtered = analysis.filter_low_cases(10)
print(filtered.shape)

print("\n=== Region with highest confirmed ===")
print(analysis.region_with_highest_confirmed())

print("\n=== Top 5 countries ===")
print(analysis.top_countries(5))

print("\n=== Region with lowest deaths ===")
print(analysis.region_with_lowest_deaths())

print("\n=== India summary ===")
print(analysis.country_summary("India"))

print("\n=== Mortality rate by region ===")
print(analysis.mortality_rate_by_region())

print("\n=== Recovery rate by region ===")
print(analysis.recovery_rate_by_region())

print("\n=== Outliers (Confirmed) ===")
out = analysis.detect_outliers()
print("mean, std", out["mean"], out["std"])
print("Outlier rows sample:")
print(out["outliers"].head())

print("\n=== Group country & region sample ===")
print(analysis.group_country_region().head())

print("\n=== Regions with zero recovered ===")
print(analysis.regions_with_zero_recovered())

# Save outputs as required
analysis.save_sorted_csv("sorted_by_confirmed.csv")
analysis.save_region_summary("summary_by_region.csv")
