from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

visits_schema = StructType([
    StructField("visit_id",    IntegerType(), False),
    StructField("customer_id", IntegerType(), False),
])

visits_data = [
    (1, 23),
    (2, 9),
    (4, 30),
    (5, 54),
    (6, 96),
    (7, 54),
    (8, 54),
]

visits = spark.createDataFrame(visits_data, visits_schema)

transactions_schema = StructType([
    StructField("transaction_id", IntegerType(), False),
    StructField("visit_id",       IntegerType(), False),
    StructField("amount",         IntegerType(), False),
])

transactions_data = [
    (2, 5, 310),
    (3, 5, 300),
    (9, 5, 200),
    (12, 1, 910),
    (13, 2, 970),
]

transactions = spark.createDataFrame(transactions_data, transactions_schema)

visits.show()
transactions.show()

print("--- Solution #1 ---")
# region: solution
from pyspark.sql.functions import count

result = (
    visits
        .join(transactions, on = "visit_id", how = "left")
        .filter(transactions["transaction_id"].isNull())
        .groupBy(visits["customer_id"])
        .agg(count(visits["visit_id"]).alias("count_no_trans"))
)
result.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, count

result_df = (
    visits.alias("v")
        .join(
            transactions.alias("t"),
            on = "visit_id",
            how = "left_anti"
        )
        .groupBy("customer_id")
        .agg(count(col("v.visit_id")).alias("count_no_trans"))
)
result_df.show()

# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion