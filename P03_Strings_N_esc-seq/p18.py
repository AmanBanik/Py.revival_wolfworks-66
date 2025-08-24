letter='''Dear <|NAME|>
You are selected!
<|DATE|>'''
print(letter)
print(letter.replace('<|NAME|>', 'Aman').replace('<|DATE|>', '7th July 2025'))#nested replace

txt="Hello my  name is  Aman"
print("Dettect doubble space affearence first index at:",txt.find("  "))
print("Replacing double space with single space:",txt.replace("  "," "))
tax="Dear Harry,\n\tThis Python course is nice.\nThanks!"
print(tax)