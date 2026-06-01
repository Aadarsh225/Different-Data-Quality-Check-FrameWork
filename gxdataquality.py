import pandas as pd
import great_expectations as gx

# Load dataset
df = pd.read_csv("dataset.csv")

# Create GX context
context = gx.get_context()

# Create datasource
datasource = context.data_sources.add_pandas(
    name="my_datasource"
)

# Create dataframe asset
asset = datasource.add_dataframe_asset(
    name="my_dataframe_asset"
)

# Create batch definition
batch_definition = asset.add_batch_definition_whole_dataframe(
    "my_batch_definition"
)

# Create expectation suite
suite = gx.ExpectationSuite(
    name="my_suite",
    expectations=[
        gx.expectations.ExpectColumnValuesToNotBeNull(
            column="id"
        ),

        gx.expectations.ExpectColumnValuesToBeUnique(
            column="id"
        ),

        gx.expectations.ExpectColumnValuesToBeBetween(
            column="age",
            min_value=18,
            max_value=100
        ),

        gx.expectations.ExpectColumnValuesToNotBeNull(
            column="email"
        ),

        gx.expectations.ExpectColumnValuesToMatchRegex(
            column="email",
            regex=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        ),

        gx.expectations.ExpectColumnValuesToBeBetween(
            column="salary",
            min_value=0,
            max_value=1000000
        ),

        gx.expectations.ExpectColumnValuesToBeInSet(
            column="city",
            value_set=[
                "Kathmandu",
                "Pokhara",
                "Lalitpur",
                "Biratnagar",
                "Butwal"
            ]
        ),

        gx.expectations.ExpectColumnValuesToMatchStrftimeFormat(
            column="join_date",
            strftime_format="%Y-%m-%d"
        )
    ]
)

# Register suite
try:
    context.suites.add(suite)
except Exception:
    pass

# Create validation definition
validation = gx.ValidationDefinition(
    name="my_validation",
    data=batch_definition,
    suite=suite
)

# Register validation definition
try:
    context.validation_definitions.add(validation)
except Exception:
    pass

# Run validation
results = validation.run(
    batch_parameters={
        "dataframe": df
    }
)

# Overall result
print("\n" + "=" * 70)
print("OVERALL VALIDATION STATUS")
print("=" * 70)
print("Validation Success:", results.success)

# Detailed results
print("\n" + "=" * 70)
print("DETAILED VALIDATION REPORT")
print("=" * 70)

for result in results.results:

    print("\n" + "-" * 70)

    expectation_name = result.expectation_config.type

    print("Expectation :", expectation_name)

    print("Passed      :", result.success)

    print(
        "Total Rows  :",
        result.result.get("element_count", "N/A")
    )

    print(
        "Failed Rows :",
        result.result.get("unexpected_count", 0)
    )

    bad_values = result.result.get(
        "partial_unexpected_list",
        []
    )

    print("Bad Values  :", bad_values)

    print("-" * 70)