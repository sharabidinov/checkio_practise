def sum_numbers(text: str):
    lst = text.split()
    int_lst = []
    for item in lst:
        if item.isdigit():
            int_lst.append(int(item))
    return sum(int_lst)


print(sum_numbers('This picture is an oil on canvas '
                  'painting by Danish artist Anna '
                  'Petersen between 1845 and 1910 year'))
