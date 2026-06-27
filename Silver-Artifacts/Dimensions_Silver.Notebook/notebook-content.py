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
df_dim_date=spark.sql("Select * from Bronze.dim_date")
df_dim_date=df_dim_date.withColumn("Date",F.to_date(F.col("Date")))
df_dim_date.write.mode("overwrite").save("Tables/Silver/dim_date")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_dim_region=spark.sql("Select * from Bronze.dim_region")
df_dim_region=df_dim_reigon.withColumn("PlanWeight",F.col("PlanWeight").cast("double"))
df_dim_region.write.mode("overwrite").save("Tables/Silver/dim_region")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_dim_account=spark.sql("Select * from Bronze.dim_account")
df_Department=spark.sql("Select * from Bronze.dim_department")

df_dim_account.write.mode("overwrite").save("Tables/Silver/dim_account")
df_Department.write.mode("overwrite").save("Tables/Silver/dim_department")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
