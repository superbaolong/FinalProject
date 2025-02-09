import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#一个神经元
class OneNeural:
    def __init__(self,weight,bias):
        self.weight = weight
        self.bias = bias

    def f(self,x):
        out=np.dot(self.weight,x)+self.bias
        return sigmoid(out)
weight=np.array([0,1])
bias=4
n=OneNeural(weight,bias)
x=np.array([2,3])
print(n.f(x))
#一个神经网络

class OneNeuralNetwork:
    def __init__(self):
        weight = np.array([0, 1])
        bias = 0
        self.h1=OneNeural(weight,bias)
        self.h2=OneNeural(weight,bias)
        self.o1=OneNeural(weight,bias)

    def f(self,x):
        h1_out=self.h1.f(x)
        h2_out=self.h2.f(x)
        o1_out=self.o1.f(np.array([h1_out,h2_out]))
        return o1_out
network = OneNeuralNetwork()
x = np.array([2, 3])
print(network.f(x))