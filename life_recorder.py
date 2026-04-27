<<<<<<< HEAD
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
=======
filename = r"C:\Python Programs\file_handling\My Life txt\mylife.txt"

file = open(filename, "w")

more_lines = "y"

while more_lines == "y":
    line_content = input("Enter line: ")
    file.write(line_content + "\n")
    
    more_lines = input("Are there more lines y/n? ")

file.close()

print("Done writing to file.")
>>>>>>> parent of 53d0346 (This is the final commit  for this program. This program is about writing some line to save to your file by running the code, once the interaction ended -- all the line you've written will be saved in your file.)
