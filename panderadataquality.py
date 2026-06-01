import pandas as pd
import pandera.pandas as pa
from pandera.pandas import Column, DataFrameSchema, Check

# Load dataset
df = pd.read_csv("dataset.csv")

# Create Schema
schema = DataFrameSchema(
    {

        "id": Column(
            float,
            nullable=False,
            unique=True,
            checks=[
                Check.greater_than(0)
            ]
        ),

        "age": Column(
            object,
            nullable=False,
            checks=[
                Check.in_range(
                    min_value=18,
                    max_value=100
                )
            ]
        ),

        "email": Column(
            object,
            nullable=False,
            checks=[
                Check.str_matches(
                    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
                )
            ]
        ),

        "salary": Column(
            object,
            nullable=False,
            checks=[
                Check.in_range(
                    min_value=0,
                    max_value=1000000
                )
            ]
        ),

        "city": Column(
            object,
            nullable=False,
            checks=[
                Check.isin(
                    [
                        "Kathmandu",
                        "Pokhara",
                        "Lalitpur",
                        "Biratnagar",
                        "Butwal"
                    ]
                )
            ]
        ),

        "join_date": Column(
            object,
            nullable=False,
            checks=[
                Check.str_matches(
                    r"^\d{4}-\d{2}-\d{2}$"
                )
            ]
        )
    },

    strict=False,
    coerce=False
)

# Run Validation
try:

    schema.validate(
        df,
        lazy=True
    )

    print("\n" + "=" * 70)
    print("OVERALL VALIDATION STATUS")
    print("=" * 70)

    print("Validation Success: True")

except pa.errors.SchemaErrors as e:

    print("\n" + "=" * 70)
    print("OVERALL VALIDATION STATUS")
    print("=" * 70)

    print("Validation Success: False")

    print("\n" + "=" * 70)
    print("DETAILED VALIDATION REPORT")
    print("=" * 70)

    failure_df = e.failure_cases

    for column in failure_df["column"].dropna().unique():

        column_failures = failure_df[
            failure_df["column"] == column
        ]

        print("\n" + "-" * 70)

        print(
            "Column      :",
            column
        )

        print(
            "Failed Rows :",
            len(column_failures)
        )

        bad_values = (
            column_failures["failure_case"]
            .drop_duplicates()
            .tolist()
        )

        print(
            "Bad Values  :",
            bad_values
        )

        print("-" * 70)

    print("\n" + "=" * 70)
    print("FULL FAILURE DETAILS")
    print("=" * 70)

    print(
        failure_df[
            [
                "column",
                "failure_case",
                "check"
            ]
        ]
    )