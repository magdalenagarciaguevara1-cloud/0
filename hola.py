meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("Significado:", meme_dict[word])
else:
    print("Lo siento, esa palabra no está en nuestro diccionario todavía.")
