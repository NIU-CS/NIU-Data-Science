# 602

L=[]
for i in range(5):
  x = input()
  if x == 'A':
    x = 1
  if x == 'J':
    x = 11
  if x == 'Q':
    x = 12
  if x == 'K':
    x = 613
  L.append(int(x))
print(sum(L))
