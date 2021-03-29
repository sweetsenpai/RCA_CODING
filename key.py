from formulas import rsa_generate_keys, abc


# Функция декодирования
def rsa_key(num_text):
    public_key_n = rsa_generate_keys()[1]
    hidden_key_d = rsa_generate_keys()[2]
    rsa_dec = (num_text ** hidden_key_d) % public_key_n
    return rsa_dec


def text_decoding(file_name):
    # Открываем закодированный файл и передаем шифр в список
    file = open(file_name, "r")
    text = file.read()
    file.close()

    print(text.split())
    text_list = text.split()
    for index in range(len(text_list)):
        # Проходим по элементам списка и к каждому из них приминяем алгоритм расшифровки
        # После чего преобразуем цифры в символы с помощью алфавита
        try:
            dec_symbol = rsa_key(int(text_list[index]))
            dec_symbol = abc[dec_symbol]
            text_list[index] = str(dec_symbol)
        except IndexError:
            continue
    # Записываем результат в файл
    decod_text = "".join(text_list)
    file = open(file_name, "w")
    file.write(decod_text)
    file.close()
    print("Декодирование завершено!")


def main():
    file_name = input("Введите имя файла декодирования:")
    text_decoding(file_name)


if __name__ == '__main__':
    main()
