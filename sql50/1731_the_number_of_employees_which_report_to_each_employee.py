from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("employee_id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("reports_to", IntegerType(), True),
    StructField("age", IntegerType(), False)
])

data = [
    (9, "Hercy", None, 43),
    (6, "Alice", 9, 41),
    (4, "Bob", 9, 36),
    (2, "Winston", None, 37)
]

employees_df = spark.createDataFrame(data, schema)
employees_df.show()

# solution
from pyspark.sql.functions import count, avg, round

emp_df = employees_df.alias("emp_df")
mng_df = employees_df.alias("mng_df")

result = (
    emp_df
        .join(
            mng_df,
            on = emp_df.reports_to == mng_df.employee_id,
            how = "inner"
        )
        .groupBy(mng_df.employee_id, mng_df.name)
        .agg(
            count(emp_df.employee_id).alias("reports_count"),
            round(avg(emp_df.age)).alias("average_age")
        )
        .orderBy("employee_id")
)
result.show()