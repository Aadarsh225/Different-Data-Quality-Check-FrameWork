# Different Data Quality Check Frameworks

A comparison and implementation of multiple Python-based data quality validation frameworks on the same dataset. This project explores how different frameworks can be used to identify and validate common data quality issues such as missing values, duplicate records, invalid data types, and schema inconsistencies.

## Project Overview

Data quality is a critical aspect of data engineering, analytics, and machine learning workflows. This repository demonstrates the use of different data validation frameworks to perform automated quality checks on datasets.

The goal of this project is to:

* Compare multiple data quality frameworks
* Validate dataset integrity and consistency
* Detect missing values and duplicate records
* Enforce schema and data type validation
* Understand the strengths and limitations of each framework

## Frameworks Used

### 1. Great Expectations

A powerful data quality and validation framework that allows users to define expectations for datasets and generate validation reports.

### 2. Pandera

A dataframe validation library built for pandas that enables schema enforcement and statistical validation checks.

## Project Structure

```text
Different-Data-Quality-Check-FrameWork/
│
├── dataset.csv
├── gxdataquality.py
├── panderadataquality.py
├── README.md
```

## Data Quality Checks Performed

* Missing Value Detection
* Duplicate Record Detection
* Data Type Validation
* Schema Validation
* Dataset Profiling
* Constraint Validation

## Installation

Clone the repository:

```bash
git clone https://github.com/Aadarsh225/Different-Data-Quality-Check-FrameWork.git
cd Different-Data-Quality-Check-FrameWork
```

Install dependencies:

```bash
pip install pandas
pip install great-expectations
pip install pandera
```

## Running the Project

Run Great Expectations validation:

```bash
python gxdataquality.py
```

Run Pandera validation:

```bash
python panderadataquality.py
```

## Learning Outcomes

Through this project, I explored:

* Data quality fundamentals
* Schema validation techniques
* Automated data validation workflows
* Great Expectations framework
* Pandera framework
* Best practices for data validation in data engineering pipelines

## Future Improvements

* Add Cerberus validation examples
* Add PyDeequ implementation
* Generate automated validation reports
* Integrate with Databricks workflows
* Build a reusable data quality validation pipeline

## Author

**Aadarsh Kumar Singh**

GitHub: https://github.com/Aadarsh225
