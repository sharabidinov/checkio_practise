def correct_sentence(text: str):
    lst = text.split()
    if lst[-1].endswith('.'):
        return ' '.join(lst).capitalize()
    else:
        lst[-1] = lst[-1] + '.'
        return ' '.join(lst).capitalize()


print(correct_sentence("greetings, friends"))
print(correct_sentence("Greetings, friends."))