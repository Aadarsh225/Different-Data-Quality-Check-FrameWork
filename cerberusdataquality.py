import pandas as pd
from cerberus import Validator

# Load dataset
df = pd.read_csv("dataset.csv")

# Convert numeric columns
df["id"] = pd.to_numeric(
    df["id"],
    errors="coerce"
)

df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)

df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)

# Cerberus Schema
schema = {

    "id": {
        "type": "float",
        "required": True,
        "min": 1,
    },

    "age": {
        "type": "float",
        "required": True,
        "min": 18,
        "max": 100,
    },

    "email": {
        "type": "string",
        "required": True,
        "regex": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    },

    "salary": {
        "type": "float",
        "required": True,
        "min": 0,
        "max": 1000000,
    },

    "city": {
        "type": "string",
        "required": True,
        "allowed": [
            "Kathmandu",
            "Pokhara",
            "Lalitpur",
            "Biratnagar",
            "Butwal"
        ]
    },

    "join_date": {
        "type": "string",
        "required": True,
        "regex": r"^\d{4}-\d{2}-\d{2}$"
    }
}

# Create validator
validator = Validator(schema)

# Store all failures
all_failures = []

# Validate each row
for index, row in df.iterrows():

    record = row.to_dict()

    if not validator.validate(record):

        for column, errors in validator.errors.items():

            all_failures.append(
                {
                    "row": index + 1,
                    "column": column,
                    "value": record.get(column),
                    "error": ", ".join(errors)
                }
            )

# Overall Status
print("\n" + "=" * 70)
print("OVERALL VALIDATION STATUS")
print("=" * 70)

if len(all_failures) == 0:

    print("Validation Success: True")

else:

    print("Validation Success: False")

    print("\n" + "=" * 70)
    print("DETAILED VALIDATION REPORT")
    print("=" * 70)

    failure_df = pd.DataFrame(all_failures)

    for column in failure_df["column"].unique():

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

        print(
            "Bad Values  :",
            column_failures["value"]
            .drop_duplicates()
            .tolist()
        )

        print(
            "Errors      :",
            column_failures["error"]
            .unique()
            .tolist()
        )

        print("-" * 70)

    print("\n" + "=" * 70)
    print("FULL FAILURE DETAILS")
    print("=" * 70)

    print(
        failure_df[
            [
                "row",
                "column",
                "value",
                "error"
            ]
        ]
    )