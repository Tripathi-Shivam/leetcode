from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("delivery_id",                IntegerType(), False),
    StructField("customer_id",                IntegerType(), False),
    StructField("order_date",                 DateType(),    False),
    StructField("customer_pref_delivery_date", DateType(),   False),
])

data = [
    (1, 1, date(2019, 8, 1),  date(2019, 8, 2)),
    (2, 2, date(2019, 8, 2),  date(2019, 8, 2)),
    (3, 1, date(2019, 8, 11), date(2019, 8, 12)),
    (4, 3, date(2019, 8, 24), date(2019, 8, 24)),
    (5, 3, date(2019, 8, 21), date(2019, 8, 22)),
    (6, 2, date(2019, 8, 11), date(2019, 8, 13)),
    (7, 4, date(2019, 8, 9),  date(2019, 8, 9)),
]

delivery = spark.createDataFrame(data, schema)
delivery.show()

# solution
from pyspark.sql.functions import col, lit, round, sum, count, min, when
from pyspark.sql.window import Window

window_spec = Window.partitionBy(col("customer_id")).orderBy(col("order_date"))

result = (
    delivery
        .withColumn("first_order", min(col("order_date")).over(window_spec))
        .filter(col("order_date") == col("first_order"))
        .agg(
            round(
                (sum(when(col("order_date") == col("customer_pref_delivery_date"), lit(1)).otherwise(lit(0))) 
                /count(col("customer_id")))
                * 100,
            2).alias("immediate_percentage")
        )
)
result.show()