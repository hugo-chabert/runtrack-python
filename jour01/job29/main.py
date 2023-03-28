notes = [50, 31, 22, 73, 64, 25, 96, 77]

def skywalker(notes):
  list = []
  for i in notes:
    if i < 40:
      list.append(i)
    elif i % 5 >= 3:
      list.append(i + 5 - i % 5)
    else:
      list.append(i)
  return list


print(skywalker(notes))