from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(name = "silver_address_clean")
@dp.expect_or_fail("valid_customer_id","customer_id IS NOT NULL")
@dp.expect_or_drop("valid_address_line_1","address_line_1 IS NOT NULL")
@dp.expect("postcode","length(postcode) = 5")
def create_silver_address():
    return(
        spark.readStream.table("LIVE.bronze_address")
        .select(
            "customer_id",
            "address_line_1",
            "city",
            "state",
            "postcode",
            F.col("created_date").cast("date")
        )
    )