with open("words.txt", "r") as f:
    output = []
    for word in f.readlines():
        word = word.replace("\n", "")
        if word.startswith("mes"):
            print(word)
            output.append("t " + word)
    # print(output)
