
from graphviz import Graph
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin'

g = Graph('G', filename='process.gv', engine='dot')
g.node('1', label='1')
g.node('2', label='2')
g.node('3', label='3')
g.node('4', label='4')
g.node('5', label='5')
g.node('6', label='6')
g.node('7', label='7')
g.edge('1', '2')
g.edge('1', '3')
g.edge('2', '4')
g.edge('2', '5')
g.edge('3', '6')
g.edge('3', '7')
g.view()
