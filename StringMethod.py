#how to convert string into upper or lowercase 
# string are immutable
a="vansh"
b=a.upper()
print(b)

#how to strip special charectars(only end ke hata sakte hain)
c="!!!!!!vansh!!!!!!!!!"
d=c.rstrip("!")
print(d)

#how to replace a word or charactar in a string
e=c.replace("vansh","yash")
print(e) 

#how to split in multiple strings 
h="vansh is a gOod a Boi"
print(h.split(" ")) 
print(h.capitalize())

#centre
print(h.center)
print(len(h))
print(len(h.center(10)))

#count
print(h.count("a"))
print(h.endswith("Boi"))

#isspace
print(h.isspace)
 
#isalnum 
print(h.isalnum)

#islower 
print(h.islower)

#isalpha
print(h.isalpha)
