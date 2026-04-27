class MyLifeWriter:
    def __init__(self):
        self.filename = r"C:\Python Programs\file_handling\My Life txt\mylife.txt"

    def write_to_file(self):
        with open(self.filename, "w") as file:
            more_lines = "y"
            
            while more_lines.lower() == "y":
                line_content = input("Enter line: ")
                file.write(line_content + "\n")               
                more_lines = input("Are there more lines y/n? ")
                
        print("\nLines have been saved to mylife.txt successfully!")

writer = MyLifeWriter()
writer.write_to_file()