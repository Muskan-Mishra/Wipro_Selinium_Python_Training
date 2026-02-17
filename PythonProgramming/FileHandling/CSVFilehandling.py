import csv
#reading csv file
with open("C://Users//MUSKAN MISHRA//PycharmProjects// Python Advance ProgrammingProject//PythonProgramming//dataformats//data.csv" , "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing to the csv file
with open("C://Users//MUSKAN MISHRA//PycharmProjects// Python Advance ProgrammingProject//PythonProgramming//dataformats//writecsv"
          ".csv" , "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id" , "name" , "marks"])
    writer.writerow([1, "muskan" , 98])
    writer.writerow([2,"riya",65])

#appending the data to csv file
with open("C://Users//MUSKAN MISHRA//PycharmProjects// Python Advance ProgrammingProject//PythonProgramming//dataformats//data.csv" , "a" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3,"vishnu",78])



