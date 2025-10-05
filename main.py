# Import libraries
import pandas as pd

# Read the data
schools = pd.read_csv("schools.csv")

# 1️ Schools with the best math results
best_math_schools = schools[schools["average_math"] >= 0.8 * 800][["school_name", "average_math"]]
best_math_schools = best_math_schools.sort_values(by="average_math", ascending=False)

# 2️ Top 10 schools by combined SAT score
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values(by="total_SAT", ascending=False).head(10)

# 3️ Borough with largest standard deviation of total SAT
borough_stats = schools.groupby("borough").agg(
    num_schools=("school_name", "count"),
    average_SAT=("total_SAT", "mean"),
    std_SAT=("total_SAT", "std")
).reset_index()

borough_stats[["average_SAT", "std_SAT"]] = borough_stats[["average_SAT", "std_SAT"]].round(2)

largest_std_dev = borough_stats.loc[borough_stats["std_SAT"].idxmax(), ["borough", "num_schools", "average_SAT", "std_SAT"]]
largest_std_dev = pd.DataFrame(largest_std_dev).transpose()

# Display results
print("Best math schools:")
print(best_math_schools.head(), "\n")

print("Top 10 schools by total SAT:")
print(top_10_schools, "\n")

print("Borough with largest standard deviation in total SAT:")
print(largest_std_dev)