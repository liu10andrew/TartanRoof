import string
import sklearn
import numpy as np
from titleParse import *
import os
from sklearn import svm
from sklearn.preprocessing import StandardScaler

#testStringList =  getTitles("test_data" + os.sep + "merged.txt")
#testStringList = getTitles("test.txt")
clf = svm.SVC(gamma = .001)

def extractVectorsFromListOfPosts(postList):
    """This is a function designed to extract an attribute vector out of the text of
    a Craigslist posting. These attribute vectors will be fed to the SciKit Learn
    module to determine the quality of the posting itself."""

    
    def extractVectorFromPost(postText):
        upperCaseText = string.upper(postText)
        count = len(postText)
        whiteCount, letterCount, symbolCount, lowerCaseCount = 0, 0 ,0, 0
        for i in xrange(count):
            if postText[i] in string.whitespace: whiteCount += 1
            elif postText[i] in string.ascii_letters: 
                letterCount += 1
                lowerCaseCount += (1 - (upperCaseText[i] == postText[i]))
            else: symbolCount += 1
            #Python boolean arithmetic casts True to 1 and 0 to False.
            #If a char was lowercase, the count will increase
        upperCaseRatio = 1 - float(lowerCaseCount)/letterCount
        symbolRatio = float(symbolCount)/count
        whiteRatio = float(whiteCount)/count
        return [upperCaseRatio*1000, symbolRatio*1000, whiteRatio*1000]

    result = np.array(map(extractVectorFromPost,postList))
    #print result
    np.set_printoptions(precision=3)
    np.savetxt('long_run.txt',result)
    return result

def writeFile(filename, contents, mode="wt"):
    """This is a function taken from the 15-112 website. It writes
    the string contents to the path defined by the string filename"""
    # wt stands for "write text"
    fout = None
    try:
        fout = open(filename, mode)
        fout.write(contents)
    finally:
        if (fout != None): fout.close()
    return True

def predictScoreForArrayOfVectors(vec_arr):
    for vec in vec_arr:
        print clf.predict(vec)
    return

def getLearningModelFromArray(data_array, scores):
    clf.fit(data_array,np.array(scores))
    return True

scaler = StandardScaler(copy = True)
(scores,titles) = getTitles('output2.txt')
#print scores
vectors = extractVectorsFromListOfPosts(titles)
getLearningModelFromArray(vectors,scores)
(_,testTitles) = getTitles('suhaas.txt')
x = extractVectorsFromListOfPosts(testTitles)
print x
print clf.predict(x)
