class NumberSorter:
    def __init__(self, input_file):
        self.input_file = input_file
        self.even_file = r"C:\Users\jkcom\OneDrive\PythonCode\even.txt"
        self.odd_file = r"C:\Users\jkcom\OneDrive\PythonCode\odd.txt"

    def process_files(self):
        try:
            with open(self.input_file, 'r') as infile:
                # Use a list comprehension to get all integers
                numbers = [int(line.strip()) for line in infile if line.strip()]

            with open(self.even_file, 'w') as e_out, open(self.odd_file, 'w') as o_out:
                for num in numbers:
                    # 'if' code to check if even or odd
                    if num % 2 == 0:
                        e_out.write(f"{num}\n")
                    else:
                        o_out.write(f"{num}\n")
            
            print(f"Processing complete. Check {self.even_file} and {self.odd_file}.")
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
        except ValueError:
            print("Error: Ensure the file contains only integers.")