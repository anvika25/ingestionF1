# Databricks notebook source
from pyspark.dbutils import DBUtils


    


# COMMAND ----------

def final_notebook():
    dbutils = DBUtils(spark)

    # Get the notebook path
    notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
    notebook_name = notebook_path.split('/')[-1]
    print(f"Notebook {notebook_name} action completed.")
final_notebook()
