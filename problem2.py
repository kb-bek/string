

text = "У вас есть строка 'Запуск Ethreum 2 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH"

text2 = text.split(' ')
list = []
for i in text2:
    try:
         list.append(int(i))
    except:
         list.append(i)

for i in list:
    print(type(i))