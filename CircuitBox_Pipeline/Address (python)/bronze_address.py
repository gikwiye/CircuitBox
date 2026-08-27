from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(name = "bronze_address")
def create_bronze_address():
  return (
    spark.readStream
    .format("cloudFiles") 
    .option("cloudFiles.format", "csv") 
    .option("cloudFiles.infercolumntypes", "true")
    .load("/Volumes/circuitbox/landing/operational_data/addresses/")
    .select(
        "*",
        F.col("_metadata.file_path").alias("file_path"),
        F.current_timestamp().alias("ingest_ts")
    ) 
    
    )