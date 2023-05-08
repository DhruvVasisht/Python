'''fo=open("foo.txt","r+")
fo.write("Python  \t \n")
fo.write("is Very bad Language ")
str=fo.read(10);
str=fo.readlines(2);
print("string read is ",str,)
fo.close()
with open('foo.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)'''

'''import csv

# Open a new CSV file for writing
with open('my_file.csv', 'w', newline='') as file:
    
    # Create a writer object
    writer = csv.writer(file)
    
    # Write some data to the file
    writer.writerow(['Name', 'Age', 'Gender'])
    writer.writerow(['John', 25, 'Male'])
    writer.writerow(['Jane', 30, 'Female'])'''

import csv

# Open the CSV file for reading
with open('my_file.csv', 'r') as file:
    
    # Create a reader object
    reader = csv.reader(file)
    
    # Loop through each row in the file and print its contents
    for row in reader:
        print(row)



