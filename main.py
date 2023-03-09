'''Melissa Mankewich'''

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Exit')
    print()


def encoder(passw):
    res = ''
    for i in passw:
        new_pass = str((int(i)+3) % 10)
        res = res + new_pass
    return res

def decoder(encoded):
        #Added by Ozlem Polat
    decoded = ''
    for i in encoded:
        new_pass = str((int(i) - 3) % 10)
        decoded += new_pass
    return decoded


def main():
    continue1 = True
    while continue1 == True:
        menu()
        option = int(input('Please enter an option:'))
        if option == 1:
            passw = input('Please enter your password to encode:')
            encoded = encoder(passw)
            print('Your password has been encoded and stored!')
            print()
        if option == 2:
            decoded = decoder(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}.')
            print()
        if option == 3:
            continue1 == False

if __name__ == "__main__":
    main()

