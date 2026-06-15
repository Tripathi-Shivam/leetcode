from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, BooleanType

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("seat_id", IntegerType(), False),
    StructField("free", BooleanType(), False),
])

data = [
    (1, True),
    (2, False),
    (3, True),
    (4, True),
    (5, True),
]

cinema_df = spark.createDataFrame(data, schema)
cinema_df.show()

print("--- Solution #1 ---")
# region: solution #1
from pyspark.sql.window import Window
from pyspark.sql.functions import col, lag, lead

window_spec = Window.orderBy(col("seat_id"))

result_df = (
    cinema_df
        .withColumn("prev_seat", lag(col("free"), 1).over(window_spec))
        .withColumn("next_seat", lead(col("free"), 1).over(window_spec))
        .filter(
            (col("free") == True)
            & ((col("prev_seat") == True) | (col("next_seat") == True))
        )
        .select("seat_id")
        .orderBy("seat_id")
)

result_df.show()
# endregion

print("--- Solution #2 ---")
# region: solution #2
from pyspark.sql.functions import col, lit

result_df = (
    cinema_df.alias("c1")
        .join(
            cinema_df.alias("c2"),
            on = col("c1.seat_id") == (col("c2.seat_id") + lit(1)),
            how = "left"
        )
        .join(
            cinema_df.alias("c3"),
            on = col("c1.seat_id") == (col("c3.seat_id") - lit(1)),
            how = "left"
        )
        .filter(
            (col("c1.free") == True)
            & (
                (col("c2.free") == True)
                | (col("c3.free") == True)
            )
        )
        .select(col("c1.seat_id"))
        .orderBy("seat_id")
)

result_df.show()
# endregion

print("--- Solution #3 ---")
# region: solution #3
from pyspark.sql.functions import col, abs

result_df = (
    cinema_df.alias("c1")
        .join(
            cinema_df.alias("c2"),
            on = abs(col("c1.seat_id") - col("c2.seat_id")) == 1,
            how = "inner"
        )
        .filter((col("c1.free") == 1) & (col("c2.free") == 1))
        .select("c1.seat_id")
        .distinct()
        .orderBy("seat_id")
)

result_df.show()
#endregion

print("--- Practice #1 ---")
# region: practice #1

# endregion