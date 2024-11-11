def divide(first, second):
    '''При делении на 0 выдает сообщение об ошибке'''

    if second == 0:
        result = "Ошибка!"
    else:
        result = first / second
    return result
