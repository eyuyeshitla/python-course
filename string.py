name= "hailemeskel"
print(len(name))

# indexing
print(name[1])
print(name[-1])

# slicing

print(name[1:6])
print(name[:6])
print(name[1:])
print(name[1::2])
print(name[::])
print(name[1::2])
print(name[::-1]) # revesing

# modifing
print("g" + name[1:])

# reptation
print(name * 7)

# membership
print( "haile" in name)
print( "haileuo"  not in name)
print( "haile" in name)
print( "Haile".lower() in name)

# othe methods
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.strip())
print(name.replace( "meskel", "maryam"))
print(name.find("meskel"))
print(name.count("e"))
print(name.startswith("ha"))
print(name.endswith("kel"))

word="my name is eyu"
words= word.split()
print(words)
joined= " " .join (words)

print(name.isalpha())
print("123".isdigit())
print("123eyu".isalnum())

