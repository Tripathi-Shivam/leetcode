from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("email", StringType(), False)
])

data = [
    (1, "john@example.com"),
    (2, "bob@example.com"),
    (3, "john@example.com")
]

person_df = spark.createDataFrame(data, schema)
person_df.show()

# solution
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("email")).orderBy(col("id").asc())

result_df = (
    person_df
        .withColumn("rnk", row_number().over(window_spec))
        .filter(col("rnk") == 1)
        .drop("rnk")
)
result_df.show()