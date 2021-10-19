"""
 Current version 0.05.00
 Date: 2018 FEB 26

	LOG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    20 April 2017

   - version 0.01

    25 April 2017

   - fixing bug with display last day of month in plot title
   - more readable axis labels and texts

    02 May 2017

   - solved problem with fonts
   - automatic comp. star aperture number detection
   - still to do: displaying time on x axis !!! <- done

    15 May 2017

   - now on x axis time in format hh:mm:ss is displayed instead of JD
   - now not reading comparission star measurment from res.3 as
     there were only '0.0's
   - code cleaned!

    26 February 2018 

   - Display date fix


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Program uses LCDB, please be awere to always have last version from
 this url http://www.minorplanet.info/lightcurvedatabase.html


"""
#!/usr/bin/python
#-*- coding: utf-8 -*-


from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from astropy.time import Time
import numpy as np
import os
import datetime as dtm

AsteroidRel, AsteroidInst = [],[]
Star1Rel, Star1Inst = [],[]
Star2Rel, Star2Inst = [],[]
Star3Rel, Star3Inst = [],[]
JD = []

DirList = os.walk('./DATA/').next()[1]
DirList.sort()
print 'Directories list: \n', DirList
Dir=raw_input("Select directory :")
ResList=[f for f in os.listdir(os.getcwd()+'/DATA/'+Dir \
    +'/Pho/') if f.endswith(".2") or f.endswith(".3")]
ResList.sort()
AstName = raw_input('Asteroid Name(<Number> <Name>): ') #Number + name
AstNameNum = AstName.split()[0] #Number of asteroid
AstNameName = AstName.split()[1] #Name of asteroid
#
# Date format
#
mjd_file = open(os.getcwd()+"/DATA/"+Dir+"/Pho/"+ResList[0],"r")
line = mjd_file.readline().split()
Date = Time(float(line[0])+2400000, format='jd').iso
while len(line) != 0:
    last_line = line
    line = mjd_file.readline().split()

endDate = Time(float(last_line[0])+2400000, format='jd').iso
dt = dtm.datetime(int(Date[0:4]),int(Date[5:7]),int(Date[8:10]))
ndt = dt+dtm.timedelta(days=1) #next day after observing, necessary to plot title
pdt = dt+dtm.timedelta(days=-1)
edt = dtm.datetime(int(endDate[0:4]),int(endDate[5:7]),int(endDate[8:10]))

if dt.day == edt.day:
    TitleDate = str(dt.day)+' '+str(dt.strftime("%B"))+' '+str(dt.year)
else:
    if dt.month == ndt.month:
        TitleDate = str(dt.day)+'/'+str(ndt.day)+' '+str(dt.strftime("%B"))+' '+str(dt.year)
    else:
        TitleDate = str(dt.day)+' '+str(dt.strftime("%B"))+'/'+' '+str(ndt.day)+' '+str(ndt.strftime("%B"))+' '+str(dt.year)
mjd_file.close()
#
# Observatory
#
Obser= raw_input('Set observatory: ') #No information in headers??
#
# Reading Aperture size
#
AprtFileName = [f for f in os.listdir(os.getcwd()+'/DATA/'+Dir \
    +'/Pho/') if f.endswith("db_dk_fl.dat")]
print 'reading aperture size from '+ AprtFileName[0]
AprtFile = open(os.getcwd()+'/DATA/'+Dir+'/Pho/'+AprtFileName[0])
AprtLine = AprtFile.readline().split()
AprtSize = round(float(AprtLine[8]),0)
print 'Aperture size is '+ str(AprtSize)+'px'
AprtFile.close()
#
# Reading number of Comp. star aperture
#
AprtNumFile = open(os.getcwd()+"/DATA/"+Dir+"/Pho/"+ResList[1],"r")
line = AprtNumFile.readline().split()
for i in line:
    if i == '0.0':
		ApertureNum = str(line.index(i))
AprtNumFile.close()
#
# Reading from res.2 file
#
res2 = open(os.getcwd()+"/DATA/"+Dir+"/Pho/"+ResList[0],"r")
line = res2.readline().split()
while len(line) != 0:
    JD.append(line[0])
    AsteroidInst.append(line[1])
    Star1Inst.append(line[2])
    Star2Inst.append(line[3])
    Star3Inst.append(line[4])
    line = res2.readline().split()
res2.close()
#
# Reading from res.3 file
#
res3 = open(os.getcwd()+"/DATA/"+Dir+"/Pho/"+ResList[1],"r")
line = res3.readline().split()
if ApertureNum == '2':
    index1, index2 = 3,4
elif ApertNum == '3':
    index1, index2 = 2,4
elif ApertNum == '4':
    index1, index2 = 2,3
while len(line) != 0:
    AsteroidRel.append(line[1])
    Star2Rel.append(line[index1])
    Star3Rel.append(line[index2])
    line = res3.readline().split()
res3.close()
#
# Finding phase in LCDB
#
LCDB = open(os.getcwd()+"/LCDB/LC_DAT_PUB.TXT","r")
line = LCDB.readline()
print 'reading data from '+line[18:62]+'...'
while line[10:10+len(AstNameName)] !=AstNameName:
	line = LCDB.readline()
	if line[10:10+len(AstNameName)]==AstNameName:
		result =1
	elif line=='':
		result=0
		print 'Asteroid not in LCBD'
		break
if result==0:
	PhaseSwitch=raw_input("Couldn't find period of asteroid \
		type it in hours (if isn't known, skip it with \'enter\'):")
else:
	PhaseSwitch=float(line[119:125])
print PhaseSwitch
LCDB.close()
#
# Checking filter
#
CheckFilter=raw_input('Set filter: ') #Different names of filters??
#
# ~~~~~~~~~~~~~~~~ Plotting ~~~~~~~~~~~~~~~~~
#
fig, (ax0,ax1) = plt.subplots(nrows=2, figsize = (12,17))
fig.suptitle(AstName, fontsize=40, fontweight='bold')
xfmt = mdates.DateFormatter('%H:%M:%S')
#
#/~~~~~~calculations~~~~~~/
#
JDF=[float(i)+2400000.5 for i in JD]

Star2RelF=[float(i) for i in Star2Rel]
Star3RelF=[float(i) for i in Star3Rel]
ScaleAsteroid=float(max(AsteroidRel))
ScaleDiff2=ScaleAsteroid-np.mean(Star2RelF)
ScaleDiff3=ScaleAsteroid-np.mean(Star3RelF)
Star2=[i+ScaleDiff2+0.15 for i in Star2RelF]
Star3=[i+ScaleDiff3+0.20 for i in Star3RelF]
sigma2=np.std(Star2)
sigma3=np.std(Star3)
fit2=np.polyfit(np.array(JDF),np.array(Star2),1)
fit3=np.polyfit(np.array(JDF),np.array(Star3),1)
fit3_fn,fit2_fn=np.poly1d(fit3),np.poly1d(fit2)

dates=[Time(i, format='jd').iso for i in JDF]
x_ax=JDF
#
#/~~~End of calculations~~~/
#

#
# upper plot
#
ax0.plot(x_ax,AsteroidInst, 'o',color = 'blue')
ax0.plot(x_ax,Star1Inst, 'x',color = 'black')
ax0.plot(x_ax,Star2Inst, 'x', color = 'black')
ax0.plot(x_ax,Star3Inst, 'x',color = 'black')
if PhaseSwitch != '':
    ax0.set_xlim([x_ax[0]-0.05,x_ax[0]+float(PhaseSwitch)/24.])
ax0.invert_yaxis()
ax0.set_ylabel('Instrumental '+CheckFilter+' Magnitude', fontsize=25)
ax0.set_title(TitleDate+','+Obser, fontsize=30)
ax0.set_xticklabels(x_ax, fontsize = 20)
ax0.xaxis.set_major_formatter(xfmt)
#
#lower plot
#
ax1.plot(x_ax,fit2_fn(JDF),color = 'r')
ax1.plot(x_ax,fit3_fn(JDF),color = 'r')
ax1.plot(x_ax,AsteroidRel, 'o', color = 'blue')
ax1.plot(x_ax,Star2, 'x', color = 'black')
ax1.plot(x_ax,Star3, '*', color = 'black')

if PhaseSwitch != '':
    ax1.set_xlim([x_ax[0]-0.05,x_ax[0]+float(PhaseSwitch)/24.])

ax1.text(x_ax[-1]+0.02, np.mean(Star2),r'$\sigma$'+' = '+str("%.3f" \
    % sigma2), fontsize=18)

ax1.text(x_ax[-1]+0.02, np.mean(Star3),r'$\sigma$'+' = '+str("%.3f" \
    % sigma3), fontsize=18)

ax1.text(0.95,1.05,'aperture radius = '+str(int(AprtSize))+'px', \
    verticalalignment='top', horizontalalignment='right', \
    transform=ax1.transAxes,fontsize=15)

ax1.text(0.05,1.05,'comp. star. amperture no:'+ ApertureNum, \
    verticalalignment='top', horizontalalignment='left', \
    transform=ax1.transAxes,fontsize=15)

ax1.invert_yaxis()
ax1.set_ylabel('Relative '+CheckFilter+' Magnitude',fontsize=25)
ax1.set_xticklabels(x_ax, fontsize = 20)
ax1.xaxis.set_major_formatter(xfmt)
plt.rcParams["mathtext.fontset"] = u"stixsans"
plt.savefig(AstName+str(Date[0:10])+'.png', dpi=300, facecolor='w', \
    edgecolor='w', orientation ='portrait')