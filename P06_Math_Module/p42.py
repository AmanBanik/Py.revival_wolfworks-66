# Demonstrate how direct comparison of floating-point results from math functions can be misleading, and how math.isclose() addresses this.
# Demonstration:

# Consider the tangent of pi/2. 
# Mathematically, tan(pi/2) is undefined (approaches infinity). However, due to floating-point representation, math.tan(math.pi / 2) will yield a very large, but finite, number. 
# If we try to check if cos(pi/2) is exactly zero, it might not be.

import math

# Problematic direct comparison
x = math.pi / 2
cos_x = math.cos(x)
print(f"cos({x}) is: {cos_x}")

if cos_x == 0.0:
    print("Direct comparison: cos(pi/2) is exactly 0.")
else:
    print("Direct comparison: cos(pi/2) is NOT exactly 0 due to floating-point precision.")

print("-" * 30)

# Using math.isclose() for robust comparison
# math.isclose(a, b, rel_tol=relative_tolerance, abs_tol=absolute_tolerance)
if math.isclose(cos_x, 0.0, rel_tol=1e-9, abs_tol=0.0):# max allowed difference rlv to each is0.000000001 and max absolute difference is 0
    print("Using math.isclose(): cos(pi/2) is close enough to 0.")
else:
    print("Using math.isclose(): cos(pi/2) is NOT close enough to 0.")