file_in = open(r"C:\Python Programs\file_handling\Squared and Cubed Processor\Integers.txt", "r")
file_squared = open(r"C:\Python Programs\file_handling\Squared and Cubed Processor\squared.txt", "w")
file_cubed = open(r"C:\Python Programs\file_handling\Squared and Cubed Processor\cubed.txt", "w")

for line in file_in:
    n = int(line.strip())
    if n % 2 == 0:
        file_squared.write(str(n * n) + "\n")
    else:
        file_cubed.write(str(n * n * n) + "\n")

file_in.close()
file_squared.close()
file_cubed.close()