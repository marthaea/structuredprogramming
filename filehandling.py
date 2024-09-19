#open a file in read mode
with open("functions.txt", "r") as file:
    #read the entire file
    content = file.read()
    print(content)
    
#reading line by line 
with open("functions.txt", "r") as file:
    for line in file:
        print(line.strip())
        
#opening a file in write mode
with open("functions.txt", "w") as file:
    #write some content in file
    file.write("Hello, World!\n")
    file.write("This is a test. ")
    
#appending a file this mode writes a new line at the end of the file
with open("functions.txt", "a") as file:
    file.write("This is an appended line")