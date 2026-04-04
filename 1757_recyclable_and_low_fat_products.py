# data prep
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("product_id", IntegerType(), False),
    StructField("low_fats", StringType(), False),
    StructField("recyclable", StringType(), False)
])

data = [
    (0, "Y", "N"),
    (1, "Y", "Y"),
    (2, "N", "Y"),
    (3, "Y", "Y"),
    (4, "N", "N"),
]

products = spark.createDataFrame(data, schema)
products.show()

# solution
from pyspark.sql.functions import col

result = (
    products
    .filter((col("low_fats") == "Y") & (col("recyclable") == "Y"))              # using col
    # .where((products["low_fats"] == "Y") & (products["recyclable"] == "Y"))   # without col, if more than one table with same column name
    .select("product_id")
)

result.show()