from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

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

# solution
from pyspark.sql.functions import count

result = (
    visits
        .join(transactions, on = "visit_id", how = "left")
        .filter(transactions["transaction_id"].isNull())
        .groupBy(visits["customer_id"])
        .agg(count(visits["visit_id"].alias("count_no_trans")))
        
)
result.show()