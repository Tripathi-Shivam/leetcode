from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("article_id", IntegerType(), False),
    StructField("author_id", IntegerType(), False),
    StructField("viewer_id", IntegerType(), False),
    StructField("view_date", DateType(), False),
])

data = [
    (1, 3, 5, date(2019, 8, 1)),
    (1, 3, 6, date(2019, 8, 2)),
    (2, 7, 7, date(2019, 8, 1)),
    (2, 7, 6, date(2019, 8, 2)),
    (4, 7, 1, date(2019, 7, 22)),
    (3, 4, 4, date(2019, 7, 21)),
    (3, 4, 4, date(2019, 7, 21)),
]

df_views = spark.createDataFrame(data, schema)
df_views.show()

# solution
from pyspark.sql.functions import col

result = (
    df_views
        .filter(
            (col("author_id") == col("viewer_id"))
        )
        .select(col("author_id").alias("id"))
        .distinct()
        .orderBy(col("id").asc())
)
result.show()