from formulas import rsa_generate_keys,abc

# Функция кодировки RSA с помощью публичных ключей
def rsa_lock(num_text):
    public_key_e = rsa_generate_keys()[0]
    public_key_n = rsa_generate_keys()[1]
    rsa = (num_text ** public_key_e) % public_key_n
    return rsa


# Функция кодировки
def num_codding(file_name):

    # Открываем файл который необходимо закодировать
    file = open(file_name, "r")
    # Считываем информацию находящуюся в файле
    text = file.read()
    file.close()
    print(text)
    # Разбиваем текст по символьно и кладем в список
    text_list = list(text)
    for index in range(len(text_list)):
        for let in range(len(abc)):
            # Проходя по списку символов сначала пресваиваем им значение равное их номеру в алфавите
            # После чего приминяем к полученному числу кодирование RSA
            if text_list[index] == abc[let]:
                text_list[index] = str(rsa_lock(let))
    print(text_list)
    # Записываем результат в файл
    cod_text = " ".join(text_list)
    file = open(file_name, "w")
    file.write(cod_text)
    file.close()
    print("Kодирование завершено!")


def main():
    file_name = input("Введите имя файла кодирования:")
    num_codding(file_name)


main()
