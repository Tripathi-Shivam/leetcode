from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("student_id", IntegerType(), False),
    StructField("course_id", IntegerType(), False),
    StructField("grade", IntegerType(), False),
])

data = [
    (2, 2, 95),
    (2, 3, 95),
    (1, 1, 90),
    (1, 2, 99),
    (3, 1, 80),
    (3, 2, 75),
    (3, 3, 82)
]

enrollments_df = spark.createDataFrame(data, schema)
enrollments_df.show()

# region: solution
print("--- Solution #1 ---")
from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("student_id")).orderBy(col("grade").desc(), col("course_id").asc())

result_df = (
    enrollments_df
        .withColumn("rnk", row_number().over(window_spec))
        .filter(col("rnk") == 1)
        .drop("rnk")
        .orderBy("student_id")
)
result_df.show()
# endregion

# region: practice
print("--- Practice ---")

# endregion