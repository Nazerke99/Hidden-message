alphabet = "AEIOUYBCDFGHJKLMNPQRSTVWXZ"


def decode(code):
    words = code.split(" ")
    message = ""

    for i in words:
        letters = i.split("-")
        result_word = ""
        for j in letters:
            representation = alphabet[int(j)-1]
            result_word += representation
        message += result_word + " "
    return message


print(decode("22-24-4 20-4-1-9-21 9-3-23-2-20-11-2-9 3-17 1 24-4-4-9 1-17-9 3 3 22-4-4-14 22-12-2 4-17-2 15-2-21-21 "
             "22-20-1-23-2-15-2-9 7-6 1-17-9 22-12-1-22 12-1-21 16-1-9-2 1-15-15 22-12-2 9-3-10-10-2-20-2-17-8-2"))
