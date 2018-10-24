# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:43:00 2018

@author: Rajput
"""
import random
import pickle 
from nltk.classify.scikitlearn import SklearnClassifier
import nltk.classify.util
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
import os
import string

def cleaning_data(data):
    #split into words
    tokens=word_tokenize(data)
    #convert to lower case
    tokens=[w.lower() for w in tokens]
    #remove punctuation 
    table=str.maketrans('','',string.punctuation)
    stripped=[w.translate(table) for w in tokens]
    #remove tokens which are not alphabetic
    words=[word for word in stripped if word.isalpha()]
    #remove stopwords
    sw=set(stopwords.words('english'))
    #sw.append('subject')
    words=[w for w in words if not w in sw]
    #removing repeated words
    nrwords=sorted(set(words),key=lambda x:words.index(x))
    return nrwords;

def create_word_features(words):
    my_dict = dict( [ (word, True) for word in words] )
    return my_dict
# to give feature to cleaned data

#function for training the classifier
    #cleaning data in enron dataset
def main():
     rootdir="\data"
     ham_list=[]
     spam_list=[]
     ham_words=[]
     spam_words=[]
     for directories,subdirs,files in os.walk(rootdir):
        if (os.path.split(directories)[1]=="ham"):
            for filename in files:
                with open(os.path.join(directories,filename),encoding="latin-1") as f:
                        data=f.read()
                        data=cleaning_data(data)
                        word=' '.join(data)
                        ham_words.append(word)
                        ham_list.append((create_word_features(data),"ham"))
                        
        if (os.path.split(directories)[1]=="spam"):
            for filename in files:
                with open(os.path.join(directories,filename),encoding="latin-1") as f:
                    data=f.read()
                    data=cleaning_data(data)
                    word=' '.join(data)                   
                    spam_words.append(word)
                    spam_list.append((create_word_features(data),"spam"))
     #combining data               
     combined_list=ham_list+spam_list  
     random.shuffle(combined_list)#shuffle combined data
     p=open('pickle/all_list.pickle','wb')
     pickle.dump(combined_list,p)
     p.close()

     d=open('pickle/ham_words.pickle','wb')
     pickle.dump(ham_words,d)
     d.close()
     
     f=open('pickle/spam_words.pickle','wb')
     pickle.dump(spam_words,f)
     f.close()
     
     training_part = int(len(combined_list) * .7)#partition data in 70:30 format
     training_set = combined_list[:training_part]#training data=70%
     test_set =  combined_list[training_part:]#testing data=30%       
   
     f=open('pickle/classifierMB.pickle','wb')
     classifier=SklearnClassifier(MultinomialNB())
     classifier.train(training_set)
     accuracy = nltk.classify.util.accuracy(classifier, test_set)
     print("Accuracy is: ", accuracy * 100)
     pickle.dump(classifier,f)
     f.close()
     return
 


def test_data(data):
    data=cleaning_data(data)
    features=create_word_features(data)
    p=open('pickle/classifierMB.pickle','rb')
    classifier=pickle.load(p)
    m=classifier.classify(features)
    p.close()
    return m 

