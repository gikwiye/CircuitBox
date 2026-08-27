from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(name = "bronze_order")
def create_bronze_order():
    return(
        spark.readStream
        .format("cloudfiles")
        .option("cloudFiles.format", "json")
        .option("cloudfiles.inferSchema", "true")
        .load("/Volumes/circuitbox/landing/operational_data/orders/")
        .select(
            "*",
            F.col("_metadata.file_path").alias("file_path"),
            F.current_timestamp().alias("ingest_ts")

        )
           )
