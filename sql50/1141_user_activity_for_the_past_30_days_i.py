from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType, StringType
from datetime import date

spark = SparkSession.builder.getOrCreate()

activity_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("session_id", IntegerType(), False),
    StructField("activity_date", DateType(), False),
    StructField("activity_type", StringType(), False)
])

activity_data = [
    (1, 1, date(2019, 7, 20), "open_session"),
    (1, 1, date(2019, 7, 20), "scroll_down"),
    (1, 1, date(2019, 7, 20), "end_session"),
    (2, 4, date(2019, 7, 20), "open_session"),
    (2, 4, date(2019, 7, 21), "send_message"),
    (2, 4, date(2019, 7, 21), "end_session"),
    (3, 2, date(2019, 7, 21), "open_session"),
    (3, 2, date(2019, 7, 21), "send_message"),
    (3, 2, date(2019, 7, 21), "end_session"),
    (4, 3, date(2019, 6, 25), "open_session"),
    (4, 3, date(2019, 6, 25), "end_session")
]

activity = spark.createDataFrame(activity_data, activity_schema)
activity.show()

# solution
from pyspark.sql.functions import col, lit, date_sub, countDistinct
from datetime import date

result = (
    activity
        .filter(
            (col("activity_date") > date_sub(lit(date(2019, 7, 27)), 29))
            & (col("activity_date") <= lit(date(2019, 7, 27)))
        )
        .groupBy(col("activity_date").alias("day"))
        .agg(
            countDistinct(col("user_id")).alias("active_users")
        )
        .filter(col("active_users") > 0)
)
result.show()