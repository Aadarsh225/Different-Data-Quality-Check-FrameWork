import pandas as pd
import great_expectations as gx

df = pd.read_csv("dirtydata.csv")

## Creating Data Context
context = gx.get_context()

## Creating Datasource
datasource = context.data_sources.add_pandas(
    name="cafe_datasource"
)

## Creating Data Asset
asset = datasource.add_dataframe_asset(
    name="cafe_asset"
)

## Creating Batch Defination
batch_definition = asset.add_batch_definition_whole_dataframe(
    name="cafe_batch_definition"
)

## Creating Expectation Suite
suite = gx.ExpectationSuite(
    name="cafe_suite",
    expectations=[
    gx.expectations.ExpectColumnValuesToNotBeNull(
            column="Transaction ID"
        ),

        gx.expectations.ExpectColumnValuesToBeUnique(
            column="Transaction ID"
        ),

        gx.expectations.ExpectColumnValuesToNotBeNull(
            column="Item"
        ),

        gx.expectations.ExpectColumnValuesToBeInSet(
            column="Item",
            value_set=[
                "Coffee",
                "Tea",
                "Cake",
                "Cookie",
                "Juice",
                "Smoothie",
                "Sandwich",
                "Salad"
            ]
        ),

        gx.expectations.ExpectColumnValuesToBeBetween(
            column="Quantity",
            min_value=1,
            max_value=5
        ),

        gx.expectations.ExpectColumnValuesToBeBetween(
            column="Price Per Unit",
            min_value=0
        ),

        gx.expectations.ExpectColumnValuesToBeBetween(
            column="Total Spent",
            min_value=0
        ),

        gx.expectations.ExpectColumnValuesToBeInSet(
            column="Payment Method",
            value_set=[
                "Cash",
                "Credit Card",
                "Digital Wallet"
            ]
        ),

        gx.expectations.ExpectColumnValuesToBeInSet(
            column="Location",
            value_set=[
                "In-store",
                "Takeaway"
            ]
        ),

        gx.expectations.ExpectColumnValuesToMatchStrftimeFormat(
            column="Transaction Date",
            strftime_format="%Y-%m-%d"
        )
    ]
)

## Register suite
try:
    context.suites.add(suite)
except Exception:
    pass

## Create validation defination
validation = gx.ValidationDefinition(
    name="cafe_validation",
    data=batch_definition,
    suite=suite
)

## Register validation definition
try:
    context.validation_definitions.add(validation)
except Exception:
    pass

## Run Validation
results = validation.run(
    batch_parameters={
        "dataframe":df
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
