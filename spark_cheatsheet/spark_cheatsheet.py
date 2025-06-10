from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, count, sum, avg, when, isnan, lit, to_timestamp, year, row_number
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("interview-prep").getOrCreate()

# -----------------------------
# 1. Handling Complex Schemas
# -----------------------------
nested_schema = StructType([
    StructField("id", StringType()),
    StructField("info", StructType([
        StructField("name", StringType()),
        StructField("age", IntegerType()),
        StructField("emails", ArrayType(StringType()))
    ]))
])

data = [
    {"id": "1", "info": {"name": "Alice", "age": 30, "emails": ["a@example.com", "alice@mail.com"]}},
    {"id": "2", "info": {"name": "Bob", "age": 40, "emails": ["bob@example.com"]}}
]

df = spark.createDataFrame(data, schema=nested_schema)
df.select("id", "info.name", "info.age", explode("info.emails").alias("email")).show()

# -----------------------------
# 2. withColumn, groupBy, agg, join, explode, window
# -----------------------------
users = spark.createDataFrame([
    ("u1", "USA"), ("u2", "UK"), ("u3", "USA")
], ["user_id", "country"])

events = spark.createDataFrame([
    ("u1", "click", "2024-01-01"),
    ("u1", "click", "2024-01-02"),
    ("u2", "purchase", "2024-01-03"),
], ["user_id", "event_type", "event_date"])

# withColumn: cast, add new column
events = events.withColumn("event_date", to_timestamp("event_date"))

# groupBy + agg
event_counts = events.groupBy("user_id").agg(count("*").alias("event_count"))

# join
joined = event_counts.join(users, on="user_id", how="inner")

# window function
window_spec = Window.partitionBy("country").orderBy(col("event_count").desc())
ranked = joined.withColumn("rank", row_number().over(window_spec))

# -----------------------------
# 3. Join Types
# -----------------------------
# inner, left, right, full, semi, anti
left = spark.createDataFrame([("1", "a")], ["id", "val"])
right = spark.createDataFrame([("1", 100), ("2", 200)], ["id", "score"])

left.join(right, on="id", how="left").show()
left.join(right, on="id", how="left_semi").show()

# -----------------------------
# 4. UDF Example
# -----------------------------
from pyspark.sql.functions import udf

def is_adult(age):
    return age >= 18 if age is not None else False

is_adult_udf = udf(is_adult)

df.withColumn("is_adult", is_adult_udf(col("info.age"))).show()

# -----------------------------
# 5. Handling Missing / Malformed Data
# -----------------------------
df_missing = spark.createDataFrame([
    (None, "a", None),
    ("2", None, 25),
    ("3", "c", 35)
], ["id", "name", "age"])

df_missing.dropna().show()
df_missing.fillna({"name": "unknown", "age": 0}).show()
df_missing.withColumn("valid_age", when(col("age").isNull(), lit(False)).otherwise(lit(True))).show()

# -----------------------------
# 6. Working with Timestamps
# -----------------------------
events.withColumn("year", year("event_date")).show()

# -----------------------------
# 7. Optimizations
# -----------------------------
# Caching
joined.cache()

# Partitioning (when writing data)
# joined.write.partitionBy("country").parquet("path")

# Broadcast Join Hint (for small tables)
from pyspark.sql.functions import broadcast
joined = events.join(broadcast(users), "user_id")
