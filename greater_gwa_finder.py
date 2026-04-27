filename = r"C:\Python Programs\file_handling\GWA FINDER\student"

file = open(filename, "r")

best_gwa = 5.0
best_student = ""

for line in file:
    data = line.strip().split(",")
    name = data[0]
    gwa = float(data[1])
    
    if gwa < best_gwa:
        best_gwa = gwa
        best_student = name

file.close()

print("Top Student:", best_student, "GWA:", best_gwa)