import re
text="Hello Sannidhi 123 #hastag. How are you??"
pattern = "H"
split_text=re.split(" ",text)
print(split_text)
if re.findall(pattern,text):
    print ("Found {}".format(pattern))
else:
    print ("Hmm not found {} ".format(pattern))

text = "Ssddd sddd sdd dsds sdsd SDSD.. #hastag 1234"
patterns = ["[^.]+"]
for pat in patterns:
    print (re.findall(pat,text))
    print ('\n')
