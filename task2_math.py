##Style 1: import math
import math
print("Square root of 144 =", math.sqrt(144))
print("Pi times 5 =", math.pi * 5)
print("sin(pi/2) =", math.sin(math.pi / 2))


##Style 2: from math import ...
from math import sqrt, pi, sin
print("Square root of 144 =", sqrt(144))
print("Pi times 5 =", pi * 5)
print("sin(pi/2) =", sin(math.pi / 2))

##Differense: |import math| loads the entire module,you must write math. prefix every time.
##|from math import sqrt, pi, sin| loads only what you need, so you can call sqrt() directly without any prefix.