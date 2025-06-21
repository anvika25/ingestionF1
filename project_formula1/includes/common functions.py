# Databricks notebook source
from pyspark.sql.functions import * 
from pyspark.sql.types import * 
def add_ingestion_date(input_df):
    output_df = input_df.withColumn("ingestion_date",current_timestamp())
    return output_df
