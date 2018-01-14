import numpy as np
import matplotlib.pyplot as plt



def p(a1,groupsize1):
    plt.axis([-1, 10, 0, 10])
    plt.ion()

    a=a1

    k=0
    sign=1
    sum=0
    groupsize=groupsize1

    for i in range(len(a)):
        if (k % groupsize == 0):
            b=a[i:i+groupsize]
            x = []
            for _ in range(len(b)):
                x.append(_+sum*groupsize)
            y = b
            # x=np.array(range(i,i+groupsize))
            # y=np.array(a[i:i+groupsize])
            plt.plot(x, y)
            sum+=1

        k+=1;



    # x = range(len(a))
    # y = a
    # # plt.figure()
    # plt.plot(x, y)

    k=0

    for i in range(len(a)):
        y = a[i]
        if (k % groupsize == 0):
            sign+=1
            sign=sign%2

        if(sign==0):
            plt.scatter(i, y)
        else:
            plt.scatter(i, y, c='r', marker='D')

        k+=1;

        # plt.pause(0.05)#暂停0.05秒

    while True:
        plt.pause(0.05)


b=[1,3,2,6,5,4,8,8,7,9]
p(b,3)





# https://codeday.me/bug/20170625/32749.html
# http://blog.csdn.net/u013634684/article/details/49646311
# https://www.cnblogs.com/wei-li/archive/2012/05/23/2506940.html