import analyse
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts.faker import Faker

def draw(all_list):
    avg=all_list[0]
    max=all_list[1]
    min=all_list[2]
    wzlx=all_list[3]
    fjsl=all_list[4]
    fxlx=all_list[5]
    fxsl=all_list[6]
    fjdx=all_list[7]
    bar = Bar()
    bar.add_xaxis(wzlx)
    bar.add_yaxis("平均值", avg, stack="stack1")
    bar.add_yaxis("最大值", max, stack="stack1")
    bar.add_yaxis("最小值", min, stack="stack1")
    #bar.add_yaxis("房屋数量", min, stack="stack1")
    bar.set_global_opts(title_opts=opts.TitleOpts(title="郑州市租金概况"),
                        toolbox_opts=opts.ToolboxOpts(is_show=True))#工具箱
    bar.render("郑州市租金概况")


    line = Line()
    line.add_xaxis(wzlx)
    line.add_yaxis("房间数量", fjsl, stack="stack1")
    line.set_global_opts(title_opts=opts.TitleOpts(title="郑州市房间数量概况"),
                        toolbox_opts=opts.ToolboxOpts(is_show=True))#
    line.render("郑州市房间数量概况")

    bar = Bar()
    bar.add_xaxis(fxlx)
    bar.add_yaxis("房间类型", fxsl, stack="stack1")
    bar.set_global_opts(title_opts=opts.TitleOpts(title="郑州市房间类型概况"),
                        toolbox_opts=opts.ToolboxOpts(is_show=True))#工具箱
    bar.render("郑州市房间类型概况")

    dx=["10-30","30-50","50-70","70-90","90-110","110-130","130-150","150-170"]
    data={"fq":dx,"fjdx":fjdx}
    dx=pd.DataFrame(data)

    pie=Pie()
    pie.add("dx",[list(z) for z in zip(dx["fq"], dx["fjdx"])])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="郑州市房间大小概况"))  # 标题
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))  # 数据标签设置
    pie.render("郑州市房间大小概况")
    print("结束绘图")
