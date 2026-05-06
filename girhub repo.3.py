#Adding bullet points to wiki file....

import pyperclip
text = pyperclip.paste()
text = '* ' + text.replace('\n','\n*')
pyperclip.copy(text)
print(text)
