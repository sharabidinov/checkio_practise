def between_markers(text: str, begin: str, end: str):
    index_begin = text.find(begin)
    index_end = text.find(end)
    return text[index_begin + 1:index_end]


if __name__ == '__main__':
    print(between_markers('What is >apple<', '>', '<'))
