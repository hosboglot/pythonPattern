import os

def main():
    s = input('Я твою строку на хую вертел: ')
    print('\n'.join([''.join( s[::i % 2 * 2 - 1] ) for i in range(100)]))

if __name__ == '__main__':
    main()
