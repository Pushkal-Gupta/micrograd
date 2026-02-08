from Code.valueClass import Value
from Visualize.visualizeGraph import draw_dot
import os

x1 = Value(2.0, label='x1')
x2 = Value(0.0, label='x2')

w1 = Value(-3.0, label='w1')
w2 = Value(1.0, label='w2')
b  = Value(6.881373587, label='b')

n = x1*w1 + x2*w2 + b
o = n.tanh()
o.label = "o"

o.backward()

# --- render graph inside Visualize folder ---
output_path = os.path.join("Visualize", "computation_graph")

dot = draw_dot(o)
dot.render(output_path, view=True)