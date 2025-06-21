# Databricks notebook source
# MAGIC %run "/project_formula1/includes/common functions"

# COMMAND ----------

# MAGIC %run "/project_formula1/includes/auditfunctions"

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

drivers_schema = StructType(fields=[StructField("resultId", IntegerType(), True),
                                    StructField("raceId", IntegerType(), True),
                                    StructField("driverId", StringType(), True),
                                    StructField("constructorId", StringType(), True),
                                    StructField("number", IntegerType(), True),
                                    StructField("grid", IntegerType(), True),
                                    StructField("position", IntegerType(), True),
                                    StructField("positionText", IntegerType(), True),
                                    StructField("positionOrder", IntegerType(), True),
                                    StructField("points", IntegerType(), True),
                                    StructField("laps", IntegerType(), True),
                                    StructField("time", StringType(), True),
                                    StructField("milliseconds", StringType(), True),
                                    StructField("fastestLap", IntegerType(), True),
                                    StructField("rank", IntegerType(), True),
                                    StructField("fastestLaptime", StringType(), True),
                                    StructField("fastestLapSpeed", StringType(), True),
                                    StructField("statusId", IntegerType(), True)
])

# COMMAND ----------

df1 = spark.read.schema(drivers_schema).json('/Volumes/formula1/raw/raw/drivers.json')

df1.display()

# COMMAND ----------

df2 = add_ingestion_date(df1)
df2.display()

# COMMAND ----------

df2.write.mode('overwrite').saveAsTable('dim_results')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from dim_results

# COMMAND ----------

final_notebook()
