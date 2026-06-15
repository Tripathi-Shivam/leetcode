from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

tree_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("p_id", IntegerType(), True)
])

tree_data = [
    (1, None),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2)
]

tree_df = spark.createDataFrame(
    tree_data,
    tree_schema
)

tree_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, when, lit

parent_nodes_df = (
    tree_df
        .filter(col("p_id").isNotNull())
        .select(col("p_id").alias("parent_id"))
        .distinct()
)

result_df = (
    tree_df.alias("t")
        .join(parent_nodes_df.alias("p"), on = col("t.id") == col("p.parent_id"), how = "left") # trying to find child nodes
        .select(
            col("t.id"),
            when(col("t.p_id").isNull(), lit("Root"))
                .when(col("p.parent_id").isNull(), lit("Leaf"))
                .otherwise(lit("Inner"))
                .alias("type")
        )
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion