from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

sales_schema = StructType([
    StructField("sale_id", IntegerType(), False),
    StructField("product_id", IntegerType(), False),
    StructField("year", IntegerType(), False),
    StructField("quantity", IntegerType(), False),
    StructField("price", IntegerType(), False)
])

sales_data = [
    (1, 100, 2008, 10, 5000),
    (2, 100, 2009, 12, 5000),
    (7, 200, 2011, 15, 9000)
]

df_sales = spark.createDataFrame(sales_data, sales_schema)

product_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("product_name", StringType(), False)
])

product_data = [
    (100, "Nokia"),
    (200, "Apple"),
    (300, "Samsung")
]

df_product = spark.createDataFrame(product_data, product_schema)


df_sales.show()
df_product.show()

# solution
result = (
    df_sales
        .join(df_product, on = df_sales["product_id"] == df_product["product_id"], how = "inner")
        .select(df_product["product_name"], df_sales["year"], df_sales["price"])
)
result.show()