a = 711
b = 67
c = 69
print(f"first stage: a = {a}, b = {b}, c = {c}")
a, b, c = c, a, b
print(f"2nd stage: a = {a}, b = {b}, c = {c}")