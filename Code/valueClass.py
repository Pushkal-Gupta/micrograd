class Value:

    def __init__(self,data,_children = (), _op = '',label = ''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda : None
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data = {self.data})"

    #Adding Operations allowed by micrograd
    
    def __add__(self,otherVar):
        otherVar = otherVar if isinstance(otherVar,Value) else Value(otherVar)
        output = Value(self.data + otherVar.data, (self,otherVar),'+')
        
        def _backward():
            self.grad += 1.0 * output.grad
            otherVar.grad += 1.0 * output.grad
        output._backward = _backward

        return output

    def __radd__(self,otherVar): #otherVar + self
        return self + otherVar
    
    def __neg__(self):
        return self * -1

    def __sub__(self,otherVar):
        return self + (-otherVar)

    def __rsub__(self,otherVar): #OtherVar - self
        return otherVar + (-self)
    
    def __mul__(self,otherVar):
        otherVar = otherVar if isinstance(otherVar,Value) else Value(otherVar)
        output = Value(self.data * otherVar.data,(self,otherVar),'*')

        def _backward():
            self.grad += otherVar.data * output.grad
            otherVar.grad += self.data * output.grad  
        output._backward = _backward

        return output

    def __rmul__(self,otherVar):  #OtherVar * self
        return self * otherVar

    def __truediv__(self,otherVar): # self/otherVar
        return self * (otherVar ** -1)

    def __rtruediv__(self,otherVar):  #otherVar/self
        return (self ** -1) * (otherVar)
        
    def tanh(self):
        x = self.data
        t = ((math.exp(2*x)-1)/(math.exp(2*x)+1))
        output = Value(t,(self,),'tanh')
        
        def _backward():
            self.grad += (1 - (t**2)) * output.grad
        output._backward = _backward

        return output

    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), 'ReLU')

        def _backward():
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward

        return out

    def exp(self):
        x = self.data
        output = Value(math.exp(x),(self,),'exp')

        def _backward():
            self.grad += output.data * output.grad # output.data is just math.exp(x)
        output._backward = _backward

        return output

    def __pow__(self,otherVar):
        assert isinstance(otherVar,(int,float)) # Ensuring only int or float powers are given
        output = Value(self.data**otherVar,(self,),f"**{otherVar}")

        def _backward():
            self.grad += otherVar * (self.data ** (otherVar - 1)) * output.grad
        output._backward = _backward

        return output

    def backward(self):
        self.grad = 1.0
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        for node in reversed(topo):
            node._backward()