from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

request_accepted_schema = StructType([
    StructField("requester_id", IntegerType(), False),
    StructField("accepter_id", IntegerType(), False),
    StructField("accept_date", DateType(), False),
])

request_accepted_data = [
    (1, 2, date(2016, 6, 3)),
    (1, 3, date(2016, 6, 8)),
    (2, 3, date(2016, 6, 8)),
    (3, 4, date(2016, 6, 9)),
]

request_accepted_df = spark.createDataFrame(request_accepted_data, request_accepted_schema)
request_accepted_df.show()

# solution
from pyspark.sql.functions import col, count

result_df = (
    request_accepted_df
        .select(col("requester_id").alias("id"))
        .unionAll(
            request_accepted_df.select(col("accepter_id").alias("id"))
        )
        .groupBy("id")
        .agg(count(col("id")).alias("num"))
        .orderBy(col("num").desc())
        .limit(1)
)
result_df.show()