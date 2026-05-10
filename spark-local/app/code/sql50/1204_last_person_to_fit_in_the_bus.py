from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("person_id", IntegerType(), False),
    StructField("person_name", StringType(), False),
    StructField("weight", IntegerType(), False),
    StructField("turn", IntegerType(), False)
])

data = [
    (5, "Alice", 250, 1),
    (4, "Bob", 175, 5),
    (3, "Alex", 350, 2),
    (6, "John Cena", 400, 3),
    (1, "Winston", 500, 6),
    (2, "Marie", 200, 4)
]

queue_df = spark.createDataFrame(data, schema)
queue_df.show()

# solution
from pyspark.sql.functions import col, sum
from pyspark.sql.window import Window

window_spec = Window.orderBy(col("turn").asc())


result_df = (
    queue_df
        .withColumn("running_total", sum(col("weight")).over(window_spec))
        .filter(col("running_total") <= 1000)
        .orderBy(col("turn").desc())
        .limit(1)
        .select("person_name")
)
result_df.show()