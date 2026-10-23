
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read the dataset
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race?
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df.loc[df["sex"] == "Male", "age"].mean(), 1
    )

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. People with advanced education earning >50K
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )
    lower_education = ~higher_education

    higher_education_rich = round(
        (
            (df["salary"] == ">50K") & higher_education
        ).sum()
        / higher_education.sum()
        * 100,
        1
    )

    # 5. People without advanced education earning >50K
    lower_education_rich = round(
        (
            (df["salary"] == ">50K") & lower_education
        ).sum()
        / lower_education.sum()
        * 100,
        1
    )

    # 6. Minimum number of hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people working minimum hours who earn >50K
    min_workers = df[df["hours-per-week"] == min_work_hours]

    num_min_workers = (
        (min_workers["salary"] == ">50K").sum()
    )

    rich_percentage = round(
        num_min_workers / len(min_workers) * 100, 1
    )

    # 8. Country with the highest percentage earning >50K
    country_earnings = df.groupby("native-country")["salary"].apply(
        lambda salaries: (salaries == ">50K").mean() * 100
    )

    highest_earning_country = country_earnings.idxmax()
    highest_earning_country_percentage = round(
        country_earnings.max(), 1
    )

    # 9. Most popular occupation for people in India earning >50K
    india_rich = df[
        (df["native-country"] == "India")
        & (df["salary"] == ">50K")
    ]

    top_IN_occupation = india_rich["occupation"].mode()[0]

    # Print results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(
            "Percentage with Bachelor's degrees:",
            percentage_bachelors
        )
        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich
        )
        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich
        )
        print("Minimum work hours:", min_work_hours)
        print(
            "Percentage of minimum-hour workers earning >50K:",
            rich_percentage
        )
        print("Country with highest percentage earning >50K:",
              highest_earning_country)
        print("Percentage:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
