import random


def start_learning_wordbyword(words):
    def ask(askWord, card):
        print(f"\nWord: {card['Word']}") if askWord else print(
            f"\nTranslation: {card['Translation']}")

    random.shuffle(words)
    currWordItr = len(words) - 1
    count_answers = 0
    skipped_cards = []
    isExit = False
    while not isExit:
        askWord = random.choice([True, False])
        card = words[currWordItr]
        currWordItr -= 1
        ask(askWord, card)
        inp = get_input(askWord, card)

        if (inp == 'answered'):
            count_answers += 1
        elif inp == 'skipped':
            skipped_cards.append(card)
        elif inp == 'exited':
            isExit = True
        elif currWordItr < 0:
            print(f'You passed through all {len(words)} words!')
            isExit = True

    print_result(count_answers, skipped_cards)


def get_input(askWord, card):
    def show_answer(askedWord, card):
        print(f"Translation: {card['Translation']}") if askedWord else print(
            f"Word: {card['Word']}")
    while True:
        inp = input("Answered or skipped? (A/S): ")
        if inp.strip().lower().startswith('a'):
            show_answer(askWord, card)
            return 'answered'
        elif inp.strip().lower().startswith('s'):
            show_answer(askWord, card)
            return 'skipped'
        elif inp.strip().lower().startswith('e'):
            show_answer(askWord, card)
            return 'exited'


def print_result(count_answers, skipped_cards):
    print('\n\n')
    print(f"You answered {count_answers} times.")
    print(f"You skipped {len(skipped_cards)} times.")
    if len(skipped_cards) > 0:
        print('Words you skipped:')
        for card in skipped_cards:
            print(f"Word: {card['Word']}\t{card['Translation']}")
