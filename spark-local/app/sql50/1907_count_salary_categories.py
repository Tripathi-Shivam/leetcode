from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("account_id", IntegerType(), False),
    StructField("income", IntegerType(), False)
])

data = [
    (3, 108939),
    (2, 12747),
    (8, 87709),
    (6, 91796)
]

accounts_df = spark.createDataFrame(data, schema)
accounts_df.show()

# solution - using union
from pyspark.sql.functions import col, lit, count

low_df = (
    accounts_df
        .filter(col("income") < 20000)
        .agg(count(col("account_id")).alias("accounts_count"))
        .withColumn("category", lit("Low Salary"))
)

avg_df = (
    accounts_df
        .filter((col("income") >= 20000) & (col("income") <= 50000))
        .agg(count(col("account_id")).alias("accounts_count"))
        .withColumn("category", lit("Average Salary"))
)

high_df = (
    accounts_df
        .filter(col("income") > 50000)
        .agg(count(col("account_id")).alias("accounts_count"))
        .withColumn("category", lit("High Salary"))
)

low_df.show()
avg_df.show()
high_df.show()

result_df = (
    low_df
        .unionAll(avg_df)
        .unionAll(high_df)
)
result_df.show()

# solution - using stack
from pyspark.sql.functions import col, lit, when, sum

agg_df = (
    accounts_df
        .agg(
            sum(when(col("income") < 20000, lit(1)).otherwise(lit(0))).alias("low"),
            sum(when((col("income") >= 20000) & (col("income") <= 50000), lit(1)).otherwise(lit(0))).alias("avg"),
            sum(when(col("income") > 50000, lit(1)).otherwise(lit(0))).alias("high")
        )
)

result_df = agg_df.selectExpr("""
    stack(3,
        'Low Salary', low,
        'Average Salary', avg,
        'High Salary', high
    ) AS (category, average_count)
""")
result_df.show()