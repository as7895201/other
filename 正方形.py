"""
画正方形
https://morvanzhou.github.io/tutorials/data-manipulation/plt/5-1-animation/

A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

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


fig, ax = plt.subplots()
ax.axis([-2, 2, -2, 2])#坐标轴范围

z=np.linspace(0, 2*np.pi, 1000)
plt.plot(list(map(Rectangle,z))*np.cos(z),list(map(Rectangle,z))*np.sin(z))
#画一个正方形框


x = np.linspace(0, 0, 1)
line, = ax.plot(list(map(Rectangle,(x)))*np.sin((x)), list(map(Rectangle,(x)))*np.cos((x)), 'ro')

x2 = np.linspace(0, 0, 1)
line2, = ax.plot(list(map(Rectangle,(x)))*np.sin((x)), list(map(Rectangle,(x)))*np.cos((x)), 'bs')


def animate(i):

    line.set_ydata(list(map(Rectangle,jiaodu1(x + i/10.0)))*np.sin(jiaodu1(x + i/10.0)))
    line.set_xdata(list(map(Rectangle,jiaodu1(x + i/10.0)))*np.cos(jiaodu1(x + i/10.0)))

    line2.set_ydata(list(map(Rectangle,jiaodu2(x2 + i/10.0)))*np.sin(jiaodu2(x2 + i/10.0)))
    line2.set_xdata(list(map(Rectangle,jiaodu2(x2 + i/10.0)))*np.cos(jiaodu2(x2 + i/10.0)))


    return line,line2,



def init():
    line.set_ydata(list(map(Rectangle,(x)))*np.sin((x)))  # update the data
    line.set_xdata(list(map(Rectangle,(x)))*np.cos((x)))

    line2.set_ydata(list(map(Rectangle, (x2))) * np.sin((x2)))  # update the data
    line2.set_xdata(list(map(Rectangle, (x2))) * np.cos((x2)))

    return line,line2,

ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=500,
                              init_func=init,
                              interval=100,
                              blit=True)


# fig 进行动画绘制的figure
# func 自定义动画函数，即传入刚定义的函数animate
# frames 动画长度，一次循环包含的帧数
# init_func 自定义开始帧，即传入刚定义的函数init
# interval 更新频率，以ms计
# blit 选择更新所有点，还是仅更新产生变化的点。应选择True，但mac用户请选择False，否则无法显示动画
plt.show()