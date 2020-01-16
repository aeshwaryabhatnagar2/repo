name = "Aish"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)
with_name_two = greeting.format("Rolf")
print(with_name_two)

#For longer phrases we can also create longer templates and use them when ever required

longer_phrase = "Hello {}, Today is {}"
print(longer_phrase.format("Rolf", "Monday"))