import numpy as np
import matplotlib.pyplot as plt
def coeff(x,y):
    n=np.size(x)
    meanx,meany =np.mean(x), np.mean(y)
    ssxy=np.sum(y*x)-n*meanx*meany
    ssxx=np.sum(x*x)-n*meanx*meanx
    b1=ssxy/ssxx
    b0=meany-b1*meanx

    return (b0,b1)
def plot (x,y,b):
    plt.scatter(x,y,color="r",marker="o",s=30)
    ypredicted=b[0]+b[1]*x;
    plt.plot(x,ypredicted,color="b")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()



x=np.array([0,1,2,3,4,5])
y=np.array([[3],[2],[9],[10],[11],[1]])
y1=np.array([3,2,9,10,11,1])
b=coeff(x,y)
print("estimated coeff\nb0={}\nb1={}".format(b[0],b[1]))
plot(x,y1,b)
if __name__=="__main__":
    main()
    
    
