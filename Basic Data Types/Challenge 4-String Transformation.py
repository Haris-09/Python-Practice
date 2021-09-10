def getStr(s):
  s = s[0]*3 + s[1]*3 + s[2]*3
  strlen = 9
  return [s, strlen]

print(getStr("abc"))
print(getStr("xyz"))