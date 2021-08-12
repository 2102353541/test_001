import pandas as pd

#参数初始化
inputfile='D:/DM(data_mining)_data/chapter/chapter5/demo/data/consumption_data.xls'
outputfile='D:/DM(data_mining)_data/chapter/chapter5/demo/tmp/data_type.xls'
k=3#聚类的类别个数（分为三类）
iteration=500#聚类最大循环次数
data=pd.read_excel(inputfile,index_col='Id')#读取数据
data_zs=1.0*(data-data.mean())/data.std()#数据标准化



