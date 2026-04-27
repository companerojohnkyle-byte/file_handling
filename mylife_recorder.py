filename = r"C:\Python Programs\file_handling\My Life txt\mylife.txt"

file = open(filename, "w")

more_lines = "y"

while more_lines == "y":
    line_content = input("Enter line: ")
    file.write(line_content + "\n")
    
    more_lines = input("Are there more lines y/n? ")

file.close()

print("Done writing to file.")