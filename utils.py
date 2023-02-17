import tensorflow as tf
import random
import numpy as np
def TrainTestValSplit(X,Y,testRate,ValRate):
    assert testRate+ValRate<1.
    testsize=int(X.shape[0]*testRate)
    valsize=int(X.shape[0]*ValRate)
    maxLength=X.shape[0]
    totalIndexes=list(range(maxLength))
    Xtrain=[]
    Ytrain=[]
    Xtest=[]
    Ytest=[]
    Xval=[]
    Yval=[]
    while len(Xtest)!=testsize:
        ind=random.choice(totalIndexes)
        Xtest.append(X[ind])
        Ytest.append(Y[ind])
        totalIndexes.remove(ind)
    while len(Xval)!=valsize:
        ind=random.choice(totalIndexes)
        Xval.append(X[ind])
        Yval.append(Y[ind])
        totalIndexes.remove(ind)
    for ind in totalIndexes:
        Xtrain.append(X[ind])
        Ytrain.append(Y[ind])
    Xtrain=np.array(Xtrain)
    Xtrain=tf.constant(Xtrain)
    Ytrain=np.array(Ytrain)
    Ytrain=tf.constant(Ytrain)
    Xtest=np.array(Xtest)
    Xtest=tf.constant(Xtest)
    Ytest=np.array(Ytest)
    Ytest=tf.constant(Ytest)
    Xval=np.array(Xval)
    Xval=tf.constant(Xval)
    Yval=np.array(Yval)
    Yval=tf.constant(Yval)
    return Xtrain,Ytrain,Xval,Yval,Xtest,Ytest
