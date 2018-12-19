import matplotlib.pyplot as plt
from numpy import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


class SensorAnalysis(object):

    def __init__(self, path, seperator=',', cols=[2, 3, 5, 6, 8, 9, 11, 12, 13, 14, 15, 0]):
        self._path = path
        self.y1, self.z1, self.y2, self.z2, self.y3, self.z3, self.y4, self.z4, self.x5, self.y5, self.z5,self.yz0 = loadtxt(path, delimiter=seperator, usecols=tuple(cols), unpack=True)
        self._total_frames = len(self.y1)
        self._cs = ['b', 'r', 'c', 'm', 'g', 'y', 'k']
        #plt.grid(True, 'both', 'both', linestyle='-.')
        # plt.xlabel([])
        # plt.ylabel([])
        # plt.axis('off')
        # frame = plt.gca()
        # y 轴不可见
        #frame.axes.get_yaxis().set_visible(False)
        # x 轴不可见
        #frame.axes.get_xaxis().set_visible(False)

    def sensor(self, which, ff, tf, step=1):
        if ff < 1:
            ff = 1
        if tf > self._total_frames:
            tf = self._total_frames
        ff = ff - 1
        tf = tf - 1
        if which == 1:
            plt.plot(self.y1[ff:tf:step], self.z1[ff:tf:step], c='b')
            plt.annotate('start', xy=(self.y1[0], self.z1[0]))
        elif which == 2:
            plt.plot(self.y2[ff:tf:step], self.z2[ff:tf:step], c='r')
            plt.annotate('start', xy=(self.y2[0], self.z2[0]))
        elif which == 3:
            plt.plot(self.y3[ff:tf:step], self.z3[ff:tf:step], c='c')
            plt.annotate('start', xy=(self.y3[0], self.z3[0]))
        elif which == 4:
            plt.plot(self.y4[ff:tf:step], self.z4[ff:tf:step], c='y')
            plt.annotate('start', xy=(self.y4[0], self.z4[0]))
        elif which == 5:
            plt.plot(self.y5[ff:tf:step], self.z5[ff:tf:step], c='m', linewidth=5.0, linestyle='--')
            #plt.annotate('start', xy=(self.y5[0], self.z5[0]))
        for i in range(ff, tf, step):
                plt.plot([self.y5[i]], [self.z5[i]], c='k')
        plt.show()

    def drawSinOfZ5(self):
        plt.plot(range(0, len(self.z5)), self.z5, c='g')
        plt.show()

    def drawAccelerate(self):
        keyframes_up = list([i for i in range(1, len(self.z5) - 1) if self.z5[i - 1] > self.z5[i] and self.z5[i + 1] > self.z5[i]])
        keyframes_down = list([i for i in range(1, len(self.z5) - 1) if self.z5[i - 1] < self.z5[i] and self.z5[i + 1] < self.z5[i]])
        num = len(keyframes_down) if len(keyframes_down) < len(keyframes_up) else len(keyframes_up)
        plt.plot(self.y5, self.z5, c='m', linewidth=1.0, linestyle='--')
        for i in range(0, num):
            upframe = keyframes_up[i]
            downframe = keyframes_down[i]
            plt.plot([self.y5[upframe], self.y5[downframe]], [self.z5[upframe], self.z5[downframe]], c='g')

        plt.show()

    def sensor_surface(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
    def sensors(self, ff, tf, step=50):
        seq = 0
        for i in range(ff - 1, tf - 1, step):
            seq += 1
            if seq >= len(self._cs):
                seq = 0
            plt.plot([self.y1[i], self.y2[i], self.y3[i], self.y4[i], self.y5[i]], [self.z1[i], self.z2[i], self.z3[i], self.z4[i], self.z5[i]], c=self._cs[seq], label='')
            #plt.annotate(str(i + 1), xy=(self.y5[i], self.z5[i]))
        plt.plot(self.y5[ff:tf:step], self.z5[ff:tf:step], c='k')
        plt.show()

    def sensors2(self, zhiding):
        seq = 0
        for i in zhiding:
            seq += 1
            if seq >= len(self._cs):
                seq = 0
            plt.plot([self.y1[i], self.y2[i], self.y3[i], self.y4[i], self.y5[i]], [self.z1[i], self.z2[i], self.z3[i], self.z4[i], self.z5[i]], c=self._cs[seq], label=str(i))
            plt.annotate(str(i + 1), xy=(self.y5[i], self.z5[i]))
        plt.show()


if __name__ == '__main__':
    s = SensorAnalysis('./test.csv', seperator='\t')
    #绘制指定sensor的轨迹。参数： sensor(第几个sensor，from帧， to帧，帧间隔）
    #s.sensor(5, 58, 1900, 2)

    #绘制全部sensor的轨迹。参数： sensors(from帧，to帧，间隔）
    #s.sensors(130, 1, -1)

    #s.sensors2([1,5,6,8,])

    #s.drawSinOfZ5()

    s.drawAccelerate()
