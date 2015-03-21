import numpy as np
import matplotlib.pyplot as plt
import math




def hist(data,bins=99):
        hist=np.zeros(bins+1);
        xmin=np.amin(data)
        dx=(np.amax(data)-xmin)/bins;
        for x in data:
                hist[int(math.floor((x-xmin)/dx))]+=1;
        return hist/len(data);
def histRange(data,rangeX,bins=100):
        hist=np.zeros(bins);
        xmin=rangeX[0];
        dx=(rangeX[1]-xmin)/(bins-1);
        data=data[data>rangeX[0]]
        data=data[data<rangeX[1]]
        for x in data:
                hist[int(math.floor((x-xmin)/dx))]+=1;
        return hist

def funkcjaA(data):
        return 2.0*data -1.0;
def funkcjaB(data):
        return data **2.0;
def funkcjaC(data):
        return np.sqrt(data);
def funkcjaD(data):
        return np.log(data);
def funkcjaE(data):
        return np.tan(math.pi/2.0*funkcjaA(data));

data=np.random.rand(10**6);
histogramA=hist(funkcjaA(data));
histogramB=hist(funkcjaB(data));
histogramC=hist(funkcjaC(data));
histogramD=hist(funkcjaD(data));
histogramE=histRange(funkcjaE(data),[-5.0,5.0]);

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6,6))

axes[0,0].bar(np.arange(len(histogramA[:-1])),histogramA[:-1]);
dopasowana=np.zeros(len(histogramA[:-1]))
dopasowana[:]=0.01;
axes[0,0].plot(dopasowana,c='r')

axes[0,1].bar(np.arange(len(histogramB[1:-1])),histogramB[1:-1]);
axes[0,1].plot(-0.01*np.sqrt(np.arange(len(histogramB[1:-1]))),c='r')
axes[0,2].bar(np.arange(len(histogramC[:-1])),histogramC[:-1]);
axes[1,0].bar(np.arange(len(histogramD[:-1])),histogramD[:-1]);
axes[1,1].bar(np.arange(len(histogramE[3:-1])),histogramE[3:-1]);


fig.subplots_adjust(hspace=0.4)
plt.show()


