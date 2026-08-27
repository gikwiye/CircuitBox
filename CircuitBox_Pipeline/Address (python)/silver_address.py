from pyspark import pipelines as dp

dp.create_streaming_table(
    name = "silver_address",
    comment = 'SCD TYPE 2 table'
)

dp.apply_changes(
    source  = "silver_address_clean",
    target = "silver_address",
    keys=["customer_id"],
    sequence_by = "created_date",
    stored_as_scd_type= 2
)