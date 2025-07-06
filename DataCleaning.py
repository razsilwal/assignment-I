# 1. Remove unwanted Space using Strip
# text = "     My name is Raz    "
# cleaned = text.strip() # it help to remove leading and trailing spaces from a string 
# print(f"Before Cleaning: {text}")
# print(f"After Cleaning: {cleaned}")

# 2. Removing Leading Characters using lstrip()
# text = "----My name is Raz"
# cleaned = text.lstrip("-") # it helps to remove all leading dash from the string
# print("Before Cleaning:", text)
# print("After Cleaning:", cleaned)

# # 3. Remove Trailing Characters using rstrip()
# text = "Good Night!!!!!"
# cleaned = text.rstrip("!") # it helps to remove all trailing exclamation mrks(!) fromt the string
# print("Before Cleaning:", text)
# print("After Cleaning:", cleaned)


# # 4. Capitalize a Sentence 
# sentence = "i live in chitwan."
# result = sentence.capitalize() # it helps to capitalize the first letter only.
# print(f"Before: {sentence}")
# print(f"After: {result}") 

# 5. Title Case a Name
# name = "raz silwal"
# result = name.title() # it helps to capitalize ta first letter of each word
# print("Before:", name)
# print("After:", result)

# 6. Clean List of Names
# name = ["   Raz", "Silwal  ", "  Chitwan   "]
# cleaned = [n.strip() for n in name] # It remove all the leading and trailing spaces from each name of a list.
# print("Before Cleaning:", name)
# print("After Cleaning:", cleaned)

# 7. Remove Custom Characters

# text = "##Raz Silwal@@@"
# cleaned = text.strip("#@") # it will remove # and @ from leading and trailing of a string
# print("Before Cleaning:", text)
# print("After Cleaning:", cleaned)


# 8. Capitalize All Name in List
# names = ["raz","krishna","prabesh","mahesh"]
# capitalized = [n.capitalize() for n in names] # it helps to capitalize each name of the list
# print("Before :", names)
# print("After :", capitalized)



# 9. Clean Dictionary Values
# data = {
#     "name":"Raz  ",
#     "city":"Chitwan "
# }
# cleaned = {k: v.rstrip for k, v in data.items()}
# print("Before :", data)
# print("After :", cleaned)

# # 10. Title Case Sentences in List
# sentences = ["welcome to my assignment", "i live in chitwan"]
# result = [s.title() for s in sentences]
# print("Before :", sentences)
# print("After :", result)

# # 11. Clean and Title Case
# text = "   visit bharatpur chitwan   "
# result = text.strip().title() # it helps to remove unwanted spaces and convert it into title case.
# print("Before:", text)
# print("After:", result)

# # 12. Clean List of emails
# emails = ["  raj@gmail.com", "mahesh@yahoo.com  "]
# result = [e.strip() for e in emails]
# print("Before:", emails)
# print("After:", result)


# 13. Remove Leading Numbers

# num_text = "1234506Raz"
# result = num_text.lstrip("0123456789") # it will remove all the number form leading
# print("Before:", num_text)
# print("After:", result)


# 14. Clean Nested List
# nested_list = [["  Apple", "banana  "], ["  mango  "]]
# cleaned = [[item.strip() for item in sublist]for sublist in nested_list]
# print("Before:", nested_list)
# print("After:", cleaned)

# 15. Capitalize After Cleaning
# text = "   raz silwal  "
# result = text.strip().capitalize()
# print("Before:", text)
# print("After:", result)


# 16. Clean Dictionary Keys
# data = {"name_":"Raz", "age_":24}
# cleaned = {k.rstrip("_"): v for k, v in data.items()}
# print("Before:", data)
# print("After:", cleaned)

# 17. Clean and Deduplicate Names
# names = ["  raz", "Krishna  ", " Raz ", "ram ", "krishna"]
# cleaned = list(set(n.strip().capitalize() for n in names)) # it helps to clean, capitalize and delete duplicate name in a list
# print("Before:", names)
# print("After:", cleaned)


# 18. Remove Multiple Characters
# text = "####**Raz*###"
# cleaned = text.strip("#*")
# print("Before:", text)
# print("After:", cleaned)


# 19. Conditional Cleaning in List

# tags = ["#python", "java", "#Golang", "#C"]
# cleaned = [t.lstrip('#') if t.startswith("#") else t for t in tags]
# print("Before:", tags)
# print("After:", cleaned)


# 20. Clean and Group by First Letter
# products = ["  apple", "--Banana", "mango", "banana  "]
# cleaned = [p.strip(" -").capitalize() for p in products]
# grouped = {}
# for p in cleaned:
#     key = p[0].upper()
#     grouped.setdefault(key, []).append(p)
# print("Before:", products)
# print("After:", grouped)

# 21. Clean Set of Strings
# data = {"###raz###", "@@@ramesh@@", "  Rajan   "}
# cleaned = {s.strip("#@ ").capitalize() for s in data}
# print("Before:", data)
# print("After:", cleaned)


# 22. Complex Nested Cleaning 
# data = {"name":["  apple", "ramesh   "], "address":["Bhandara  ", "  Parsa"]}
# cleaned = {k: [v.strip().title() for v in vals] for k, vals in data.items()}
# print("Before:", data)
# print("After:", cleaned)


# 23. Custom Title Funtion 
# def custom_title(s):
#     return ' '.join([w.capitalize() for w in s.split()])
# data = "my name is raz"
# result = custom_title(data)
# print("Before:", data)
# print("After:", result)

# 24. clean and Formats Emails
# emails = ["  RAM@gmail.com", "raj@GMAIL.COM  "]
# cleaned = [e.strip().split("@")[0].capitalize() + "@" + e.strip().split("@")[1].lower() for e in emails]
# print("Before:", emails)
# print("After:", cleaned)


# 25. Multi-Step Cleaning

# data = "12310raz silwal!!!!"
# cleaned = data.lstrip("0123456789").rstrip("!").title()  
# print("Before:", data)
# print("After:", cleaned)


# 26. In-Place Cleaning 

# names = ["   raz", "HARI", "  krishna  "]
# print("Before:", names)
# for i in range(len(names)):
#     names[i] = names[i].strip().title()
# print("After:", names)

# 27. Clean and Count Unique Words
# sentences = ["  hello how are you  ", "hello i am good  "]
# words = set()
# for s in sentences:
#     words.update(s.strip().capitalize().split())
# print("Before:",sentences)
# print("After:", words) 
# print("unique words:", len(words))


# 28. Clean Dictionery Sentences

# data = {"name":"  my name is raz  ", "address":"I live in chitwan"}
# cleaned = {k: v.strip().capitalize() for k, v in data.items()}
# print("Before:", data)
# print("After:", cleaned)


# 29. Select Character Removal 

# text = "#@Raz@#"
# cleaned = text.strip("#@")
# print("Before:", text)
# print("After:", cleaned)


# 30. Batch Clean and Sort

data = [" mango ", "APPLE  ", "banana", "mango2"]
cleaned = sorted([d.strip().title() for d in data])
print("Before:", data)
print("After:", cleaned)