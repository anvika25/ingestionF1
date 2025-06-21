# Databricks notebook source
# MAGIC %run "/project_formula1/includes/common functions"

# COMMAND ----------

# MAGIC %run "/project_formula1/includes/auditfunctions"

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

name_schema = StructType(fields=[StructField("forename", StringType(), True),
                                 StructField("surname", StringType(), True)
  
])


# COMMAND ----------

drivers_schema = StructType(fields=[StructField("driverId", IntegerType(), False),
                                    StructField("driverRef", StringType(), True),
                                    StructField("number", IntegerType(), True),
                                    StructField("code", StringType(), True),
                                    StructField("name", name_schema),
                                    StructField("dob", DateType(), True)
])

# COMMAND ----------

df1 = spark.read.schema(drivers_schema).json('/Volumes/formula1/raw/raw/drivers.json')
df2 = df1.withColumn("name", concat(col("name.forename"), lit(" "), col("name.surname")))
df2.display()

# COMMAND ----------

df2 = add_ingestion_date(df2)
df2.display()

# COMMAND ----------

df2.write.mode('overwrite').saveAsTable('dim_drivers')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from dim_drivers

# COMMAND ----------

final_notebook()
