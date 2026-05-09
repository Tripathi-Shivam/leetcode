from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

products_schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("new_price", IntegerType(), False),
    StructField("change_date", DateType(), False),
])

products_data = [
    (1, 20, date(2019, 8, 14)),
    (2, 50, date(2019, 8, 14)),
    (1, 30, date(2019, 8, 15)),
    (1, 35, date(2019, 8, 16)),
    (2, 65, date(2019, 8, 17)),
    (3, 20, date(2019, 8, 18))
]

products_df = spark.createDataFrame(products_data, products_schema)
products_df.show()

# solution
from pyspark.sql.functions import col, lit, lead, date_sub, min
from pyspark.sql.window import Window
from datetime import date

window_spec = Window.partitionBy(col("product_id")).orderBy(col("change_date").asc())

filter_date = date(2019, 8, 16)

products_enhanced_df = (
    products_df
        .withColumn("end_date", date_sub(lead(col("change_date"), 1, date(2099, 12, 12)).over(window_spec), 1))
        .withColumn("first_change_date", min(col("change_date")).over(window_spec))
)

products_aftr_chng = (
    products_enhanced_df
        .filter(lit(filter_date).between(col("change_date"), col("end_date")))
        .select("product_id", col("new_price").alias("price"))
)

products_bfr_chng = (
    products_enhanced_df
        .filter(lit(filter_date) < col("first_change_date"))
        .select("product_id", lit(10).alias("price"))
)

result_df = (
    products_aftr_chng.union(products_bfr_chng)
)
result_df.show()