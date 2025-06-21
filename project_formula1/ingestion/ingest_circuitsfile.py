# Databricks notebook source
# MAGIC %run "/project_formula1/includes/common functions"

# COMMAND ----------

# MAGIC %run "/project_formula1/includes/auditfunctions"

# COMMAND ----------

from pyspark.sql.types import * 
from pyspark.sql.functions import * 
circuits_schema = StructType(fields=[
    StructField("circuitId", IntegerType(), False),
    StructField("circuitRef", StringType(), True),
    StructField("name", StringType(), True),
    StructField("location", StringType(), True),
    StructField("country", StringType(), True),
    StructField("lat", DoubleType(), True),
    StructField("lng", DoubleType(), True),
    StructField("alt", IntegerType(), True),
    StructField("url", StringType(), True)
])

df_circuit = spark.read.option('header',True).schema(circuits_schema).csv('/Volumes/formula1/raw/raw/circuits.csv')

df_circuit = df_circuit.drop('url','alt')
df_circuit.display()



# COMMAND ----------

df_circuit = add_ingestion_date(df_circuit)
df_circuit.display()

# COMMAND ----------

df_circuit.write.mode('overwrite').saveAsTable('dim_circuits')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from dim_circuits

# COMMAND ----------

final_notebook()
