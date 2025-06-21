# Databricks notebook source
# MAGIC %run "/project_formula1/includes/common functions"

# COMMAND ----------

# MAGIC %run "/project_formula1/includes/auditfunctions"

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

con_schema = StructType(fields=[StructField("constructorId", IntegerType(), False),
                                    StructField("constructorRef", StringType(), True),
                                    StructField("name", StringType(), True),
                                    StructField("nationality", StringType(), True),
                                    StructField("url", StringType(), True)
])

# COMMAND ----------

df1 = spark.read.schema(con_schema).json('/Volumes/formula1/raw/raw/constructors.json')

df1.display()

# COMMAND ----------

df1 = add_ingestion_date(df1)
df1.display()

# COMMAND ----------

df1.write.mode('overwrite').saveAsTable('dim_constructors1')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from dim_constructors1

# COMMAND ----------

final_notebook()
