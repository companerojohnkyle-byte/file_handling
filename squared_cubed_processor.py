class IntegerProcessor:
    def __init__(self):
        self.input_file = r"C:\Python Programs\file_handling\Squared and Cubed Processor\Integers.txt"
        self.squared_file = r"C:\Python Programs\file_handling\Squared and Cubed Processor\squared.txt"
        self.cubed_file = r"C:\Python Programs\file_handling\Squared and Cubed Processor\cubed.txt"

    def process_data(self):
        try:
            with open(self.input_file, "r") as infile:
                numbers = [line.strip() for line in infile if line.strip()]

            with open(self.squared_file, "w") as f_double, open(self.cubed_file, "w") as f_triple:
                for val in numbers:
                    num = int(val)
                    
                    if num % 2 == 0:
                        square = num ** 2
                        f_double.write(f"{square}\n")
                    else:
                        cube = num ** 3
                        f_triple.write(f"{cube}\n")

            print("'squared.txt' and 'cubed.txt' have been updated.")

        except FileNotFoundError:
            print("Error: 'integers.txt' not found in the folder.")
        except ValueError:
            print("Error: The file contains non-numeric characters.")

if __name__ == "__main__":
    app = IntegerProcessor()
    app.process_data()