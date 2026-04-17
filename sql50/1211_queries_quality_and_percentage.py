from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.getOrCreate()

queries_schema = StructType([
    StructField("query_name", StringType(), False),
    StructField("result", StringType(), False),
    StructField("position", IntegerType(), False),
    StructField("rating", IntegerType(), False)
])

queries_data = [
    ("Dog", "Golden Retriever", 1,   5),
    ("Dog", "German Shepherd",  2,   5),
    ("Dog", "Mule",             200, 1),
    ("Cat", "Shirazi",          5,   2),
    ("Cat", "Siamese",          3,   3),
    ("Cat", "Sphynx",           7,   4),
]

queries = spark.createDataFrame(queries_data, queries_schema)
queries.show()

# solution
from pyspark.sql.functions import col, lit, sum, count, when, round

result = (
    queries
        .groupBy("query_name")
        .agg(
            round(
                (sum(col("rating") / col("position"))) / count("query_name"),
            2).alias("quality"),
            round(
                (sum(when(col("rating") < 3, lit(1)).otherwise(lit(0))) / count(col("query_name")))
                * 100,
            2).alias("poor_query_percentage")
        )
)
result.show()