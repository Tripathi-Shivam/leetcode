from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("pid", IntegerType(), False),
    StructField("tiv_2015", DoubleType(), False),
    StructField("tiv_2016", DoubleType(), False),
    StructField("lat", DoubleType(), False),
    StructField("lon", DoubleType(), False)
])

data = [
    (1, 10.0, 5.0, 10.0, 10.0),
    (2, 20.0, 20.0, 20.0, 20.0),
    (3, 10.0, 30.0, 20.0, 20.0),
    (4, 10.0, 40.0, 40.0, 40.0)
]

insurance_df = spark.createDataFrame(data, schema)
insurance_df.show()

print("--- Solution #1 ---")
# region: solution
from pyspark.sql.functions import col, lit, concat, count, sum
from pyspark.sql.window import Window

window_spec_1 = Window.partitionBy(concat(col("lat"), lit("-"), col("lon")))
window_spec_2 = Window.partitionBy(col("tiv_2015"))

result_df = (
    insurance_df
        .withColumn("cnt_lat_lon", count("*").over(window_spec_1))
        .withColumn("cnt_tiv_2015", count("*").over(window_spec_2))
        .filter(
            (col("cnt_lat_lon") == 1)
            & (col("cnt_tiv_2015") > 1)
        )
        .agg(sum(col("tiv_2016")).alias("tiv_2016"))
)
result_df.show()
# endregion

print("--- Practice #1 ---")
# region: practice

# endregion