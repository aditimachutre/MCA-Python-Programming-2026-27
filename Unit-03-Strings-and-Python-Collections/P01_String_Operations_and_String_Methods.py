
s = input("Enter a sentence: ")

print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Remove spaces:", s.strip())

print("Replace:", s.replace("Python", "Java"))

ch = input("Enter character to count: ")
print("Character count:", s.count(ch))

word = input("Enter word to check: ")
print("Starts with:", s.startswith(word))
print("Ends with:", s.endswith(word))

print("Concatenation:", s + " Welcome")
print("Repetition:", s * 2)
print("Membership:", "Python" in s)
