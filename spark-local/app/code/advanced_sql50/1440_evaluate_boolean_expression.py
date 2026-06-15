from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

variables_schema = StructType([
    StructField("name", StringType(), False),
    StructField("value", IntegerType(), False)
])

expressions_schema = StructType([
    StructField("left_operand", StringType(), False),
    StructField("operator", StringType(), False),
    StructField("right_operand", StringType(), False)
])

variables_data = [
    ("x", 66),
    ("y", 77)
]

expressions_data = [
    ("x", ">", "y"),
    ("x", "<", "y"),
    ("x", "=", "y")
]

variables_df = spark.createDataFrame(variables_data, variables_schema)
expressions_df = spark.createDataFrame(expressions_data, expressions_schema)

variables_df.show()
expressions_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, when

result_df = (
    expressions_df.alias("e")
        .join(
            variables_df.alias("v1"),
            on = col("e.left_operand") == col("v1.name"),
            how = "inner"
        )
        .join(
            variables_df.alias("v2"),
            on = col("e.right_operand") == col("v2.name"),
            how = "inner"
        )
        .select(
            col("e.*"),
            when(col("e.operator") == ">", col("v1.value") > col("v2.value"))
            .when(col("e.operator") == "<", col("v1.value") < col("v2.value"))
            .when(col("e.operator") == "=", col("v1.value") == col("v2.value"))
            .alias("value")
        )
)
result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, when

is_true_condition = (
    ((col("e.operator") == ">") & (col("v1.value") > col("v2.value"))) |
    ((col("e.operator") == "<") & (col("v1.value") < col("v2.value"))) |
    ((col("e.operator") == "=") & (col("v1.value") == col("v2.value")))
)

result_df = (
    expressions_df.alias("e")
        .join(
            variables_df.alias("v1"),
            on = col("e.left_operand") == col("v1.name"),
            how = "inner"
        )
        .join(
            variables_df.alias("v2"),
            on = col("e.right_operand") == col("v2.name"),
            how = "inner"
        )
        .select(
            col("e.*"),
            when(is_true_condition, True).otherwise(False).alias("value")
        )
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice

# endregion