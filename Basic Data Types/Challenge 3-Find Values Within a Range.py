def inRange(x, y):
  if(x<1/3<y):
    return True
  else:
    return False

print(inRange(0, 1))
print(inRange(0.1, 0.3))
print(inRange(0.2, 1.8))
print(inRange(0.5, 1))