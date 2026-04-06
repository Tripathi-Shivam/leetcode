from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

spark = SparkSession.builder.getOrCreate()

activity_schema = StructType([
    StructField("machine_id", IntegerType(), False),
    StructField("process_id", IntegerType(), False),
    StructField("activity_type", StringType(), False),
    StructField("timestamp", DoubleType(), False)
])

activity_data = [
    (0, 0, "start", 0.712),
    (0, 0, "end",   1.520),
    (0, 1, "start", 3.140),
    (0, 1, "end",   4.120),
    (1, 0, "start", 0.550),
    (1, 0, "end",   1.550),
    (1, 1, "start", 0.430),
    (1, 1, "end",   1.420),
    (2, 0, "start", 4.100),
    (2, 0, "end",   4.512),
    (2, 1, "start", 2.500),
    (2, 1, "end",   5.000),
]

activity = spark.createDataFrame(activity_data, activity_schema)
activity.show()

# solution
from pyspark.sql.functions import col, avg, round

a1 = activity.alias("a1")
a2 = activity.alias("a2")

result = (
    a1
        .join(
                a2, 
                on = 
                    (col("a1.machine_id") == col("a2.machine_id"))
                    & (col("a1.process_id") == col("a2.process_id"))
                    & (col("a1.activity_type") == "start")
                    & (col("a2.activity_type") == "end"),
                how = "inner"
            )
        .groupBy(col("a1.machine_id").alias("machine_id"))
        .agg(round(avg(col("a2.timestamp") - col("a1.timestamp")), 3).alias("processing_time"))
)
result.show()

# conditional aggregation
from pyspark.sql.functions import col, avg, round, when

result = (
    activity
        .groupBy("machine_id")
        .agg(
            round(
                avg(when(col("activity_type") == "end", col("timestamp"))) -
                avg(when(col("activity_type") == "start", col("timestamp"))), 
            3).alias("processing_time")
        )
)
result.show()