爬取京东商城中指定商品下的用户评论，对数据预处理后基于SnowNLP的sentiment模块对文本进行情感分析。
## 运行环境

* Mac OS X
* Python3.7
* Pycharm
---
## 运行方法
#### 数据爬取（jd.comment.py)
1. 启动jd_comment.py
2. 输入京东商品地址
3. 得到京东评论词云，存放于jd_ciyun.jpg（词云轮廓形状存放于jdicon.jpg)
4. 得到京东评论数据，存放于jd_comment.csv
#### 模型训练（train.py）
1. 准备正负语料集[online_shopping_10_cats.csv](https://link.zhihu.com/?target=https%3A//github.com/SophonPlus/ChineseNlpCorpus/raw/master/datasets/online_shopping_10_cats/online_shopping_10_cats.zip)，分别存入negative.txt和positive.txt
2. 启动train.py，新建文件sentiment.marshal，存入训练后的模型
3. 找到外部库中snownlp中sentiment模块，将训练得到的sentiment.marshal.3文件覆盖sentiment模块中自带的sentiment.marshal.3
#### 情感分析（sentiment.analysis.py）
1. 启动sentiment.analysis.py
2. 开始对jd_comment.csv中评论进行数据处理，处理后文件存入processed_comment_data.csv
3. sentiment模块根据sentiment.marshal.3对评论进行情感评分，评分结果存入result.csv
4. 评分结果可视化，生成文件fig.png
---
