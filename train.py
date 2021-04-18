# -*-coding:utf-8-*-

def train():
    from snownlp import sentiment
    print("开始训练数据集...")
    sentiment.train('negative.txt', 'positive.txt')#自己准备数据集
    sentiment.save('sentiment.marshal')#保存训练模型
    #python2保存的是sentiment.marshal；python3保存的是sentiment.marshal.3
    "训练完成后，将训练完的模型，替换sentiment中的模型"

def main():
    train()  # 训练正负向商品评论数据集
    print("数据集训练完成！")

if __name__ == '__main__':
    main()