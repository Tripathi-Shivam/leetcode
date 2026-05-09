from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("x", IntegerType(), False),
    StructField("y", IntegerType(), False),
    StructField("z", IntegerType(), False)
])

data = [
    (13, 15, 30),
    (10, 20, 15)
]

triangle_df = spark.createDataFrame(data, schema)
triangle_df.show()

# solution
from pyspark.sql.functions import col, when

result = (
    triangle_df
        .select(
            "*",
            when(
                (col("x") + col("y") > col("z"))
                & (col("x") + col("z") > col("y"))
                & (col("y") + col("z") > col("x")),
                "Yes"
            ).otherwise("No").alias("triangle")
        )
)
result.show()