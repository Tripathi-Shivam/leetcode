from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

person_schema = StructType([
    StructField("personId", IntegerType(), False),
    StructField("lastName", StringType(), False),
    StructField("firstName", StringType(), False)
])

address_schema = StructType([
    StructField("addressId", IntegerType(), False),
    StructField("personId", IntegerType(), False),
    StructField("city", StringType(), False),
    StructField("state", StringType(), False)
])

person_data = [
    (1, "Wang", "Allen"),
    (2, "Alice", "Bob")
]

address_data = [
    (1, 2, "New York City", "New York")
]

person_df = spark.createDataFrame(person_data, person_schema)
address_df = spark.createDataFrame(address_data, address_schema)

person_df.show()
address_df.show()

print("--- Solution #1 ---")
# region: solution
from pyspark.sql.functions import col

result_df = (
    person_df.alias("p")
        .join(
            address_df.alias("a"),
            on = "personId",
            how = "left"
        )
        .select(col("p.firstName"), col("p.lastName"), col("a.city"), col("a.state"))
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion