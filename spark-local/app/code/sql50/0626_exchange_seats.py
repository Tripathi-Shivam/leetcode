from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("student", StringType(), False)
])

data = [
    (1, "Abbot"),
    (2, "Doris"),
    (3, "Emerson"),
    (4, "Green"),
    (5, "Jeames")
]

seat_df = spark.createDataFrame(data, schema)
seat_df.show()

# region: solution
from pyspark.sql.functions import max, col, when, lit

max_id = seat_df.agg(max(col("id"))).collect()[0][0]

result_df = (
    seat_df
        .select(
            when(
                (col("id") % 2 == 1) & (col("id") == max_id),
                col("id")
            )
            .when(col("id") % 2 == 1, col("id") + 1)
            .otherwise(col("id") - 1)
            .alias("id"),
            col("student")
        )
        .orderBy("id")
)
result_df.show()
# endregion

# region: practice
print("--- Practice ---")
from pyspark.sql.functions import col, max, when, lit

max_id = seat_df.agg(max(col("id"))).collect()[0][0]

result_df = (
    seat_df
        .select(
            when((col("id") % 2 == 1) & (col("id") == lit(max_id)), col("id"))
            .otherwise(when(col("id") % 2 == 1, col("id") + lit(1)).otherwise(col("id") - lit(1)))
            .alias("id"),
            col("student")
        )
        .orderBy(col("id"))
)
result_df.show()
# endregion