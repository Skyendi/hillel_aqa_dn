some_text = input("Pleace enter text: ")
filtered_text = set(some_text)

if len(filtered_text) > 10:
    print(True)
else:
    print(False)
