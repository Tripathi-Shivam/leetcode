from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

prices_schema = StructType([
    StructField("product_id",  IntegerType(), False),
    StructField("start_date",  DateType(),    False),
    StructField("end_date",    DateType(),    False),
    StructField("price",       IntegerType(), False),
])

prices_data = [
    (1, date(2019, 2, 17), date(2019, 2, 28), 5),
    (1, date(2019, 3, 1),  date(2019, 3, 22), 20),
    (2, date(2019, 2, 1),  date(2019, 2, 20), 15),
    (2, date(2019, 2, 21), date(2019, 3, 31), 30),
]

prices = spark.createDataFrame(prices_data, prices_schema)

units_sold_schema = StructType([
    StructField("product_id",   IntegerType(), False),
    StructField("purchase_date",DateType(),    False),
    StructField("units",        IntegerType(), False),
])

units_sold_data = [
    (1, date(2019, 2, 25), 100),
    (1, date(2019, 3, 1),  15),
    (2, date(2019, 2, 10), 200),
    (2, date(2019, 3, 22), 30),
]

units_sold = spark.createDataFrame(units_sold_data, units_sold_schema)

prices.show()
units_sold.show()

# solution
from pyspark.sql.functions import col, sum, coalesce, lit, round

result = (
    prices
        .join(
            units_sold,
            on = 
                (prices.product_id == units_sold.product_id)
                & (units_sold.purchase_date.between(prices.start_date, prices.end_date)),
            how = "left"
        )
        .groupBy(prices.product_id)
        .agg(
            round(
                coalesce(
                    sum(prices.price * units_sold.units) / sum(units_sold.units),
                    lit(0)
                ),
            2).alias("average_price")
        )
)
result.show()