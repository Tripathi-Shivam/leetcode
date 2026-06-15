from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

users_schema = StructType([
    StructField("account", IntegerType(), False),
    StructField("name", StringType(), False)
])

transactions_schema = StructType([
    StructField("trans_id", IntegerType(), False),
    StructField("account", IntegerType(), False),
    StructField("amount", IntegerType(), False)
])

users_data = [
    (900001, "Alice"),
    (900002, "Bob"),
    (900003, "Charlie")
]

transactions_data = [
    (1, 900001, 7000),
    (2, 900001, 7000),
    (3, 900001, -3000),
    (4, 900002, 1000),
    (5, 900003, 6000),
    (6, 900003, 6000),
    (6, 900003, -4000)
]

users_df = spark.createDataFrame(users_data, users_schema)
users_df.show()

transactions_df = spark.createDataFrame(transactions_data, transactions_schema)
transactions_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, sum
result_df = (
    transactions_df.alias("t")
        .join(
            users_df.alias("u"),
            on = "account",
            how = "inner"
        )
        .groupBy(col("u.account"), col("u.name"))
        .agg(
            sum(col("amount")).alias("balance")
        )
        .filter(col("balance") > 10000)
        .select("name", "balance")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregio