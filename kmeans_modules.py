# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:48:39 2018

@author: dell
"""
#画线图
def line(data, k):
    import pygal
    if k == 4:
        line_chart = pygal.Line()
        line_chart.title = '聚类中心指标线图'
        line_chart.x_labels = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC']
        line_chart.add('1', list(data.iloc[0,1:].values))
        line_chart.add('2', list(data.iloc[1,1:].values))
        line_chart.add('3', list(data.iloc[2,1:].values))
        line_chart.add('4', list(data.iloc[3,1:].values))
        line_chart.render_to_file('center_line.svg')
    if k == 5:
        line_chart = pygal.Line()
        line_chart.title = '聚类中心指标线图'
        line_chart.x_labels = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC']
        line_chart.add('1', list(data.iloc[0,1:].values))
        line_chart.add('2', list(data.iloc[1,1:].values))
        line_chart.add('3', list(data.iloc[2,1:].values))
        line_chart.add('4', list(data.iloc[3,1:].values))
        line_chart.add('5', list(data.iloc[4,1:].values))
        line_chart.render_to_file('center_line.svg')
    if k == 6:
        line_chart = pygal.Line()
        line_chart.title = '聚类中心指标线图'
        line_chart.x_labels = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC']
        line_chart.add('1', list(data.iloc[0,1:].values))
        line_chart.add('2', list(data.iloc[1,1:].values))
        line_chart.add('3', list(data.iloc[2,1:].values))
        line_chart.add('4', list(data.iloc[3,1:].values))
        line_chart.add('5', list(data.iloc[4,1:].values))
        line_chart.add('6', list(data.iloc[5,1:].values))
        line_chart.render_to_file('center_line.svg')
    if k == 8:
        line_chart = pygal.Line()
        line_chart.title = '聚类中心指标线图'
        line_chart.x_labels = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC']
        line_chart.add('1', list(data.iloc[0,1:].values))
        line_chart.add('2', list(data.iloc[1,1:].values))
        line_chart.add('3', list(data.iloc[2,1:].values))
        line_chart.add('4', list(data.iloc[3,1:].values))
        line_chart.add('5', list(data.iloc[4,1:].values))
        line_chart.add('6', list(data.iloc[5,1:].values))
        line_chart.add('7', list(data.iloc[6,1:].values))
        line_chart.add('8', list(data.iloc[7,1:].values))
        line_chart.render_to_file('center_line.svg')

#画柱形图
def bar(data, k):
    import pygal
    hist_chart = pygal.Bar()
    hist_chart.title = '各类别客户数量统计图'
    if k == 4:
        hist_chart.x_labels = ['1', '2', '3', '4']
    if k == 5:
        hist_chart.x_labels = ['1', '2', '3', '4', '5']
    if k == 6:
        hist_chart.x_labels = ['1', '2', '3', '4', '5', '6']
    if k == 8:
        hist_chart.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8']
    hist_chart.add('客户数量', list(data.values))
    hist_chart.render_to_file('count_bar.svg')

#画xy点线图
def xy(data, n):
    import pygal
    from pygal.style import RotateStyle, LightColorizedStyle
    #取第n类客户数据
    d1 = data[data['labels'].isin([n])]
    #计算该类客户数量
    d1_count = d1.iloc[:,0].size

    #计算密度
    count_ZL = d1['ZL'].value_counts().reset_index()
    count_ZL.columns = ['value', 'count']
    count_ZL['count'] = count_ZL['count']/d1_count
    count_ZL = count_ZL.sort_values(by = 'value',axis = 0,ascending = True)
    #将计算的密度存储为[(x1,y1),...,(xn,yn)]格式
    list_ZL = [tuple(xi) for xi in count_ZL.values]

    count_ZR = d1['ZR'].value_counts().reset_index()
    count_ZR.columns = ['value', 'count']
    count_ZR['count'] = count_ZR['count']/d1_count
    count_ZR = count_ZR.sort_values(by = 'value',axis = 0,ascending = True)
    list_ZR = [tuple(xi) for xi in count_ZR.values]

    count_ZF = d1['ZF'].value_counts().reset_index()
    count_ZF.columns = ['value', 'count']
    count_ZF['count'] = count_ZF['count']/d1_count
    count_ZF = count_ZF.sort_values(by = 'value',axis = 0,ascending = True)
    list_ZF = [tuple(xi) for xi in count_ZF.values]

    count_ZM = d1['ZM'].value_counts().reset_index()
    count_ZM.columns = ['value', 'count']
    count_ZM['count'] = count_ZM['count']/d1_count
    count_ZM = count_ZM.sort_values(by = 'value',axis = 0,ascending = True)
    list_ZM = [tuple(xi) for xi in count_ZM.values]

    count_ZC = d1['ZC'].value_counts().reset_index()
    count_ZC.columns = ['value', 'count']
    count_ZC['count'] = count_ZC['count']/d1_count
    count_ZC = count_ZC.sort_values(by = 'value',axis = 0,ascending = True)
    list_ZC = [tuple(xi) for xi in count_ZC.values]
    
    
    #画XY图
    xy_ZL_chart = pygal.XY(style=RotateStyle('#FF6347', base_style=LightColorizedStyle))#红色
    xy_ZL_chart.title = str(n)+'类客户ZL密度分布'
    xy_ZL_chart.add('ZL', list_ZL)
    xy_ZL_chart.render_to_file(str(n)+'_ZL_density_xy.svg')
    xy_ZR_chart = pygal.XY(style=RotateStyle('#FFD700', base_style=LightColorizedStyle))#黄色
    xy_ZR_chart.title = str(n)+'类客户ZR密度分布'
    xy_ZR_chart.add('ZR', list_ZR)
    xy_ZR_chart.render_to_file(str(n)+'_ZR_density_xy.svg')
    xy_ZF_chart = pygal.XY(style=RotateStyle('#9AC0CD', base_style=LightColorizedStyle))#蓝色
    xy_ZF_chart.title = str(n)+'类客户ZF密度分布'
    xy_ZF_chart.add('ZF', list_ZF)
    xy_ZF_chart.render_to_file(str(n)+'_ZF_density_xy.svg')
    xy_ZM_chart = pygal.XY(style=RotateStyle('#9ACD32', base_style=LightColorizedStyle))#绿色
    xy_ZM_chart.title = str(n)+'类客户ZM密度分布'
    xy_ZM_chart.add('ZM', list_ZM)
    xy_ZM_chart.render_to_file(str(n)+'_ZM_density_xy.svg')
    xy_ZC_chart = pygal.XY(style=RotateStyle('#DDA0DD', base_style=LightColorizedStyle))#紫色
    xy_ZC_chart.title = str(n)+'类客户ZC密度分布'
    xy_ZC_chart.add('ZC', list_ZC)
    xy_ZC_chart.render_to_file(str(n)+'_ZC_density_xy.svg')

#画密度图    
def density(data, k):
    if k == 4:
        xy(data, 1)
        xy(data, 2)
        xy(data, 3)
        xy(data, 4)
    if k == 5:
        xy(data, 1)
        xy(data, 2)
        xy(data, 3)
        xy(data, 4)
        xy(data, 5)
    if k == 6:
        xy(data, 1)
        xy(data, 2)
        xy(data, 3)
        xy(data, 4)
        xy(data, 5)
        xy(data, 6)
    if k == 8:
        xy(data, 1)
        xy(data, 2)
        xy(data, 3)
        xy(data, 4)
        xy(data, 5)
        xy(data, 6)
        xy(data, 7)
        xy(data, 8)
   
#此函数输入数据文件名、需要分类数和期望结果类型即可得到数据分析结果（存储在相应文件中，详见结果图绘制函数）      
def kmeans(filename_source, k, result_type):#filename_source:导入文件名；k:分类数(提供4、5、6、8类)；result_type:数据可视化结果类别
    
    import pandas as pd
    from sklearn.cluster import KMeans #导入K均值聚类算法
    import numpy as np
    
    datafile = filename_source#原始数据文件（包含L、R、F、M、C）
    
    #data存储原始数据
    data = pd.read_excel(datafile)
    #调整data中列顺序，使其为LRFMC顺序
    d1 = data['L']
    d2 = data['R']
    d3 = data['F']
    d4 = data['M']
    d5 = data['C']
    data = pd.concat([d1, d2, d3, d4, d5], axis=1)
 
    #data1存储清洗完空值的数据
    data1 = data[data.notnull()] 
    
    #data2存储标准化后数据
    data2 = (data1-data1.mean())/data1.std()  #zscore标准化
    data2.columns = ['Z'+i for i in data1.columns]#表头重命名
    
    #kmeans聚类
    #调用k-means算法，进行聚类分析
    kmodel = KMeans(n_clusters=k, n_jobs=4)# n_job是并行数，一般等于CPU数较好
    kmodel.fit(data2)
 
    labels = kmodel.labels_#查看各样本类别
    
    demo = pd.DataFrame(labels,columns=['numbers'])
    demo1= pd.DataFrame(kmodel.cluster_centers_, columns=data2.columns) # 保存聚类中心
    demo2= demo['numbers'].value_counts() # 确定各个类的数目
    demo2.sort_index()
 
    #demo4存储聚类中心数据用于结果可视化
    demo4 = pd.concat([demo2,demo1],axis=1)
    demo4.index.name='labels'
    
    #将样本类别加在data2中以备之后使用
    labels = pd.DataFrame(labels)
    data2 = pd.concat([data2, labels],axis=1)
    new_col = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC', 'labels']
    data2.columns = new_col
    #供以后查询的data2存储在search_data.xlsx中
    data2.to_excel('search_data.xlsx',index=True)
    
    
    #将客户类群进行价值排序（不同分类数算法不同，是我看文章自己设计的，详细算法流程之后会给出流程图，没有什么问题这部分先不要改，有问题告诉我）
    #先计算ZC+ZM和ZL+ZF的值
    demo5 = demo4
    if k == 4:
        custom_123 = demo5.sort_values(by='ZC' , ascending=False)[:3]
        custom_4 = demo5.sort_values(by='ZC' , ascending=False)[3:]
        custom_4['type'] = '一般客户与低价值客户'
        custom_12 = custom_123.sort_values(by='ZR' , ascending=False)[1:]
        custom_3 = custom_123.sort_values(by='ZR' , ascending=False)[:1]
        custom_3['type'] = '重要挽留客户'
        custom_1 = custom_12.sort_values(by='ZL' , ascending=False)[:1]
        custom_2 = custom_12.sort_values(by='ZL' , ascending=False)[1:]
        custom_1['type'] = '重要保持客户'
        custom_2['type'] = '重要发展客户'
        demo6 = custom_1.append([custom_2, custom_3, custom_4])
    if k == 5:
        custom_123 = demo5.sort_values(by='ZC' , ascending=False)[:3]
        custom_45 = demo5.sort_values(by='ZC' , ascending=False)[3:]
        custom_4 = custom_45.sort_values(by='ZM' , ascending=False)[:1]
        custom_5 = custom_45.sort_values(by='ZM' , ascending=False)[1:]
        custom_4['type'] = '一般价值客户'
        custom_5['type'] = '低价值客户'
        custom_12 = custom_123.sort_values(by='ZR' , ascending=False)[1:]
        custom_3 = custom_123.sort_values(by='ZR' , ascending=False)[:1]
        custom_3['type'] = '重要挽留客户'
        custom_1 = custom_12.sort_values(by='ZL' , ascending=False)[:1]
        custom_2 = custom_12.sort_values(by='ZL' , ascending=False)[1:]
        custom_1['type'] = '重要保持客户'
        custom_2['type'] = '重要发展客户'
        demo6 = custom_1.append([custom_2, custom_3, custom_4, custom_5])
    if k == 6:
        custom_123 = demo5.sort_values(by='ZC' , ascending=False)[:3]
        custom_456 = demo5.sort_values(by='ZC' , ascending=False)[3:]
        custom_12 = custom_123.sort_values(by='ZR' , ascending=False)[1:]
        custom_3 = custom_123.sort_values(by='ZR' , ascending=False)[:1]
        custom_3['type'] = '重要挽留客户'
        custom_1 = custom_12.sort_values(by='ZL' , ascending=False)[:1]
        custom_2 = custom_12.sort_values(by='ZL' , ascending=False)[1:]
        custom_1['type'] = '重要保持客户'
        custom_2['type'] = '重要发展客户'
        custom_45 = custom_456.sort_values(by='ZR' , ascending=False)[1:]
        custom_6 = custom_456.sort_values(by='ZR' , ascending=False)[:1]
        custom_6['type'] = '一般挽留客户'
        custom_4 = custom_45.sort_values(by='ZL' , ascending=False)[:1]
        custom_5 = custom_45.sort_values(by='ZL' , ascending=False)[1:]
        custom_4['type'] = '一般保持客户'
        custom_5['type'] = '一般发展客户'
        demo6 = custom_1.append([custom_2, custom_3, custom_4, custom_5, custom_6])
    if k == 8:
        custom_1234 = demo5.sort_values(by='ZC' , ascending=False)[:3]
        custom_5678 = demo5.sort_values(by='ZC' , ascending=False)[3:]
        custom_123 = custom_1234.sort_values(by='ZR' , ascending=False)[1:]
        custom_4 = custom_1234.sort_values(by='ZR' , ascending=False)[:1]
        custom_4['type'] = '重要挽留客户'
        custom_3 = custom_123.sort_values(by='ZL' , ascending=False)[2:]
        custom_3['type'] = '重要发展客户'
        custom_12 = custom_123.sort_values(by='ZL' , ascending=False)[:2]
        custom_1 = custom_12.sort_values(by='ZM' , ascending=False)[:1]
        custom_2 = custom_12.sort_values(by='ZM' , ascending=False)[1:]
        custom_1['type'] = '重要价值客户'
        custom_2['type'] = '重要保持客户'
        custom_567 = custom_5678.sort_values(by='ZR' , ascending=False)[1:]
        custom_8 = custom_5678.sort_values(by='ZR' , ascending=False)[:1]
        custom_8['type'] = '一般挽留客户'
        custom_7 = custom_567.sort_values(by='ZL' , ascending=False)[2:]
        custom_7['type'] = '一般发展客户'
        custom_56 = custom_567.sort_values(by='ZL' , ascending=False)[:2]
        custom_5 = custom_56.sort_values(by='ZM' , ascending=False)[:1]
        custom_6 = custom_56.sort_values(by='ZM' , ascending=False)[1:]
        custom_1['type'] = '一般价值客户'
        custom_2['type'] = '一般保持客户'
        demo6 = custom_1.append([custom_2, custom_3, custom_4, custom_5, custom_6, custom_7, custom_8])
    
    #kmeans_result.xlsx存储结果表格，需要保存，查询指定客户时还需要将类号与客户类名称通过这个表对应
    #这个不需要用户选择，必须直接与结果一起呈现，否则用户不知道1,2,3,4,5...类分别是何种类型客户，后面的结果就没有意义
    demo6.to_excel('kmeans_result.xlsx',index=True)
        
    #数据可视化(我只做到图像生成svg对象，需要你们把svg对象整合输出)
    if result_type == 'center_only':#仅显示聚类中心对比结果--用线图显示（存储文件见函数line）
        line(demo4, k)
    if result_type == 'count_only':#仅显示每类客户数量柱状图（存储文件见函数bar）
        bar(demo4['numbers'], k)
    if result_type == 'density_only':#仅显示客户密度图（存储文件见函数xy）
        density(data2, k)
    if result_type == 'all':#全部显示
        line(demo4, k)
        bar(demo4['numbers'], k)
        density(data2, k)
#kmeans示例        

kmeans('sxgz.xlsx',6,'all')
#kmeans('sxgz.xlsx',4,'density_only')

#再分类时使用的分片函数，返回想要再分类的类别，想要再分类时再将此返回结果放入re_kmeans函数的参数中调用就行了
def slc(index):#index为想要再分类的类别，比如想要将1类再分类，index就为1
    import numpy as np
    import np.pandas as pd
    data = pd.read_excel('search_data.xlsx')
    d = data[data['labels'].isin([index])].drop(['labels'], axis=1)
    return d

#此函数与kmeans几乎相同（没有数据清洗和标准化了，因为已经做过了），只是不输入文件名了，使用时直接输入slc(index),k,result_type，导出的excel名字与kmeans不一样了，前面都加了re，导出图像名字没有变，因为图像是用哪个生成哪个     
def re_kmeans(data2, k, result_type):#k:分类数(提供4、5、6、8类)；result_type:数据可视化结果类别
    
    import pandas as pd
    from sklearn.cluster import KMeans #导入K均值聚类算法
    import numpy as np
    
    #kmeans聚类
    #调用k-means算法，进行聚类分析
    kmodel = KMeans(n_clusters=k, n_jobs=4)# n_job是并行数，一般等于CPU数较好
    kmodel.fit(data2)
 
    labels = kmodel.labels_#查看各样本类别
    
    demo = pd.DataFrame(labels,columns=['numbers'])
    demo1= pd.DataFrame(kmodel.cluster_centers_, columns=data2.columns) # 保存聚类中心
    demo2= demo['numbers'].value_counts() # 确定各个类的数目
    demo2.sort_index()
 
    #demo4存储聚类中心数据用于结果可视化
    demo4 = pd.concat([demo2,demo1],axis=1)
    demo4.index.name='labels'
    
    #将样本类别加在data2中以备之后使用
    labels = pd.DataFrame(labels)
    data2 = pd.concat([data2, labels],axis=1)
    new_col = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC', 'labels']
    data2.columns = new_col
    #供以后查询的data2存储在search_data.xlsx中
    data2.to_excel('re_search_data.xlsx',index=True)
    
    
    #将客户类群进行价值排序（不同分类数算法不同，是我看文章自己设计的，详细算法流程之后会给出流程图，没有什么问题这部分先不要改，有问题告诉我）
    #先计算ZC+ZM和ZL+ZF的值
    demo5 = demo4
    if k == 4:
        custom_123 = demo5.sort_values(by='ZC' , ascending=False)[:3]
        custom_4 = demo5.sort_values(by='ZC' , ascending=False)[3:]
        custom_4['type'] = '一般客户与低价值客户'
        custom_12 = custom_123.sort_values(by='ZR' , ascending=False)[1:]
        custom_3 = custom_123.sort_values(by='ZR' , ascending=False)[:1]
        custom_3['type'] = '重要挽留客户'
        custom_1 = custom_12.sort_values(by='ZL' , ascending=False)[:1]
        custom_2 = custom_12.sort_values(by='ZL' , ascending=False)[1:]
        custom_1['type'] = '重要保持客户'
        custom_2['type'] = '重要发展客户'
        demo6 = custom_1.append([custom_2, custom_3, custom_4])
    if k == 5:
        custom_123 = demo5.sort_values(by='ZC' , ascending=False)[:3]
        custom_45 = demo5.sort_values(by='ZC' , ascending=False)[3:]
        custom_4 = custom_45.sort_values(by='ZM' , ascending=False)[:1]
        custom_5 = custom_45.sort_values(by='ZM' , ascending=False)[1:]
        custom_4['type'] = '一般价值客户'
        custom_5['type'] = '低价值客户'
        custom_12 = custom_123.sort_values(by='ZR' , ascending=False)[1:]
        custom_3 = custom_123.sort_values(by='ZR' , ascending=False)[:1]
        custom_3['type'] = '重要挽留客户'
        custom_1 = custom_12.sort_values(by='ZL' , ascending=False)[:1]
        custom_2 = custom_12.sort_values(by='ZL' , ascending=False)[1:]
        custom_1['type'] = '重要保持客户'
        custom_2['type'] = '重要发展客户'
        demo6 = custom_1.append([custom_2, custom_3, custom_4, custom_5])
    if k == 6:
        custom_123 = demo5.sort_values(by='ZC' , ascending=False)[:3]
        custom_456 = demo5.sort_values(by='ZC' , ascending=False)[3:]
        custom_12 = custom_123.sort_values(by='ZR' , ascending=False)[1:]
        custom_3 = custom_123.sort_values(by='ZR' , ascending=False)[:1]
        custom_3['type'] = '重要挽留客户'
        custom_1 = custom_12.sort_values(by='ZL' , ascending=False)[:1]
        custom_2 = custom_12.sort_values(by='ZL' , ascending=False)[1:]
        custom_1['type'] = '重要保持客户'
        custom_2['type'] = '重要发展客户'
        custom_45 = custom_456.sort_values(by='ZR' , ascending=False)[1:]
        custom_6 = custom_456.sort_values(by='ZR' , ascending=False)[:1]
        custom_6['type'] = '一般挽留客户'
        custom_4 = custom_45.sort_values(by='ZL' , ascending=False)[:1]
        custom_5 = custom_45.sort_values(by='ZL' , ascending=False)[1:]
        custom_4['type'] = '一般保持客户'
        custom_5['type'] = '一般发展客户'
        demo6 = custom_1.append([custom_2, custom_3, custom_4, custom_5, custom_6])
    if k == 8:
        custom_1234 = demo5.sort_values(by='ZC' , ascending=False)[:3]
        custom_5678 = demo5.sort_values(by='ZC' , ascending=False)[3:]
        custom_123 = custom_1234.sort_values(by='ZR' , ascending=False)[1:]
        custom_4 = custom_1234.sort_values(by='ZR' , ascending=False)[:1]
        custom_4['type'] = '重要挽留客户'
        custom_3 = custom_123.sort_values(by='ZL' , ascending=False)[2:]
        custom_3['type'] = '重要发展客户'
        custom_12 = custom_123.sort_values(by='ZL' , ascending=False)[:2]
        custom_1 = custom_12.sort_values(by='ZM' , ascending=False)[:1]
        custom_2 = custom_12.sort_values(by='ZM' , ascending=False)[1:]
        custom_1['type'] = '重要价值客户'
        custom_2['type'] = '重要保持客户'
        custom_567 = custom_5678.sort_values(by='ZR' , ascending=False)[1:]
        custom_8 = custom_5678.sort_values(by='ZR' , ascending=False)[:1]
        custom_8['type'] = '一般挽留客户'
        custom_7 = custom_567.sort_values(by='ZL' , ascending=False)[2:]
        custom_7['type'] = '一般发展客户'
        custom_56 = custom_567.sort_values(by='ZL' , ascending=False)[:2]
        custom_5 = custom_56.sort_values(by='ZM' , ascending=False)[:1]
        custom_6 = custom_56.sort_values(by='ZM' , ascending=False)[1:]
        custom_1['type'] = '一般价值客户'
        custom_2['type'] = '一般保持客户'
        demo6 = custom_1.append([custom_2, custom_3, custom_4, custom_5, custom_6, custom_7, custom_8])
    
    #kmeans_result.xlsx存储结果表格，需要保存，查询指定客户时还需要将类号与客户类名称通过这个表对应
    #这个不需要用户选择，必须直接与结果一起呈现，否则用户不知道1,2,3,4,5...类分别是何种类型客户，后面的结果就没有意义
    demo6.to_excel('re_kmeans_result.xlsx',index=True)
        
    #数据可视化(我只做到图像生成svg对象，需要你们把svg对象整合输出)
    if result_type == 'center_only':#仅显示聚类中心对比结果--用线图显示（存储文件见函数line）
        line(demo4, k)
    if result_type == 'count_only':#仅显示每类客户数量柱状图（存储文件见函数bar）
        bar(demo4['numbers'], k)
    if result_type == 'density_only':#仅显示客户密度图（存储文件见函数xy）
        density(data2, k)
    if result_type == 'all':#全部显示
        line(demo4, k)
        bar(demo4['numbers'], k)
        density(data2, k)

#re_kmeans示例
# re_kmeans(slc(1),4,'center_only')
       
        
        




    
