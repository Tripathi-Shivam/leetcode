from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

delivery_schema = StructType([
    StructField("delivery_id", IntegerType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("order_date", DateType(), False),
    StructField("customer_pref_delivery_date", DateType(), False)
])

delivery_data = [
    (1, 1, date(2019, 8, 1), date(2019, 8, 2)),
    (2, 5, date(2019, 8, 2), date(2019, 8, 2)),
    (3, 1, date(2019, 8, 11), date(2019, 8, 12)),
    (4, 3, date(2019, 8, 24), date(2019, 8, 24)),
    (5, 4, date(2019, 8, 21), date(2019, 8, 22)),
    (6, 2, date(2019, 8, 11), date(2019, 8, 13))
]

delivery_df = spark.createDataFrame(delivery_data, delivery_schema)
delivery_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import col, avg, when, lit, round
result_df = (
    delivery_df
        .agg(
            round(
                100 *
                avg(
                    when(col("order_date") == col("customer_pref_delivery_date"), lit(1))
                    .otherwise(lit(0))
                )
            , 2).alias("immediate_percentage")
        )
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion