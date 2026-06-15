from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

sales_person_schema = StructType([
    StructField("sales_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("salary", IntegerType(), False),
    StructField("commission_rate", IntegerType(), False),
    StructField("hire_date", DateType(), False)
])

company_schema = StructType([
    StructField("com_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("city", StringType(), False)
])

orders_schema = StructType([
    StructField("order_id", IntegerType(), False),
    StructField("order_date", DateType(), False),
    StructField("com_id", IntegerType(), False),
    StructField("sales_id", IntegerType(), False),
    StructField("amount", IntegerType(), False)
])

sales_person_data = [
    (1, "John", 100000, 6, date(2006, 4, 1)),
    (2, "Amy", 12000, 5, date(2010, 5, 1)),
    (3, "Mark", 65000, 12, date(2008, 12, 25)),
    (4, "Pam", 25000, 25, date(2005, 1, 1)),
    (5, "Alex", 5000, 10, date(2007, 2, 3))
]

company_data = [
    (1, "RED", "Boston"),
    (2, "ORANGE", "New York"),
    (3, "YELLOW", "Boston"),
    (4, "GREEN", "Austin")
]

orders_data = [
    (1, date(2014, 1, 1), 3, 4, 10000),
    (2, date(2014, 2, 1), 4, 5, 5000),
    (3, date(2014, 3, 1), 1, 1, 50000),
    (4, date(2014, 4, 1), 1, 4, 25000)
]

sales_person_df = spark.createDataFrame(sales_person_data, sales_person_schema)
company_df = spark.createDataFrame(company_data, company_schema)
orders_df = spark.createDataFrame(orders_data, orders_schema)

sales_person_df.show()
company_df.show()
orders_df.show()

print("--- Solution #1 ---")
# region: solution
from pyspark.sql.functions import col

red_orders_df = (
    orders_df.alias("o")
        .join(
            company_df.alias("c"),
            on = "com_id",
            how = "inner"
        )
        .filter(col("name") == "RED")
)

result_df = (
    sales_person_df.alias("s")
        .join(
            red_orders_df.alias("ro"),
            on = "sales_id",
            how = "left_anti"
        )
        .select(col("s.name"))
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice

# endregion