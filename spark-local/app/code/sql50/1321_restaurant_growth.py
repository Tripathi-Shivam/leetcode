from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

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

print("--- Solution #1---")
# region: solution #1
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
# endregion

print("--- Practice #1---")
# region: last practice

from pyspark.sql.window import Window
from pyspark.sql.functions import col, sum, round, date_add, min, lit

window_spec = Window.orderBy(col("visited_on")).rowsBetween(-6, Window.currentRow)

min_date = customer_df.agg(min(col("visited_on"))).collect()[0][0]

result_df = (
    customer_df
        .groupBy("visited_on")
        .agg(sum(col("amount")).alias("amount_sum"))
        .withColumn("amount", sum(col("amount_sum")).over(window_spec))
        .filter(col("visited_on") >= lit(date_add(lit(min_date), 6)))
        .select(
            col("visited_on"),
            col("amount"),
            round(col("amount") / 7, 2).alias("average_amount")
        )
        .orderBy("visited_on")
)
result_df.show()
# endregion

print("--- Practice #2---")
# region: practice

# endregion