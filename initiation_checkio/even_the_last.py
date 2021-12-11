def checkio(array: list):
    if len(array) == 0:
        return 0
    else:
        return sum(array[0::2])*array[-1]
