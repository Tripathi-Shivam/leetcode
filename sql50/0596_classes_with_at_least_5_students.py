from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("student", StringType(), False),
    StructField("class", StringType(), False)
])

data = [
    ("A", "Math"),
    ("B", "English"),
    ("C", "Math"),
    ("D", "Biology"),
    ("E", "Math"),
    ("F", "Computer"),
    ("G", "Math"),
    ("H", "Math"),
    ("I", "Math")
]

courses_df = spark.createDataFrame(data, schema)
courses_df.show()

# solution
from pyspark.sql.functions import col, count

result = (
    courses_df
        .groupBy(col("class"))
        .agg(count(col("student")).alias("student_count"))
        .filter(col("student_count") >= 5)
        .select("class")
)
result.show()