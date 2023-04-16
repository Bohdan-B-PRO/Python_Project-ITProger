# data = input("Ввидите текст: ")
#
# file = open("Test/text.txt", "a")
#
# file.write(data + "\n")
#
# file.close()

file_1 = open("Test/text.txt","r")

print(file_1.read())

for line in file_1:
    print(line, end="")


file_1.close()





