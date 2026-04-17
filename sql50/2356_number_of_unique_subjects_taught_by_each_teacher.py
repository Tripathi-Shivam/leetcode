from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()

teacher_schema = StructType([
    StructField("teacher_id", IntegerType(), False),
    StructField("subject_id", IntegerType(), False),
    StructField("dept_id", IntegerType(), False)
])

teacher_data = [
    (1, 2, 3),
    (1, 2, 4),
    (1, 3, 3),
    (2, 1, 1),
    (2, 2, 1),
    (2, 3, 1),
    (2, 4, 1),
]

teacher = spark.createDataFrame(teacher_data, teacher_schema)
teacher.show()

# solution
from pyspark.sql.functions import col, countDistinct

result = (
teacher
    .groupBy(col("teacher_id"))
    .agg(
        countDistinct(col("subject_id")).alias("cnt")
    )
)
result.show()