integers = r"C:\Python Programs\file_handling\Squared and Cubed Processor\Integers.txt"
odds = r"C:\Python Programs\file_handling\Squared and Cubed Processor\odd.txt"
even = r"C:\Python Programs\file_handling\Squared and Cubed Processor\even.txt"

file_in = open(integers, "r")

file_even = open(even, "w")
file_odd = open(odds, "w")

for line in file_in:
    number = int(line.strip())
    
    if number % 2 == 0:
        result = number * number
        file_even.write(str(result) + "\n")
    else:
        result = number * number * number
        file_odd.write(str(result) + "\n")

file_in.close()
file_even.close()
file_odd.close()
print("Process complete: Files created.")