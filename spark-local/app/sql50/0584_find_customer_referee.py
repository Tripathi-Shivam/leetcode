# data prep
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("referee_id", IntegerType(), True),
])

data = [
    (1, "Will", None),
    (2, "Jane",   None),
    (3, "Alex",   2),
    (4, "Bill",   None),
    (5, "Zack",   1),
    (6, "Mark",   2),
]

df_customer = spark.createDataFrame(data, schema)
df_customer.show()

# solution
from pyspark.sql.functions import col

result = (
    df_customer
    .filter(
        (col("referee_id") != 2) | 
        (col("referee_id").isNull())
    )
    .select("name")
)
result.show()