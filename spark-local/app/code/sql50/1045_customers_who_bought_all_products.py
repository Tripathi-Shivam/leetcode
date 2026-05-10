from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

customer_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("product_key", IntegerType(), False)
])

product_schema = StructType([
    StructField("product_key", IntegerType(), False)
])

customer_data = [
    (1, 5),
    (2, 6),
    (3, 5),
    (3, 6),
    (1, 6)
]

product_data = [
    (5,),
    (6,)
]

customer_df = spark.createDataFrame(customer_data, customer_schema)
product_df = spark.createDataFrame(product_data, product_schema)

# solution
from pyspark.sql.functions import countDistinct, col, lit

no_of_products = product_df.count()

result = (
    customer_df
        .groupBy("customer_id")
        .agg(countDistinct("product_key").alias("product_count"))
        .filter(col("product_count") == lit(no_of_products))
        .select("customer_id")
)
result.show()