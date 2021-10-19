#!/bin/python
#-*- coding: utf-8 -*-

import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

class starlinkResults():
    u"""All operations and storage for STARLINK results"""

    dirPath = os.getcwd()+'/STARLINK/'

    @staticmethod
    def loadResults(path):
        return [i for i in  os.listdir(path) if i.endswith('.3')]

    @staticmethod
    def prepareData(fileList):
        dataDict={}
        for _file in fileList:
            dataDict[_file]=[]
            tempFile = open(starlinkResults.dirPath + '/' + _file)
            line = tempFile.readline().split()
            while len(line) != 0:
                epoch=float(line[0])
                mag=float(line[1])
                dataDict[_file].append((epoch,mag))
                line = tempFile.readline().split()

        return dataDict

class ppResults():
    u"""All operations and storage for photmetrypipeline results"""

    dirPath = os.getcwd()+'/PP/'

    @staticmethod
    def loadResults(path):
        return [i for i in os.listdir(path)]

    @staticmethod
    def prepareData(fileList):
        dataDict={}
        for _file in fileList:
            dataDict[_file]=[]
            tempFile = open(ppResults.dirPath + '/' + _file)
            line = tempFile.readline().split()
            line = tempFile.readline().split()
            while line[0] != '#':
                epoch=float(line[1])
                mag=float(line[2])
                dataDict[_file].append((epoch,mag))
                line = tempFile.readline().split()
                if line[0] == '#': break
        return dataDict

class matchData():

    @staticmethod
    def matchByNames(dataDict):
        resultDict={}
        for fileName in dataDict.keys():
            template, asteroid, obsDate = matchData.lookForSameDate(fileName)
            if len(starlinkPhoto[fileName]) == len(ppPhoto[template]):
                k=[]
                x,y = zip(*starlinkPhoto[fileName])
                l,m = zip(*ppPhoto[template])
                for i in range(0,len(m)):
                    k.append(float(m[i])-float(y[i]))
                avg=np.mean(k)
                k=[element - avg for element in k]
                l=[float(element1)+0.5 for element1 in l]
                resultDict[asteroid+'.'+obsDate] = zip(l,k)
            else:
                pass
        return resultDict

    @staticmethod
    def lookForSameDate(fileName):
        tmp = fileName.split('.')
        nameList = tmp[0].split('_')
        template = nameList[1] + '_' + nameList[2] + '.dat'
        return template, nameList[1], nameList[2]

class nameComposition():

    @staticmethod
    def separate(fileName):
        tmpList = fileName.split('.')
        asteroid, obsDate = tmpList[0], tmpList[1]
        year, month, day = obsDate[0:4], obsDate[4:6], obsDate[6:8]
        return asteroid + ' ' + year + '-' + month + '-' + day

if __name__ == '__main__':
    starlinkData = starlinkResults.loadResults(starlinkResults.dirPath)
    starlinkPhoto = starlinkResults.prepareData(starlinkData)

    ppData = ppResults.loadResults(ppResults.dirPath)
    ppPhoto = ppResults.prepareData(ppData)

    resultDict = matchData.matchByNames(starlinkPhoto)
    nameKeys = [fname for fname in resultDict.keys()]

    fig, ((ax0,ax1),(ax2,ax3),(ax4,ax5)) = plt.subplots(nrows=3, ncols=2, figsize = (12,13))
    xfmt = mdates.DateFormatter('%H:%M')

    x0,y0 = zip(*resultDict[nameKeys[0]])
    fit0=np.polyfit(np.array(x0),np.array(y0),1)
    fit0_fn=np.poly1d(fit0)
    sigma0=np.std(y0)

    x1,y1 = zip(*resultDict[nameKeys[1]])
    fit1=np.polyfit(np.array(x1),np.array(y1),1)
    fit1_fn=np.poly1d(fit1)
    sigma1=np.std(y1)

    x2,y2 = zip(*resultDict[nameKeys[2]])
    fit2=np.polyfit(np.array(x2),np.array(y2),1)
    fit2_fn=np.poly1d(fit2)
    sigma2=np.std(y2)

    x3,y3 = zip(*resultDict[nameKeys[3]])
    fit3=np.polyfit(np.array(x3),np.array(y3),1)
    fit3_fn=np.poly1d(fit3)
    sigma3=np.std(y3)

    x4,y4 = zip(*resultDict[nameKeys[4]])
    fit4=np.polyfit(np.array(x4),np.array(y4),1)
    fit4_fn=np.poly1d(fit4)
    sigma4=np.std(y4)

    x5,y5 = zip(*resultDict[nameKeys[5]])
    fit5=np.polyfit(np.array(x5),np.array(y5),1)
    fit5_fn=np.poly1d(fit5)
    sigma5=np.std(y5)

    ax0.plot(x0,y0,'o')
    ax0.plot(x0,fit0_fn(x0), color = 'r')
    ax0.set_ylim([np.mean(y0)-0.25,np.mean(y0)+0.25])
    ax0.set_title(nameComposition.separate(nameKeys[0]), fontsize = 12)
    ax0.text(x0[0], -0.15 ,r'$\sigma$'+' = '+str("%.3f" \
        % sigma0), fontsize=12)
    ax0.xaxis.set_major_formatter(xfmt)

    ax1.plot(x1,y1,'o')
    ax1.plot(x1,fit1_fn(x1), color = 'r')
    ax1.set_ylim([np.mean(y1)-0.25,np.mean(y1)+0.25])
    ax1.set_title(nameComposition.separate(nameKeys[1]), fontsize = 12)
    ax1.text(x1[0], -0.15 ,r'$\sigma$'+' = '+str("%.3f" \
        % sigma1), fontsize=12)
    ax1.xaxis.set_major_formatter(xfmt)

    ax2.plot(x2,y2,'o')
    ax2.plot(x2,fit2_fn(x2), color = 'r')
    ax2.set_ylim([np.mean(y2)-0.25,np.mean(y2)+0.25])
    ax2.set_title(nameComposition.separate(nameKeys[2]), fontsize = 12)
    ax2.text(x2[0], -0.15 ,r'$\sigma$'+' = '+str("%.3f" \
        % sigma2), fontsize=12)
    ax2.xaxis.set_major_formatter(xfmt)

    ax3.plot(x3,y3,'o')
    ax3.plot(x3,fit3_fn(x3), color = 'r')
    ax3.set_ylim([np.mean(y3)-0.25,np.mean(y3)+0.25])
    ax3.set_title(nameComposition.separate(nameKeys[3]), fontsize = 12)
    ax3.text(x3[0], -0.15 ,r'$\sigma$'+' = '+str("%.3f" \
        % sigma3), fontsize=12)
    ax3.xaxis.set_major_formatter(xfmt)

    ax4.plot(x4,y4,'o')
    ax4.plot(x4,fit4_fn(x4), color = 'r')
    ax4.set_ylim([np.mean(y4)-0.25,np.mean(y4)+0.25])
    ax4.set_title(nameComposition.separate(nameKeys[4]), fontsize = 12)
    ax4.text(x4[0], -0.15 ,r'$\sigma$'+' = '+str("%.3f" \
        % sigma4), fontsize=12)
    ax4.xaxis.set_major_formatter(xfmt)

    ax5.plot(x5,y5,'o')
    ax5.plot(x5,fit5_fn(x5), color = 'r')
    ax5.set_ylim([np.mean(y5)-0.25,np.mean(y5)+0.25])
    ax5.set_title(nameComposition.separate(nameKeys[5]), fontsize = 12)
    ax5.text(x5[0], -0.15 ,r'$\sigma$'+' = '+str("%.3f" \
        % sigma5), fontsize=12)
    ax5.xaxis.set_major_formatter(xfmt)

    fig.text(0.5, 0.03, 'observation epoch (HH:MM)', ha='center',
        va='center', fontsize = 13)
    fig.text(0.05, 0.5, u'normalized difference in photometry result\n using'+
        ' photometrypipeline and STARLINK', ha='center',
        va='center', fontsize = 13, rotation='vertical')
    plt.rcParams["mathtext.fontset"] = u"stixsans"

    plt.savefig('oc.png', dpi=300, facecolor='w', edgecolor='w', orientation ='portrait')
