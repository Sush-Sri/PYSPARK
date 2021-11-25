'''f=open('fh_file.txt','r+')
f.write(Good Morning
My name is Sushmita Srivastava.
I am from Fathepur Uttar Pradesh.
I did my graduation from GLA University Mathura and I did my schooling from Maharishi Vidya Mandir School.
I worked on Python during second year.


)

with(open('fh_file.txt','a')) as i:
    i.write("During graduation I also worked on Python")


print(f.tell())
print(f.read(11))
print(f.readlines())
print(f.seekable())
print(f.write("This is all From my side\n"))
print(f.fileno())
print(f.isatty())
print(f.writable())
'''

file1 = open("fh_file.txt", "rt")
data = file1.read()
data = data.replace("Python", "JAVA")
file1.close()
file1 = open("fh_file.txt", "wt")
file1.write(data)
file1.close()

file = open("fh_file.txt", "r")
print(file.read())
file.close()