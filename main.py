file = open('111.txt', encoding='utf-8')
text = file.read()
text_base = []
text_repeat = []
print(text)


while text.find('.,') != -1:
    open_repeat = text.find('.,')
    close_repeat = text.find(',.')
    text_base.append(text[0:open_repeat])
    text_repeat.append(text[(open_repeat + 2):close_repeat])
    text = text[(close_repeat + 2):]
    print(text_base)
    print(text_repeat)
    print(text)

text_base.append(text)
print(text_base)
print(text_repeat)



