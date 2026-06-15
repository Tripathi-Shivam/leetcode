from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

weather_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("recordDate", DateType(), False),
    StructField("temperature", IntegerType(), False)
])

weather_data = [
    (1, date(2015, 1, 1), 10),
    (2, date(2015, 1, 2), 25),
    (3, date(2015, 1, 3), 20),
    (4, date(2015, 1, 4), 30),
]

df_weather = spark.createDataFrame(weather_data, weather_schema)
df_weather.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, datediff

w1 = df_weather.alias("w1")
w2 = df_weather.alias("w2")

result = (
    w1
        .join(
            w2, 
            on = datediff(col("w1.recordDate"), col("w2.recordDate")) == 1, 
            how = "inner"
        )
        .filter(col("w1.temperature") > col("w2.temperature"))
        .select(col("w1.id").alias("Id"))
)
result.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2 
from pyspark.sql.functions import col, lag, datediff
from pyspark.sql.window import Window

window_spec = Window.orderBy("recordDate")

result = (
    df_weather
        .withColumn("prev_temp", lag(col("temperature"), 1).over(window_spec))
        .withColumn("prev_date", lag(col("recordDate"), 1).over(window_spec))
        .filter(
            (col("temperature") > col("prev_temp"))
            & (datediff(col("recordDate"), col("prev_date")) == 1)
        )
        .select(col("id").alias("Id"))
)
result.show()
# endregion

print("--- Solution #3 ---")
# region: solution #3
from pyspark.sql.functions import col, date_sub

result_df = (
    df_weather.alias("weather_1")
        .join(
            df_weather.alias("weather_2"),
            on = col("weather_1.recordDate") == date_sub(col("weather_2.recordDate"), 1),
            how = "inner"
        )
        .filter(col("weather_2.temperature") > col("weather_1.temperature"))
        .select(col("weather_2.id"))
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion