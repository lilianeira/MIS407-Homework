file = open('chatting.txt','r')
count = 1
textFull = file.read()
texts = str(textFull.split(","))
response = ""
message = ""
for i in range(len(texts)):
    if i/2 == 0:
        response1 = texts[i].split("/")
        response.append(response1)
    elif i == 0:
        response1 = texts[i].split("/")
        response.append(response1)
    else:
        response1 = texts[i].split("/")
        message.append(response1)

print (response,message)
