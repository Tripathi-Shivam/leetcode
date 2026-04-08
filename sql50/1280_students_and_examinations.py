from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.getOrCreate()

students_schema = StructType([
    StructField("student_id", IntegerType(), False),
    StructField("student_name", StringType(), False)
])

students_data = [
    (1, "Alice"),
    (2, "Bob"),
    (13, "John"),
    (6, "Alex"),
]

students = spark.createDataFrame(students_data, students_schema)

subjects_schema = StructType([
    StructField("subject_name", StringType(), False)
])

subjects_data = [
    ("Math",),
    ("Physics",),
    ("Programming",),
]

subjects = spark.createDataFrame(subjects_data, subjects_schema)

examinations_schema = StructType([
    StructField("student_id", IntegerType(), False),
    StructField("subject_name", StringType(), False)
])

examinations_data = [
    (1,  "Math"),
    (1,  "Physics"),
    (1,  "Programming"),
    (2,  "Programming"),
    (1,  "Physics"),
    (1,  "Math"),
    (13, "Math"),
    (13, "Programming"),
    (13, "Physics"),
    (2,  "Math"),
    (1,  "Math"),
]

examinations = spark.createDataFrame(examinations_data, examinations_schema)

students.show()
subjects.show()
examinations.show()

# solution
from pyspark.sql.functions import col, when, sum

result = (
    students.alias("stu")
        .crossJoin(subjects.alias("sub"))
        .alias("ssi")
        .join(
            examinations.alias("exam"), 
            on = 
                (col("ssi.student_id") == col("exam.student_id")) 
                & (col("ssi.subject_name") == col("exam.subject_name")), 
            how = "left"
        )
        .groupBy(
            col("ssi.student_id"), 
            col("ssi.student_name"), 
            col("ssi.subject_name")
        )
        .agg(sum(when(col("exam.student_id").isNull(), 0).otherwise(1)).alias("attended_exams"))
        .orderBy("student_id", "student_name", "subject_name")
)
result.show()