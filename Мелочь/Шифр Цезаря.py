def scesar_enscrypt(key, text):
    arr = ['а', 'б', 'в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я',' ']

    key = int(key)
    text = text.lower()
    enscriptedText = []

    i=0
    j=0

    for i in range(len(text)):
        j = 0
        while text[i] != arr[j]:
            j += 1
        if arr[(j + key) % len(arr)] == ' ':
            enscriptedText.append('_')  
        else:
            enscriptedText.append(arr[(j + key) % len(arr)])
    return "".join(enscriptedText)
    
print(scesar_enscrypt(input(f"Введите ключ \n"), input(f"Введите текст. Ь=Ъ, Е=Ё \n")))