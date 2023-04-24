array = [1, 5, 7, 3, 9, 2, 8]
k = 5
count = 0
summa = 0
for elem in array:
    if elem > k:
        count += 1  #
        summa += elem
        print("Количество элементов, больших", k, ":", count)
        print("Их сумма:", summa)