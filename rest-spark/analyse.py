from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import col
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts.faker import Faker

def spark_analyse(rent):
    print("开始spark分析")
    # 程序主入口
    spark = SparkSession.builder.master("local").appName("rent_analyse").getOrCreate()
    df = spark.read.csv(rent,header=True)
    df1 = df.withColumn("price",df.price.cast(IntegerType())).withColumn("daxiao",df.daxiao.cast(IntegerType()))
    df2=df1.toPandas()
    def zjgk(cl):
        zjgk_list=list(df2.groupby("weizhi").agg({"price":cl})["price"])
        zjgk=[float("{:.2f}".format(i)) for i in zjgk_list]
        return zjgk
    avg=zjgk("mean")
    max=zjgk("max")
    min=zjgk("min")
    fjsl_df = df1.groupby("weizhi").count()
    wzlx_list=list(fjsl_df.toPandas()["weizhi"])
    fjsl_list=list(fjsl_df.toPandas()["count"])
    fx_df = df1.groupby("fangxing").count()
    fxlx_list=list(fx_df.toPandas()["fangxing"])
    fxsl_list=list(fx_df.toPandas()["count"])
    dx = df1.toPandas()["daxiao"]
    fjdx_list = list(pd.cut(dx, [10,30,50,70,90,110,130,150,170]).value_counts())
    all_list=[]
    all_list.append(avg)
    all_list.append(max)
    all_list.append(min)
    all_list.append(wzlx_list)
    all_list.append(fjsl_list)
    all_list.append(fxlx_list)
    all_list.append(fxsl_list)
    all_list.append(fjdx_list)
    return all_list


