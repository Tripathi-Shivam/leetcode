from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")  # only shows errors, not INFO/WARN

schema = StructType([
    StructField("sell_date", DateType(), False),
    StructField("product", StringType(), False)
])

data = [
    (date(2020,5,30), "Headphone"),
    (date(2020,6,1), "Pencil"),
    (date(2020,6,2), "Mask"),
    (date(2020,5,30), "Basketball"),
    (date(2020,6,1), "Bible"),
    (date(2020,6,2), "Mask"),
    (date(2020,5,30), "T-Shirt")
]

activities_df = spark.createDataFrame(data, schema)
activities_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, collect_set, size, sort_array, concat_ws

result_df = (
    activities_df
        .groupBy(col("sell_date"))
        .agg(
            size(collect_set(col("product"))).alias("num_sold"),
            concat_ws(",", sort_array(collect_set(col("product")))).alias("products")
        )
        .orderBy(col("sell_date"))
)
result_df.show(truncate = False)
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion