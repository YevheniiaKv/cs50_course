name = input("Name: ")
#print("Hello, " + name)
# print(f"Hello, {name}")

lastname = input("Last name: ")
print("Hello, " + name + lastname) #тут не буде пробілу між імʼям та прізвищем, щоб це виправити, краще використати f-рядок або поставити кому перед name та lastname

print(f"Hello, {name}")
print(f"Hello, {name} {lastname}!")