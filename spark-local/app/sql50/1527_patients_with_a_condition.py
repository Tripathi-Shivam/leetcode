from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField("patient_id", IntegerType(), False),
    StructField("patient_name", StringType(), False),
    StructField("conditions", StringType(), False)
])

data = [
    (1, "Daniel", "YFEV COUGH"),
    (2, "Alice", "DIAB100 MYOP"),
    (3, "Bob", "ACNE DIAB100"),
    (4, "George", "DIAB201"),
    (5, "Alain", "DIAB100")
]

patients_df = spark.createDataFrame(data, schema)
patients_df.show()

# solution
from pyspark.sql.functions import col

result_df = (
    patients_df
        .filter(col("conditions").rlike('(^| )DIAB1'))
)
result_df.show()