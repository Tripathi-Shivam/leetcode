from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("id",          IntegerType(), False),
    StructField("movie",       StringType(),  False),
    StructField("description", StringType(),  False),
    StructField("rating",      DoubleType(),  False),
])

data = [
    (1, "War",      "great 3D",   8.9),
    (2, "Science",  "fiction",    8.5),
    (3, "irish",    "boring",     6.2),
    (4, "Ice song", "Fantacy",    8.6),
    (5, "House",    "interesting",9.1),
]

cinema = spark.createDataFrame(data, schema)
cinema.show()

# solution
from pyspark.sql.functions import col

result = (
    cinema
        .filter(
            (col("id") % 2 == 1)
            & (col("description") != "boring")
        )
        .orderBy(col("rating").desc())
)