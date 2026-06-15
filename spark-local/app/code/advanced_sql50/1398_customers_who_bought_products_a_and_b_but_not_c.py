from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

customers_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("customer_name", StringType(), False)
])

orders_schema = StructType([
    StructField("order_id", IntegerType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("product_name", StringType(), False)
])

customers_data = [
    (1, "Daniel"),
    (2, "Diana"),
    (3, "Elizabeth"),
    (4, "Jhon")
]

orders_data = [
    (10, 1, "A"),
    (20, 1, "B"),
    (30, 1, "D"),
    (40, 1, "C"),
    (50, 2, "A"),
    (60, 3, "A"),
    (70, 3, "B"),
    (80, 3, "D"),
    (90, 4, "C")
]

customers_df = spark.createDataFrame(customers_data, customers_schema)
orders_df = spark.createDataFrame(orders_data, orders_schema)

customers_df.show()
orders_df.show()

# region: solution #1
print("--- Solution #1 ---")
from pyspark.sql.functions import col, collect_set, sort_array, concat_ws

result_df = (
    orders_df.alias("o")
        .join(
            customers_df.alias("c"),
            on = "customer_id",
            how = "inner"
        )
        .groupBy(col("o.customer_id"), col("c.customer_name"))
        .agg(
            concat_ws("", sort_array(collect_set(col("o.product_name")))).alias("products")
        )
        .filter(col("products").rlike("(^AB)($|[^C])"))
        .select("customer_id", "customer_name")
        .orderBy("customer_id")
)
result_df.show()
# endregion

# region: solution #2
print("--- Solution #2 ---")
from pyspark.sql.functions import col, sum, when

result_df = (
    orders_df.alias("o")
        .join(
            customers_df.alias("c"),
            on = "customer_id",
            how = "inner"
        )
        .groupBy(col("o.customer_id"), col("c.customer_name"))
        .agg(
            sum(when(col("o.product_name") == 'A', 1).otherwise(0)).alias("a_count"),
            sum(when(col("o.product_name") == 'B', 1).otherwise(0)).alias("b_count"),
            sum(when(col("o.product_name") == 'C', 1).otherwise(0)).alias("c_count")
        )
        .filter(
            (col("a_count") > 0)
            & (col("b_count") > 0)
            & (col("c_count") == 0)
        )
        .select("o.customer_id", "c.customer_name")
        .orderBy("o.customer_id")
)
result_df.show()
# endregion

# region: practice
print("--- Practice ---")

# endregion