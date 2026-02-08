import random
from micrograd.valueClass import Value

class Neuron:

    def __init__(self,nin): #nin -> (n)umber of (in)puts
        #Creating nin Value objects as weights with random value between  -1 and 1
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]

        #Creating a bias for the neuron
        self.b = Value(random.uniform(-1,1))

    def __call__(self,x):
        # ∑w*x + b
        act = sum((wi*xi for wi,xi in zip(self.w,x)),self.b)
        output = act.tanh()
        return output

    def parameters(self):
        return self.w + [self.b]

class Layer:

    def __init__(self,nin,nout): #nout -> (n)umber of (out)puts
        #Creating nout number of neurons per layer
        self.neurons = [Neuron(nin) for _ in range(nout)]

    def __call__(self,x):
        #Initializing the neurons as done earlier
        outputs = [n(x) for n in self.neurons]
        return outputs[0] if len(outputs)==1 else outputs

    def parameters(self):
        params = []
        for neuron in self.neurons:
            ps = neuron.parameters()
            params.extend(ps)
        return params

class MLP:

    def __init__(self,nin,nouts): #nouts -> number of outputs per layer(is an array)
        #Adding input layer size also
        sz = [nin]+nouts
        
        #Creates layer by layer, taking sizes one by one
        self.layers = [Layer(sz[i],sz[i+1]) for i in range(len(nouts))]

    def __call__(self,x):
        #Calling these layers sequentially
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        params = []
        for layer in self.layers:
            ps = layer.parameters()
            params.extend(ps)
        return params