# temperatures = [10, 12, 14]
#
# file = open("file.txt", 'w')
#
# file.writelines(temperatures)

temperatures = [10, 12, 14]
file = open("file.txt", 'w')
file.writelines(f"{str(t)}\n" for t in temperatures)
file.close()