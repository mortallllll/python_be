"""
柱状图制作
"""
from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts,TitleOpts

def main():
    #print("main")
    #读取文件
    f = None
    try:
        f = open("1969-2011GDP.csv","r",encoding="UTF-8")
        content = f.readlines()
    except:
        f = open("1969-2011GDP.csv","w",encoding="UTF-8")
        content = f.readlines()
        f.close()
        #去除第一行无用信息
    content.pop(0)
    #print(content)
    #对content进行处理
    dict_GDP = {}
    timeline = Timeline()
    for line in content:
        line = line.strip()#去除前后空格，换行符
        line = line.split(',')#按照逗号进行分割
        year = int(line[0])
        country = str(line[1])
        gpt_count = float(line[2])
        #print(line)
        #数据存入dict
        try:
            dict_GDP[year].append([country,gpt_count])
        except:
            dict_GDP[year] = []
            dict_GDP[year].append([country,gpt_count])
    #将年份排序
    sorted_year_line = sorted(dict_GDP.keys())
    #制作循环图
    for year in sorted_year_line:
        #将GDP前八数据存入bar
        #排序
        dict_GDP[year].sort(key = lambda elements:elements[1])
        dict_GDP_eight = dict_GDP[year][0:8]
        #print(dict_GDP[year])
        #数据存入bar
        bar = Bar()
        x_data = []
        y_data = []
        for element in dict_GDP_eight:
            x_data.append(element[0])
            y_data.append(element[1])
        #print(x_data)
        bar.add_xaxis(x_data)
        bar.add_yaxis("GDP",y_data,label_opts=LabelOpts(position="right"))
        bar.reversal_axis()
        bar.set_global_opts(
            title_opts=TitleOpts(title=f"{year}年全球前八GDP排名")
        )
        #将bar加入时间线timeline
        timeline.add(bar,str(year))
    #时间线自动播放
    timeline.add_schema(
        play_interval= 1500,
        is_timeline_show= True,
        is_auto_play= True,
        is_loop_play= True
    )
    #循环播放
    timeline.render("1969-2011GDP.html")



if __name__ == '__main__':
    main()