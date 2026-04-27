class StudentGrades:
    def __init__(self):

        self.filename = r"C:\Python Programs\file_handling\GWA FINDER\student"

    def get_highest(self):
        best_gwa = 5.0 
        best_student = ""

        file = open(self.filename, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            data = line.strip().split(",")
            
            name = data[0]
            gwa = float(data[1])

            if gwa < best_gwa:
                best_gwa = gwa
                best_student = name
                
        print("-----------------------------------------")
        print("The student with the highest GWA is:")
        print(f"Name: {best_student}")
        print(f"GWA: {best_gwa}")
        print("-----------------------------------------")

app = StudentGrades()
app.get_highest()