# Using readlines() 
file1 = open('hi.txt', 'r') 
Lines = file1.readlines() 
  

# Strips the newline character 
for line in Lines: 
    line = line + " yoyo"
    f = open("demofile3.txt", "a")
    f.write(line)

f.close()
