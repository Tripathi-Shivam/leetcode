from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

users_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("name", StringType(), False)
])

users_data = [
    (1, "aLice"),
    (2, "bOB")
]

users_df = spark.createDataFrame(users_data, users_schema)
users_df.show()

# region: solution
from pyspark.sql.functions import col, concat, upper, lower, substr, lit

result_df = (
    users_df
        .select(
            col("user_id"),
            concat(
                upper(substr(col("name"), lit(1), lit(1))),
                lower(substr(col("name"), lit(2))),
            ).alias("name")
        )
        .orderBy("user_id")
)

result_df.show()
# endregion

# region: solution - using initcap()
from pyspark.sql.functions import col, initcap

resutl_df = (
    users_df
        .select(
            "user_id",
            # initcap("john DOE") → "John Doe"
            # capitalizes every word, not just first letter
            initcap(col("name")).alias("name")
        )
        .orderBy("user_id")
)
result_df.show()
# endregion

# region: practice
print("--- Practice ---")

# endregion