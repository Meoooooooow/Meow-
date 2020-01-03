#encoding:utf-8
'''
程序：实现对《黎明破晓的街道》文本中人物关系的提取。
作者：王紫鑫
2020.1.3
'''

import os,sys
import jieba,codecs,math
import jieba.posseg as pseg
#姓名字典
names={} 
#关系字典
relationships={}
#每段人物关系
lineNames=[]  
#设置字典,加载字典
jieba.load_userdict('dict.txt')
with codecs.open("黎明破晓的街道.txt",'r','gbk') as f:
    for line in f.readlines():
        poss=pseg.cut(line)
        lineNames.append([])
        for w in poss:
            if  w.flag!="nr" or len(w.word) <2:
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word]=0
                relationships[w.word]={}
            names[w.word]+=1
    for name,times in names.items():
        print (name,times)
#根据识别结果构架网络
for line in lineNames:
   for name1 in line:
      for name2 in line:
          if name1==name2:
              continue
          if relationships[name1].get(name2) is None:
            relationships[name1][name2]=1
          else:
            relationships[name1][name2]+=1
#过滤冗余的边并输出结果，将已经建立好的names和relationships输出到文本

#节点集合保存在黎明破晓的街道_node.txt
with codecs.open('黎明破晓的街道_node.txt','w','gbk') as f:
    f.write("id lable weight\r\n")
    for name,times in names.items():
        f.write(name+" "+name+" "+str(times)+"\r\n")
#边集合保存在黎明破晓的街道_edge.txt
with codecs.open('黎明破晓的街道_edge.txt','w','gbk') as f:
    f.write("source target weight\r\n")
    for name,edges in relationships.items():
        for v, w in edges.items():
            if w>3:
                f.write(name+ " "+v+" "+str(w)+"\r\n")
