text = "This is new content every time replace the original text"
# writing new content to the file
fp = open(r"C:\Users\USER\ppp\filehandle\info.txt", 'w+')
fp.write(text)
print('Done Writing')
fp.close()