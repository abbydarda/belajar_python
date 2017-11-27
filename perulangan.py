#contoh penggunaan while loop
count = 0
while count < 10:
    print ("the count is ", count)
    count+=1
print ("good bye")

# contoh penggunaan for sederhana
angka = [1,2,3,4,5]
for x in angka:
    print x

#contoh penggunaan for
buah = ["nanas","apel","mangga"]
for makanan  in buah:
    print ("saya suka makan ",makanan)

# contoh penggunaan nested loop
i = 2
while (i<10):
    j = 2
    while (j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j): print(i, " is prime")
    i = i + 1
print("good bye")
