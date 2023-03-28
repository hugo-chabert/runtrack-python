def draw_triangle(height):
  for i in range(height-1):
    for j in range(height-i-1):
      print(" ", end="")
    print("/", end="")
    for j in range(i*2):
      print(" ", end="")
    print("\\")
  print("/", end="")
  for i in range(height*2-2):
    print("_", end="")
  print("\\")


draw_triangle(5)