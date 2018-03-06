"""
画正方形
https://morvanzhou.github.io/tutorials/data-manipulation/plt/5-1-animation/

A simple example of an animated plot
"""
#utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def Rectangle(x):#极坐标表示正方形，x表示角度θ
    x=x%(2*np.pi)

    if (((x)>7/4*np.pi and x<2*np.pi) or (x>0 and x<1/4*np.pi)):
        return (1/(np.cos(x)))
    elif (x>1/4*np.pi and x<3/4*np.pi):
        return (1/(np.sin(x)))
    elif (x>3/4*np.pi and x<5/4*np.pi):
        return ((-1/np.cos(x)))
    elif (x>5/4*np.pi and x<7/4*np.pi):
        return ((-1/np.sin(x)))
    elif(x==0):
        return 1
    else:
       return math.sqrt(2)

def jiaodu1(x):
    x = x % (2 * np.pi)
    if (x<= np.pi):
        return x
    else:
        return  ((2 * np.pi)-x)
def jiaodu2(x):
    x = x % (2 * np.pi)
    if (x<= np.pi):
        return -x
    else:
        return  x


fig, ax = plt.subplots(num='n卡车m铲车调度结果')
ax.axis([-2, 2, -2, 2])#坐标轴范围



z=np.linspace(0, 2*np.pi, 1000)
plt.plot(list(map(Rectangle,z))*np.cos(z),list(map(Rectangle,z))*np.sin(z))
#画一个正方形框

z=np.linspace(-1/2*np.pi, 1/2*np.pi, 1000)
plt.plot(list(map(Rectangle,z))*np.cos(z)+0.4,list(map(Rectangle,z))*np.sin(z))

z=np.linspace(-1/2*np.pi, 1/2*np.pi, 1000)
plt.plot(list(map(Rectangle,z))*np.cos(z)+0.2,list(map(Rectangle,z))*np.sin(z))

z=np.linspace(1/2*np.pi, 3/2*np.pi, 1000)
plt.plot(list(map(Rectangle,z))*np.cos(z)-0.2,list(map(Rectangle,z))*np.sin(z))

z=np.linspace(1/2*np.pi, 3/2*np.pi, 1000)
plt.plot(list(map(Rectangle,z))*np.cos(z)-0.4,list(map(Rectangle,z))*np.sin(z))

a=[
   -1.2,-1.2,-1.2,
   -0.8,-0.5,-0.2,0,0.3,0.9,
   -0.6, -0.4, 0.2, 0.5, 0.6
   ]
b=[
   -0.9, -0.8,0.95,
   1, 1, 1, 1, 1, 1,
   -1, -1, -1, -1, -1
   ]
plt.scatter(a,b)

#铲车
plt.scatter(1.1,0.5,c = 'r', marker = 's',s=70)
plt.scatter(1.3,-0.5,c = 'r', marker = 's',s=70)


#工作面
a1=[1.1,1.1,1.1]
b1=[0.58,0.73,0.81]
plt.scatter(a1,b1)

a2=[1.3,1.3,1.3]
b2=[-0.83,-0.59,-0.66]
plt.scatter(a2,b2)

# x = np.linspace(0, 0, 1)
# line, = ax.plot(list(map(Rectangle,(x)))*np.sin((x)), list(map(Rectangle,(x)))*np.cos((x)), 'ro')
#
# x2 = np.linspace(0, 0, 1)
# line2, = ax.plot(list(map(Rectangle,(x)))*np.sin((x)), list(map(Rectangle,(x)))*np.cos((x)), 'bs')
plt.text(-1.8, 0.3, u'排土区',
         fontdict={'rotation':90,'size': 16, 'color': 'r'})

plt.text(1.7, 0.3, u'工作面',
         fontdict={'rotation':90,'size': 16, 'color': 'r'})

plt.text(-1.4, -1.3, u'台阶1',
         fontdict={'rotation':90,'size': 16, 'color': 'r'})
plt.text(-1.2, -1.3, u'台阶2',
         fontdict={'rotation':90,'size': 16, 'color': 'r'})
plt.text(1.2, -1.3, u'台阶1',
         fontdict={'rotation':90,'size': 16, 'color': 'r'})
plt.text(1.0, -1.3, u'台阶2',
         fontdict={'rotation':90,'size': 16, 'color': 'r'})


# ax.set_title('n卡车m铲车调度结果')

plt.show()
