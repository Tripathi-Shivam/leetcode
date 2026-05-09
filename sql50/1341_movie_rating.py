from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from datetime import date

spark = SparkSession.builder.getOrCreate()

# Movies
movies_schema = StructType([
    StructField("movie_id", IntegerType(), False),
    StructField("title", StringType(), False)
])

movies_data = [
    (1, "Avengers"),
    (2, "Frozen 2"),
    (3, "Joker")
]

movies_df = spark.createDataFrame(movies_data, movies_schema)

# Users
users_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("name", StringType(), False)
])

users_data = [
    (1, "Daniel"),
    (2, "Monica"),
    (3, "Maria"),
    (4, "James")
]

users_df = spark.createDataFrame(users_data, users_schema)

# MovieRating
ratings_schema = StructType([
    StructField("movie_id", IntegerType(), False),
    StructField("user_id", IntegerType(), False),
    StructField("rating", IntegerType(), False),
    StructField("created_at", DateType(), False)
])

ratings_data = [
    (1, 1, 3, date(2020, 1, 12)),
    (1, 2, 4, date(2020, 2, 11)),
    (1, 3, 2, date(2020, 2, 12)),
    (1, 4, 1, date(2020, 1, 1)),
    (2, 1, 5, date(2020, 2, 17)),
    (2, 2, 2, date(2020, 2, 1)),
    (2, 3, 2, date(2020, 3, 1)),
    (3, 1, 3, date(2020, 2, 22)),
    (3, 2, 4, date(2020, 2, 25))
]

ratings_df = spark.createDataFrame(ratings_data, ratings_schema)

movies_df.show(truncate=False)
users_df.show(truncate=False)
ratings_df.show(truncate=False)

# solution
from pyspark.sql.functions import col, count, date_format, avg

greatest_no_of_movies_df = (
    users_df.alias("u")
        .join(
            ratings_df.alias("r"),
            on = "user_id",
            how = "inner"
        )
        .groupBy("u.name")
        .agg(count(col("r.movie_id")).alias("no_of_movies"))
        .orderBy(col("no_of_movies").desc(), col("u.name").asc())
        .limit(1)
        .select(col("u.name").alias("results"))
)
greatest_no_of_movies_df.show()

highest_avg_rating_df = (
    movies_df.alias("m")
        .join(
            ratings_df.alias("r"),
            on = "movie_id",
            how = "inner"
        )
        .filter(date_format(col("created_at"), "yyyy-MM") == "2020-02")
        .groupBy("m.title")
        .agg(avg(col("rating")).alias("avg_rating"))
        .orderBy(col("avg_rating").desc(), col("m.title").asc())
        .limit(1)
        .select(col("m.title").alias("result"))
)
highest_avg_rating_df.show()

result_df = (
    greatest_no_of_movies_df
        .unionAll(highest_avg_rating_df)
)
result_df.show()