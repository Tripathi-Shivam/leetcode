from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, DateType, StringType, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

sales_schema = StructType([
    StructField("sale_date", DateType(), False),
    StructField("fruit", StringType(), False),
    StructField("sold_num", IntegerType(), False)
])

sales_data = [
    (date(2020, 5, 1), "apples", 10),
    (date(2020, 5, 1), "oranges", 8),
    (date(2020, 5, 2), "apples", 15),
    (date(2020, 5, 2), "oranges", 15),
    (date(2020, 5, 3), "apples", 20),
    (date(2020, 5, 3), "oranges", 0),
    (date(2020, 5, 4), "apples", 15),
    (date(2020, 5, 4), "oranges", 16)
]

sales_df = spark.createDataFrame(sales_data, sales_schema)
sales_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, when, sum as spark_sum

result_df = (
    sales_df
        .groupBy("sale_date")
        .agg(
            spark_sum(
                when(col("fruit") == "apples", col("sold_num"))
                .when(col("fruit") == "oranges", col("sold_num") * -1)
            ).alias("diff")
        )
        .orderBy("sale_date")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion