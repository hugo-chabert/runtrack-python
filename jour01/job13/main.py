def sorting():
    num_list = []
    for i in range(5):
      num = int(input("Entrez un nombre: "))
      num_list.insert(i, num)
    num_list.sort()
    print(num_list)

sorting()