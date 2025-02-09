import numpy as np

def sigmoid(x):
    # 我们的激活函数: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))

#Neuron神经元，给一个输入x（1×2的矩阵），得到一个输出y（一个数）
class Neuron:  # 神经元
    def __init__(self, weights, bias):     # 对象元素
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):       #对象方法(方法就是定义在类中的函数)，返回y=f(w×x+b)
        # 加权输入，加入偏置，然后使用激活函数
        total = np.dot(self.weights, inputs) + self.bias  # dot是矩阵乘法运算
        return sigmoid(total)

# y=f(w×x+b)。x是输入，w和b是参数。f(x) = 1 / (1 + e^(-x))
weights = np.array([0, 1])  # w1 = 0, w2 = 1
bias = 4  # b = 4
n = Neuron(weights, bias)     #定义了个对象n
x = np.array([2, 3])  # 输入x
print(n.feedforward(x))  # 输出y=f(w×x+b),0.9990889488055994t(a)

#一个简单的神经网络
class OurNeuralNetwork:
    '''
   神经网络具有：
   -2个输入
   -具有2个神经元（h1、h2）的隐藏层
   -具有1个神经元（o1）的输出层
   每个神经元都有相同的权重和偏差：
   -w=[0,1]
   -b=0
    '''
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0

        # h1,h2,o1都是神经元
        self.h1 = Neuron(weights, bias)    #隐藏层
        self.h2 = Neuron(weights, bias)    #隐藏层
        self.o1 = Neuron(weights, bias)    #输出，o1的输入是h1和h2

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)    #输入x得到h1的输出
        out_h2 = self.h2.feedforward(x)    #输入x得到h2的输出

        # 再把h1和h2的输出作为o1的输入
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))

        return out_o1

    # h1=h2=f(w·x+b)
    # =f(0*2)+(1*3)+0)
    # =f(3)
    # =0.9526

    # o1=f(w·[h1,h2]+b)
    # =f(0*h1)+(1*h2)+0)
    # =f(0.9526)
    # =0.7216

network = OurNeuralNetwork()
x = np.array([2, 3])
print(network.feedforward(x)) # 0.7216325609518421

#损失函数

def mse_loss(y_true, y_pred):      #预设的和真实的值求方差
  # y_true and y_pred are numpy arrays of the same length.
  return ((y_true - y_pred) ** 2).mean()   #.mean()就是求均值

y_true = np.array([1, 0, 0, 1])
y_pred = np.array([0, 0, 0, 0])
print(mse_loss(y_true, y_pred)) # 0.5

#接下来我们的目标就是：最小化神经网络的损失
