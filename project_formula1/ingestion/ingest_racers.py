# Databricks notebook source
# MAGIC %run "/project_formula1/includes/common functions"

# COMMAND ----------

# MAGIC %run "/project_formula1/includes/auditfunctions"

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

race_schema = StructType(fields=[StructField("raceId", IntegerType(), False),
                                    StructField("year", DateType(), True),
                                    StructField("round", IntegerType(), True),
                                    StructField("circuitId", StringType(), True),
                                    StructField("name", StringType(), True),
                                    StructField("date", DateType(), True),
                                    StructField("time", DateType(), True),
                                    StructField("url", StringType(), True),
                                    StructField("fp1_date", StringType(), True),
                                    StructField("fp1_time", StringType(), True),
                                    StructField("fp2_date", StringType(), True),
                                    StructField("fp2_time", StringType(), True),
                                    StructField("fp3_date", StringType(), True),
                                    StructField("fp3_time", StringType(), True),
                                    StructField("quali_date", StringType(), True),
                                    StructField("quali_time", StringType(), True)


])

# COMMAND ----------

df1 = spark.read.option('header',True).schema(race_schema).csv('/Volumes/formula1/raw/raw/races.csv')

df1.display()

# COMMAND ----------

df3 = add_ingestion_date(df1)
df3.display()

# COMMAND ----------

df3.write.mode('overwrite').saveAsTable('dim_races')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from dim_races

# COMMAND ----------

final_notebook()
