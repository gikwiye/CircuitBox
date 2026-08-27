# CircuitBox
Databricks project for Lakeflow Spark Declarative Pipelines 
This project showcases how Lakeflow spark declarative pipeline (LSDP) is implemented.

Object:This project's objective is to showcase technical know how and LSDP latest development,
The project simulates a business demand for a DataMart that gathers Customer orders and address information.

In the code we used the following:

- Lakeflow Declarative Pipelines
- PySpark and Spark SQL
- Structured Streaming
- Auto Loader
- Delta Lake
- Medallion Architecture
- Data quality expectations
- SCD Type 1
- SCD Type 2
- Complex JSON parsing
- ARRAY / STRUCT processing


Sources:

The data source is stored in Azure Data Lake storage (ADLS) and is queried in Databricks via external location framework.
The architecture is described in Architecture.png




Transformations:

We respect the medallion architecture here.
Most of the transformations are done in script (Python OR SQL) using a silver prefix.
The reason we do this is because Databricks did not have the possibility to query different catalogs at the time.

we also used python and SQL to show both languages and how to use them to transform data. 
The silver (and bronze) tables are mostly streaming tables because we had daily data coming in the landing folders of ADLS. We wanted to incrementally load the data
and observe how this works.

We also added data quality rules to clean up the data when needed, or fail the pipeline if business rules were not respected.

You can see the table dependencies in LSDP_DAG.png.

Code FILE Structure:

CircuitBox_Pipeline
  - Address (python)
    
    - bronze_address.py
    - silver_address.py
    - silver_address_clean.py
      
  - Customer(SQL)
    
    - bronze_customers.sql
    - silver_customers_clean.sql
      
  - Order
    
    - bronze_order.py
    - silver_order.py
    - silver_order_clean.py
      
  - Summary (NOTEBOOK SQL)

    - gold_customer_summary.ipynb




