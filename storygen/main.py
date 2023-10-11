def storygen(text):
    question_words = ["how", "why", "what", "where"]
    capitalize = text.capitalize()
    for words in question_words:
        if text.startswith(words):
            return f"{capitalize}?"
    return f"{capitalize}."

result = []
while True:
    user_input = input("Input a statemnt: ")
    if user_input == "end" or user_input == "":
        break
    else:
        complete_sentence = storygen(user_input)
        result.append(complete_sentence)

func_input = " ".join(result)
print(func_input)