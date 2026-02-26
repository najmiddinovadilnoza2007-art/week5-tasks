from mypackage.geometry import area_circle, area_rectangle
from mypackage.statistics import average, maximum
print("Circle area (r=5):", area_circle(5))
print("Rectangle area (3x4):", area_rectangle(3, 4))
numbers = [10, 20, 30, 40, 50]
print("Average:", average(numbers))
print("Maximum:", maximum(numbers))