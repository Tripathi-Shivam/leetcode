from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType
)

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

daily_sales_schema = StructType([
    StructField("date_id", StringType(), False),
    StructField("make_name", StringType(), False),
    StructField("lead_id", IntegerType(), False),
    StructField("partner_id", IntegerType(), False)
])

daily_sales_data = [
    ("2020-12-8", "toyota", 0, 1),
    ("2020-12-8", "toyota", 1, 0),
    ("2020-12-8", "toyota", 1, 2),
    ("2020-12-7", "toyota", 0, 2),
    ("2020-12-7", "toyota", 0, 1),
    ("2020-12-8", "honda", 1, 2),
    ("2020-12-8", "honda", 2, 1),
    ("2020-12-7", "honda", 0, 1),
    ("2020-12-7", "honda", 1, 2),
    ("2020-12-7", "honda", 2, 1)
]

daily_sales_df = spark.createDataFrame(
    daily_sales_data,
    daily_sales_schema
)

daily_sales_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.functions import countDistinct

result_df = (
    daily_sales_df
        .groupBy("date_id", "make_name")
        .agg(
            countDistinct("lead_id").alias("unique_leads"),
            countDistinct("partner_id").alias("unique_partners"),
        )
)

result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion