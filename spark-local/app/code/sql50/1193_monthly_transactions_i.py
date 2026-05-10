from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("id",         IntegerType(), False),
    StructField("country",    StringType(),  False),
    StructField("state",      StringType(),  False),  # ENUM → StringType
    StructField("amount",     IntegerType(), False),
    StructField("trans_date", DateType(),    False),
])

data = [
    (121, "US",  "approved", 1000, date(2018, 12, 18)),
    (122, "US",  "declined", 2000, date(2018, 12, 19)),
    (123, "US",  "approved", 2000, date(2019, 1,  1)),
    (124, "DE",  "approved", 2000, date(2019, 1,  7)),
]

transactions = spark.createDataFrame(data, schema)
transactions.show()

# solution
from pyspark.sql.functions import col, date_format, count, sum, when, lit

result = (
    transactions
        .withColumn("month", date_format(col("trans_date"), "yyyy-MM"))
        .groupBy("month", "country")
        .agg(
            count(col("id")).alias("trans_count"),
            sum(when(col("state") == "approved", lit(1)).otherwise(lit(0))).alias("approved_count"),
            # using count
            # count(when(col("state") == "approved", lit(1)).otherwise(lit(None))).alias("approved_count"), 
            sum("amount").alias("trans_total_amount"),
            sum(when(col("state") == "approved", col("amount")).otherwise(lit(0))).alias("approved_total_amount")
        )
)
result.show()
