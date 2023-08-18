meme_dict = {
                "CRINGE": "Garip ya da utandırıcı bir şey",
                "LOL": "Komik bir şeye verilen cevap",
                "IDK": "Bilmiyorum",
                "N/A": "[Not Available]"
                }

while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])

    elif word == "break":
        print("Bye :D")
        break
    
    else:
        print("N/A")
