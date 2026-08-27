# CircuitBox

CircuitBox is a Databricks data engineering project demonstrating the implementation of **Lakeflow Spark Declarative Pipelines (LSDP)**.

## Objective

The project simulates a business requirement to build a customer-order Data Mart combining:

- Customer information
- Customer addresses
- Orders
- Order items

The main objective is to demonstrate practical knowledge of modern Databricks data engineering patterns and recent Lakeflow Declarative Pipelines capabilities.

## Technologies and Concepts

The project demonstrates:

- Lakeflow Declarative Pipelines
- PySpark
- Spark SQL
- Structured Streaming
- Auto Loader
- Delta Lake
- Medallion Architecture
- Data quality expectations
- SCD Type 1
- SCD Type 2
- Complex JSON parsing
- ARRAY and STRUCT processing
- Azure Data Lake Storage
- Databricks External Locations

## Architecture

Source data is stored in **Azure Data Lake Storage (ADLS)** and accessed from Databricks through external locations.

The project follows the Medallion Architecture:

ADLS  
↓  
Bronze  
↓  
Silver  
↓  
Gold / Data Mart

The detailed architecture is available in `Architecture.png`.

## Data Ingestion

Most Bronze tables are implemented as streaming tables.

New source files are delivered periodically to landing folders in ADLS. Auto Loader and Structured Streaming are used to incrementally process newly arriving data rather than repeatedly processing the entire dataset.

This demonstrates how Databricks handles incremental file ingestion and streaming workloads.

## Transformations

The Silver layer contains most of the transformation and data-cleaning logic.

Both **PySpark and Spark SQL** are deliberately used throughout the project to demonstrate how equivalent Lakeflow transformations can be implemented using either language.

Transformations include:

- Data type conversions
- Data-quality validation
- JSON parsing
- ARRAY and STRUCT processing
- Flattening nested order items
- SCD Type 1 processing
- SCD Type 2 historization

## Data Quality

Lakeflow expectations are used to enforce business and data-quality rules.

Depending on the rule, invalid records can either:

- be retained while recording a quality violation,
- be dropped,
- or cause the pipeline update to fail.

Examples include validation of:

- Customer IDs
- Order IDs
- Order statuses
- Payment methods
- Required address information

## Slowly Changing Dimensions

The project demonstrates both:

### SCD Type 1

Used when only the latest version of a record needs to be retained.

### SCD Type 2

Used when historical changes need to be preserved.

For example, customer address changes can be historized so that previous addresses remain available for historical analysis.

## Pipeline Dependencies

Lakeflow automatically manages dependencies between pipeline datasets.

The generated pipeline DAG can be viewed in:

LSDP_DAG.png

## Project Structure


CircuitBox_Pipeline/
│
├── Address (Python)/
│   ├── bronze_address.py
│   ├── silver_address.py
│   └── silver_address_clean.py
│
├── Customer (SQL)/
│   ├── bronze_customers.sql
│   └── silver_customers_clean.sql
│
├── Order/
│   ├── bronze_order.py
│   ├── silver_order.py
│   └── silver_order_clean.py
│
└── Summary (SQL Notebook)/
    └── gold_customer_summary.ipynb



