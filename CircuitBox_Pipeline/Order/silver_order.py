from pyspark import pipelines as dp

@dp.table(name="silver_order")
def create_silver_order():
    return(
        spark.readStream.table("LIVE.silver_order_clean")
        .select("customer_id",
                "order_id",
                "order_timestamp",
                "payment_method",
                "order_status",
                "item.item_id",
                "item.name",
                "item.price",
                "item.quantity",
                "item.category"
                )   
        )