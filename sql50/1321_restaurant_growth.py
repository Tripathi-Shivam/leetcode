from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("visited_on", DateType(), False),
    StructField("amount", IntegerType(), False)
])

data = [
    (1, "Jhon", date(2019, 1, 1), 100),
    (2, "Daniel", date(2019, 1, 2), 110),
    (3, "Jade", date(2019, 1, 3), 120),
    (4, "Khaled", date(2019, 1, 4), 130),
    (5, "Winston", date(2019, 1, 5), 110),
    (6, "Elvis", date(2019, 1, 6), 140),
    (7, "Anna", date(2019, 1, 7), 150),
    (8, "Maria", date(2019, 1, 8), 80)
]

customer_df = spark.createDataFrame(data, schema)
customer_df.show()

# solution
from pyspark.sql.window import Window
from pyspark.sql.functions import col, sum, round, row_number

window_spec = Window.orderBy(col("visited_on").asc()).rowsBetween(-6, Window.currentRow)

daily_sales_df = (
    customer_df
        .groupBy("visited_on")
        .agg(sum(col("amount")).alias("daily_amount"))
)

result_df = (
daily_sales_df
    .withColumn("amount", sum(col("daily_amount")).over(window_spec))
    .withColumn("average_amount", round(col("amount") / 7, 2))
    .withColumn("rnk", row_number().over(Window.orderBy("visited_on")))
    .filter(col("rnk") >= 7)
    .select("visited_on", "amount", "average_amount")
    .orderBy("visited_on")
)
result_df.show()