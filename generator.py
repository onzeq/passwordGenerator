import argparse  
from random import randint

parser = argparse.ArgumentParser(description='Options for password')
parser.add_argument('--spec_char', type=str)
args = parser.parse_args()


class generator:
    def __init__(self,) -> None:
        self.char_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
        self.spec_string = '!$%&?#@!'

    
    def finalString(self, string:str = None):
        if string == None:
            self.char_string += self.spec_string*5
        else: self.char_string += string

    
    def generate(self, pw_size:int = 25):
        password = ''
        length: int = len(self.char_string)
        for i in range(pw_size):
            password += self.char_string[randint(0,length-1)]
        
        return password


def main():
    gen = generator()

    if args.spec_char:
        gen.finalString(args.spec_char)
        
    else: gen.finalString()

    print('Generated password: ' + gen.generate())



if __name__ == '__main__':
    
    main()
