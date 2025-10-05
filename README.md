# DC-Project_4 — Analyzing NYC Public School SAT Performance

**Author:** Completed independently by Ivan Shelest

**Based on DataCamp project:** [Exploring NYC Public School Test Result Scores](https://app.datacamp.com/learn/projects/exploring_nyc_public_school_test_result_scores/guided/Python)

---

## Project Description

New York City is home to some of the most competitive public high schools in the United States, where SAT performance often reflects both the academic standards of schools and socioeconomic disparities between neighborhoods.

In this project, SAT results from NYC public schools are analyzed to identify which schools perform best in math and overall, and which borough shows the greatest variation in test scores.

The analysis focuses on three key questions:

1. Which NYC schools have the best math results?
2. Which schools rank in the top 10 by total SAT score?
3. Which borough exhibits the largest variability (standard deviation) in SAT performance?

The project combines data manipulation and aggregation using **pandas** to summarize educational outcomes across schools and boroughs.

---

## Objectives

1. **Identify top-performing math schools** — schools where the average math score is at least 80% of the maximum possible SAT score (≥ 640).
2. **Rank schools by overall SAT performance** — sum of average math, reading, and writing scores.
3. **Find the borough with the largest SAT score variation** — based on standard deviation of total SAT scores among schools.

---

## Dataset

The dataset `schools.csv` contains information on New York City public high schools, including their average SAT section scores and borough classification.

| Column            | Description                            |
| ----------------- | -------------------------------------- |
| `school_name`     | Name of the high school                |
| `borough`         | Borough in which the school is located |
| `average_math`    | Average math SAT score                 |
| `average_reading` | Average reading SAT score              |
| `average_writing` | Average writing SAT score              |

---

## Methodology

1. **Data Import and Exploration:**
   Load the CSV file using pandas and inspect columns to verify data consistency.

2. **Math Performance Analysis:**
   Filter schools where `average_math ≥ 640` (80% of 800), sort by descending `average_math`, and store in `best_math_schools`.

3. **Overall SAT Ranking:**
   Create a new column `total_SAT` as the sum of math, reading, and writing scores.
   Select the top 10 schools with the highest combined scores and store in `top_10_schools`.

4. **Borough Variation Analysis:**
   Group data by borough to calculate:

   * `num_schools`: number of schools in each borough
   * `average_SAT`: mean of `total_SAT`
   * `std_SAT`: standard deviation of `total_SAT`
     Round results to two decimals and store the borough with the highest `std_SAT` in a DataFrame called `largest_std_dev`.

---

## Code Summary

```python
import pandas as pd

# Read data
schools = pd.read_csv("schools.csv")

# 1. Best math schools
best_math_schools = schools[schools["average_math"] >= 0.8 * 800][["school_name", "average_math"]]
best_math_schools = best_math_schools.sort_values(by="average_math", ascending=False)

# 2. Top 10 schools by combined SAT
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values(by="total_SAT", ascending=False).head(10)

# 3. Borough with largest SAT score variation
borough_stats = schools.groupby("borough").agg(
    num_schools=("school_name", "count"),
    average_SAT=("total_SAT", "mean"),
    std_SAT=("total_SAT", "std")
).reset_index()

borough_stats[["average_SAT", "std_SAT"]] = borough_stats[["average_SAT", "std_SAT"]].round(2)
largest_std_dev = borough_stats.loc[borough_stats["std_SAT"].idxmax(), ["borough", "num_schools", "average_SAT", "std_SAT"]]
largest_std_dev = pd.DataFrame(largest_std_dev).transpose()
```

---

## Results

### 1. Schools with the Best Math Results

| Rank | School Name                                                    | Average Math |
| ---- | -------------------------------------------------------------- | ------------ |
| 1    | Stuyvesant High School                                         | 754          |
| 2    | Bronx High School of Science                                   | 714          |
| 3    | Staten Island Technical High School                            | 711          |
| 4    | Queens High School for the Sciences at York College            | 701          |
| 5    | High School for Math, Science, and Engineering at City College | 683          |

---

### 2. Top 10 Schools by Total SAT Score

| Rank | School Name                                                           | Total SAT |
| ---- | --------------------------------------------------------------------- | --------- |
| 1    | Stuyvesant High School                                                | 2144      |
| 2    | Bronx High School of Science                                          | 2041      |
| 3    | Staten Island Technical High School                                   | 2041      |
| 4    | High School of American Studies at Lehman College                     | 2013      |
| 5    | Townsend Harris High School                                           | 1981      |
| 6    | Queens High School for the Sciences at York College                   | 1947      |
| 7    | Bard High School Early College                                        | 1914      |
| 8    | Brooklyn Technical High School                                        | 1896      |
| 9    | Eleanor Roosevelt High School                                         | 1889      |
| 10   | High School for Mathematics, Science, and Engineering at City College | 1889      |

---

### 3. Borough with the Largest Standard Deviation in SAT

| Borough   | Number of Schools | Average SAT | Std Dev |
| --------- | ----------------- | ----------- | ------- |
| Manhattan | 89                | 1340.13     | 230.29  |

---

## Interpretation

* The **top-performing schools** are specialized STEM-focused institutions, particularly **Stuyvesant**, **Bronx Science**, and **Staten Island Tech**.
* The **highest SAT averages** are concentrated in competitive Manhattan schools, but the same borough also exhibits the **largest score variation**, indicating significant disparities between top and lower-performing schools.
* These results illustrate the educational diversity within NYC and the concentration of elite academic institutions in Manhattan and the Bronx.

---

## Technologies Used

* Python 3.12
* pandas — data manipulation and aggregation
* VS Code — development environment

---

## Repository Structure

```
DC-Project_4/
│
├── main.py        # Analysis script
├── schools.csv    # Dataset of NYC public high school SAT results
└── README.md      # Project documentation
```

---

## Conclusion

This analysis of NYC public school SAT data highlights the strong performance of specialized science and math schools and underscores Manhattan’s dual character — home to both the city’s best and most variable educational outcomes.
The findings reinforce the role of advanced academic programs in shaping top SAT results across the city.