from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(name="silver_order_clean")
@dp.expect_or_fail("valid_customer_id","customer_id IS NOT NULL")
@dp.expect_or_fail("valid_order_id","order_id IS NOT NULL")
@dp.expect("valid_order_status","order_status IN ('Pending','Shipped','Cancelled','Completed')")
@dp.expect("Valid_payment_method","payment_method IN ('Credit Card','PayPal','Bank Transfer')")
def create_silver_order_clean():
 
    return(
        spark.readStream.table("LIVE.bronze_order").select(
            "customer_id",
            "order_id",
            "order_status",
            "payment_method",
            F.explode(F.from_json(F.col("items"),
                        "ARRAY<STRUCT<category: STRING, item_id: BIGINT, name: STRING, price: BIGINT, quantity: BIGINT>>" )).alias("item"),
            "file_path",
            "ingest_ts",
            F.col("order_timestamp").cast("timestamp").alias("order_timestamp"))
    )
