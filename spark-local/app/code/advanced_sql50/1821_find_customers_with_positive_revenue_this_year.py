from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

customers_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("year", IntegerType(), False),
    StructField("revenue", IntegerType(), True)
])

customers_data = [
    (1, 2018, 50),
    (1, 2021, 30),
    (1, 2020, 70),
    (2, 2021, -10),
    (3, 2018, 20),
    (3, 2021, 40),
    (4, 2021, 0)
]

customers_df = spark.createDataFrame(customers_data, customers_schema)
customers_df.show(truncate=False)

# region: solution
from pyspark.sql.functions import col

result_df = (
    customers_df
        .filter(
            (col("revenue") > 0)
            & (col("year") == 2021)
        )
)
result_df.show()
# endregion

# command to execute: 
# docker exec -it spark-master /opt/spark/bin/spark-submit /opt/spark-app/code/advanced_sql50/1821_find_customers_with_positive_revenue_this_year.py

# region: practice

# endregion