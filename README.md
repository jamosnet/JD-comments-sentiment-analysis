# 京东商品评论情感分析
爬取京东商城中指定商品下的用户评论，对数据预处理后基于SnowNLP的sentiment模块对文本进行情感分析。
## 运行环境

* Mac OS X 兼容更低版本
* Python3.7  `requirements.txt`
* Pycharm
---
## 运行方法
#### 数据爬取（`jd.comment.py`)
1. 启动`jd_comment.py`，建议修改`jd_comment.py`中变量user-agent为自己浏览器用户代理
2. 输入京东商品完整URL
3. 得到京东评论词云，存放于`jd_ciyun.jpg`（词云轮廓形状存放于`jdicon.jpg`)
4. 得到京东评论数据，存放于`jd_comment.csv`
#### 模型训练（`train.py`）
1. 准备正负语料集[`online_shopping_10_cats.csv`](https://link.zhihu.com/?target=https%3A//github.com/SophonPlus/ChineseNlpCorpus/raw/master/datasets/online_shopping_10_cats/online_shopping_10_cats.zip)，分别存入negative.txt和positive.txt
2. 启动`train.py`，新建文件`sentiment.marshal`，存入训练后的模型
3. 找到外部库中snownlp中sentiment模块，将训练得到的`sentiment.marshal.3`文件覆盖sentiment模块中自带的`sentiment.marshal.3`
#### 情感分析（`sentiment.analysis.py`）
1. 启动`sentiment.analysis.py`
2. 开始对`jd_comment.csv`中评论进行数据处理，处理后文件存入`processed_comment_data.csv`
3. sentiment模块根据`sentiment.marshal.3`对评论进行情感评分，评分结果存入`result.csv`
4. 评分结果可视化，生成文件`fig.png`
---
* 词云轮廓图
<img src="https://raw.githubusercontent.com/DA1YAYUAN/JD-comments-sentiment-analysis/main/jdicon.jpg" width=200 height=200/>
* 商品评论词云
<img src="https://raw.githubusercontent.com/DA1YAYUAN/JD-comments-sentiment-analysis/main/jd_ciyun.jpg" width=500 height=500/>
* 情感分析结果可视化
<img src="https://raw.githubusercontent.com/DA1YAYUAN/JD-comments-sentiment-analysis/main/fig.png" width=600 height=500/>
