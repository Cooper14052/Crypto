import hashlib


def main():
    choose = input('Выбор алгоритма для хеширования: ')
    choose = choose.lower()
    if choose == 'sha256':
        crypt_to_sha256()
    if choose == 'md5':
        crypt_to_md5()


def crypt_to_sha256():
    your_input = input('Введите текст: ')
    algo = hashlib.sha256(your_input.encode())
    print(algo.hexdigest())


def crypt_to_md5():
    your_input = input('Введите текст: ')
    algo = hashlib.md5(your_input.encode())
    print(algo.hexdigest())


if __name__ == '__main__':
    main()
