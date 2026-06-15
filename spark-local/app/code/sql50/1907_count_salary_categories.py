from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

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

print("--- Solution #1 ---")
# region: solution - using union
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

# low_df.show()
# avg_df.show()
# high_df.show()

result_df = (
    low_df
        .unionAll(avg_df)
        .unionAll(high_df)
        .select("category", "accounts_count")
)
result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2 - using stack
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
    ) AS (category, accounts_count)
""")
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion