def main():
    string = input('Input: ')
    twttr(string)

def twttr(string):
    for s in string:
        if s not in ['a', 'e', 'i' ,'o' ,'u' , 'A', 'E', 'I', 'O', 'U']:
            print(s, end='')
    print()

main()