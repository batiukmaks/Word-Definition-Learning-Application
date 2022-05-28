import sys
sys.path.insert(0, 'HERE IS THE PATH/include')
import quiz
import learning
import file_manager


def main():
    # file_in = '100words.csv'
    file_in = get_filename(sys.argv)
    words = file_manager.get_words(file_in)
    choice = str
    while True:
        choice = input("Learning (L), quiz (Q) or exit (E)? ").upper()
        if choice in ['L', 'Q', 'E']:
            break
    if choice == 'L':
        learning.start_learning_wordbyword(words)
    elif choice == 'Q':
        quiz.start_quiz(words)
    elif choice == 'E':
        exit()


def get_filename(arguments):
    if len(arguments) == 2:
        return arguments[1]
    elif len(arguments) < 2:
        print('Too few arguments!')
    else:
        print('Too many arguments!')
    exit()


if __name__ == '__main__':
    main()
