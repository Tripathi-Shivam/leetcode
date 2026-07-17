from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

tasks_schema = StructType([
    StructField("task_id", IntegerType(), False),
    StructField("subtasks_count", IntegerType(), False)
])

executed_schema = StructType([
    StructField("task_id", IntegerType(), False),
    StructField("subtask_id", IntegerType(), False)
])

tasks_data = [
    (1, 3),
    (2, 2),
    (3, 4)
]

executed_data = [
    (1, 2),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4)
]

tasks_df = spark.createDataFrame(
    tasks_data,
    tasks_schema
)

executed_df = spark.createDataFrame(
    executed_data,
    executed_schema
)

tasks_df.show()
executed_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, lit

expected_df = current_df = tasks_df

while True:
    next_df = (
        current_df
            .filter(col("subtasks_count") > lit(1))
            .select(col("task_id"), (col("subtasks_count") - lit(1)).alias("subtasks_count"))
    )

    if next_df.count() == 0:
        break

    expected_df = expected_df.unionAll(next_df)
    current_df = next_df

expected_df = expected_df.select("task_id", col("subtasks_count").alias("subtask_id"))
print("Look at the rows one-by-one, it'll help understand the flow:")
expected_df.show()

result_df = (
    expected_df.alias("t")
        .join(executed_df.alias("e"), on = ["task_id", "subtask_id"], how = "left_anti")
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col

numbers_df = (
    spark.range(1, 20)
        .withColumnRenamed("id", "subtask_id")
)

result_df = (
    tasks_df.alias("t")
        .join(numbers_df.alias("n"), on = col("t.subtasks_count") >= col("n.subtask_id"), how = "inner")
        .select("t.task_id", "n.subtask_id")
        .join(executed_df.alias("e"), on = ["task_id", "subtask_id"], how = "left_anti")
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion