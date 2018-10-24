# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 23:06:43 2018

@author: Rajput
"""
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d=open('pickle/all_list.pickle','rb')
combined_list=pickle.load(d)
d.close()

d=open('pickle/ham_words.pickle','rb')
ham_list=pickle.load(d)
d.close()
ham_words=' '.join(ham_list)

d=open('pickle/spam_words.pickle','rb')
spam_list=pickle.load(d)
d.close()
spam_words=' '.join(spam_list)

d=open('pickle/classifierMB.pickle','rb')
multinb=pickle.load(d)
d.close()

training_part = int(len(combined_list) * .7)#partition data in 70:30 format
training_set = combined_list[:training_part]#training data=70%
test_set =  combined_list[training_part:]#testing data=30%   

labels=[row[1] for row in test_set]
test=[row[0] for row in test_set]
results=multinb.classify_many(test)   

def getcloud(label):
    if(label=="ham"):
        words=ham_words
    else:
        words=spam_words
    wordcloud = WordCloud(width=1600, height=800).generate(words)
    plt.figure( figsize=(20,10) )
    plt.imshow(wordcloud)
    plt.axis('off')
    #plt.show() 
    plt.savefig('img/'+label+'.png')
    plt.close()

def getinfo(tag):
    print('confusion matrix')
    cm=confusion_matrix(labels,results)
    print(cm)
    print('accuracy')
    accuracy=accuracy_score(labels,results)
    print(accuracy)
    print('precision')
    precision=precision_score(labels,results,pos_label=tag)
    print(precision)
    print('recall')
    recall=recall_score(labels,results,pos_label=tag)
    print(recall)
    print('f-Score')
    fscore=f1_score(labels,results,pos_label=tag)
    print(fscore)
    plt.matshow(cm, cmap=plt.cm.binary, interpolation='nearest')
    plt.title('confusion matrix')
    plt.colorbar()
    plt.ylabel('expected label')
    plt.xlabel('predicted label')
    plt.savefig('img/conf_mat.png')
    plt.close()
    return accuracy,precision,recall,fscore
