#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 20:20:02 2017

@author: Mohammad Hamza Owais
"""


import numpy as np;

class TransformCsv:
    def __init__(self, file_path):
        self.data = np.genfromtxt(file_path,delimiter=',',dtype='str');
        # key is column number. the values is the array which contains the iterms ut has replaced
        self.columnmapping={}; 
        
        
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        
    def replaceStringWithInt(self):
        dataShape=np.shape(self.data);
        columnsToTranform=[];
        for i in range(dataShape[1]):
            temp=self.data[0][i];
            print(temp)
            if(not self.is_number(temp)):
                columnsToTranform.append(i);
        for column in columnsToTranform:
            uniqueStrings=np.unique(self.data[:,column]);
            for i in range(len(self.data[:,column])):
                string=self.data[i,column];
                num=np.where(uniqueStrings==string)[0][0];
                self.data[i,column]=num;
            self.columnmapping[column]=uniqueStrings;
        
    def intergifyData(self):
        data=self.data;
        self.data=data.astype(np.float);
    
    def shuffleData(self):
        np.random.shuffle(self.data)
    
    def trainGen(self, type):
        if(type==1):
            #this convert the data in to the trainng, validation, testing data in the retion 50:25:25
            self.trainData=self.data[::2,:];
            self.testData=self.data[1::4,:];
            self.validationData=self.data[3::4,:];
            
    def multiClassGen(self,column):
        uniqueValues=np.unique(self.data[:,column]);
        target=np.zeros((np.shape(self.data)[0],np.shape(uniqueValues)[0]));
        for j in  range(np.shape(self.data)[0]):
            currentClass=self.data[j,column];
            num=np.where(uniqueValues==currentClass)[0][0];
            target[j,num]=1;
        self.data=np.concatenate((self.data, target), axis=1);
        #for output morethan 0,1 we use multiclassifation eg. one output for each class
        
            
    