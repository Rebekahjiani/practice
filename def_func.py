import math

def quadratic(a, b, c):
    if a == 0:
        return None
    else:
        x = b**2 - 4*a*c
        if x < 0:
            return None
        else:
            y = -b + math.sqrt(x)
            z = -b - math.sqrt(x)
            m = 2*a
            x1 = y / m
            x2 = z / m
            return x1,x2

# 测试：
print('quadratic(2, 3, 1) = ', quadratic(2,3,1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))