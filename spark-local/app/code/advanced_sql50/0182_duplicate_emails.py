from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("email", StringType(), False)
])

data = [
    (1, "a@b.com"),
    (2, "c@b.com"),
    (3, "a@b.com")
]

person_df = spark.createDataFrame(data, schema)
person_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, count

result_df = (
    person_df
        .groupBy(col("email"))
        .agg(count(col("email")).alias("email_cnt"))
        .filter(col("email_cnt") > 1)
        .select("email")
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregio