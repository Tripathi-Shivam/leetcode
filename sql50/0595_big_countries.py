from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("name", StringType(), False),
    StructField("continent", StringType(), False),
    StructField("area", IntegerType(), False),
    StructField("population", IntegerType(), False),
    StructField("gpd", LongType(), False),
])

data = [
    ("Afghanistan", "Asia",    652230,    25500100,  20343000000),
    ("Albania",     "Europe",  28748,     2831741,   12960000000),
    ("Algeria",     "Africa",  2381741,   37100000,  188681000000),
    ("Andorra",     "Europe",  468,       78115,     3712000000),
    ("Angola",      "Africa",  1246700,   20609294,  100990000000),
]

df_world = spark.createDataFrame(data, schema)
df_world.show()

# solution
from pyspark.sql.functions import col

result = (
    df_world
    .filter(
        (col("area") >= 3_000_000) 
        | (col("population") >= 25_000_000)
    )
    .select("name", "population", "area")
)
result.show()