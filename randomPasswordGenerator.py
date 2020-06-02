import sys
import random

def main():
    print("Welcome to the random password generator.\n" +
          "Here is your new password:\n")

    name = ('djb', 'dan', 'DJB', 'DAN', 'Djb', 'dJb', 'djB', 'jayson', 'Jayson', 'bauer', 'Bauer')

    numbers = ('10', '23', '99', '1023', '2310', '1230', '3021', '2310', '0231', '102399', '992310', '991023', '231099')

    special_character = ('*', '!', "#", '$', '%', '&')

    noun = ('you', 'me', 'dog', 'cat', 'book', 'block', 'bottle', 'phone', 'case', 'sign', 'candle', 'pencil', 'pen',
            'weed', 'drugs', 'porn', 'list', 'boobs', 'slave', 'blunt', 'whiskey', 'bourbon', 'vodka', 'high', 'rum',
            'bullet', 'gun', 'apache', 'helicopter', 'car', 'engine', 'red', 'blue', 'green', 'purple', 'jack',
            'captiain', 'morgan', 'crowns', 'russe', 'crown', 'royal')


    part1 = random.choice(name)
    part2 = random.choice(numbers)
    part3 = random.choice(special_character)
    part4 = random.choice(noun)

    x = random.randint(1,4)

    if x == 1:
        print("{}{}{}{}".format(part1, part2, part3, part4))
    elif x == 2:
        print("{}{}{}{}".format(part2, part3, part4, part1))
    elif x == 3:
        print("{}{}{}{}".format(part3, part4, part1, part2))
    else:
        print("{}{}{}{}".format(part4, part1, part2, part3))


if __name__ == '__main__':
    main()
