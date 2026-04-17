from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("sale_id", IntegerType(), False),
    StructField("product_id", IntegerType(), False),
    StructField("year", IntegerType(), False),
    StructField("quantity", IntegerType(), False),
    StructField("price", IntegerType(), False)
])

data = [
    (1, 100, 2008, 10, 5000),
    (2, 100, 2009, 12, 5000),
    (7, 200, 2011, 15, 9000)
]

sales_df = spark.createDataFrame(data, schema)
sales_df.show()

# solution
from pyspark.sql.functions import col, min
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("product_id")).orderBy(col("year").asc())

result = (
    sales_df
        .withColumn("first_year", min(col("year")).over(window_spec))
        .filter(col("year") == col("first_year"))
        .select(col("product_id"), col("first_year"), col("quantity"), col("price"))
)
result.show()