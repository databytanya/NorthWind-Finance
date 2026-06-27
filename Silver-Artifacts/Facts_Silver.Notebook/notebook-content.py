# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# MAGIC %%configure -f
# MAGIC {"defaultLakehouse": { 
# MAGIC         "name": "NorthWind_Finance_lakehouse"
# MAGIC     }
# MAGIC }


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pyspark.sql.functions as F
df_fact_budget=spark.sql("Select * from Bronze.fact_budget")
df_fact_budget=df_fact_budget.withColumn("BudgetAmount",F.col("BudgetAmount").cast("double")) \
                             .withColumn("Month",F.to_date(F.col("Month"))) \
                             .withColumn("DateKey", F.date_format("Month", "yyyyMMdd").cast('string'))
df_fact_budget.write.mode('overwrite').save('Tables/Silver/fact_budget')                             

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_fact_forecast=spark.sql("Select * from Bronze.fact_forecast")
df_fact_forecast=df_fact_forecast.withColumn("ForecastAmount",F.col("ForecastAmount").cast("double")) \
                             .withColumn("Month",F.to_date(F.col("Month"))) \
                             .withColumn("DateKey", F.date_format("Month", "yyyyMMdd").cast('string'))
df_fact_forecast.write.mode('overwrite').save('Tables/Silver/fact_forecast') 


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_fact_gl_actuals=spark.sql("Select * from Bronze.fact_gl_actuals")
df_fact_gl_actuals=df_fact_gl_actuals.withColumn("Amount",F.col("Amount").cast("double")) \
                             .withColumn("Date",F.to_date(F.col("Date"))) \
                             .withColumn("DateKey", F.date_format("Date", "yyyyMMdd").cast('string'))
df_fact_gl_actuals.write.mode('overwrite').save('Tables/Silver/fact_gl_actuals') 


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
