from circuit_layer import *
x = circuit("TEST")
aux = resistor(1, "R1")
aux2 = resistor(2, "R2")
aux3 = vSource(5, "V1")
x.add_component(aux3, 'up')
x.add_component(aux2, 'right')
x.add_component(aux, 'down')
x.draw()
