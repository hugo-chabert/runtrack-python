def draw_rectangle(width, height):
    for i in range(height):
      print("|", end="")
      if(i==0 or i==height-1):
        for j in range(width):
          print("-", end="")
      else:
        for j in range(width):
          print(" ", end="")
      print("|")

draw_rectangle(5, 3)