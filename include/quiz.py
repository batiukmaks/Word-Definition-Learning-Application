import random


def start_quiz(words):
    count_correct_answers = 0
    wrong_cards = []
    isExit = False
    while not isExit:
        askWord = random.choice([True, False])
        cards = get_cards_firstcorrect(words)
        correct_card = cards[0]
        random.shuffle(cards)
        ask_word(correct_card, cards) if askWord else ask_translation(
            correct_card, cards)

        answer = get_answer()
        correct_answer = chr(65 + cards.index(correct_card))
        if answer == 'E':
            isExit = True
        elif answer == correct_answer:
            print("Correct!")
            count_correct_answers += 1
        else:
            print(f"Wrong! The answer is {correct_answer}.")
            wrong_cards.append(correct_card)

    print_result(count_correct_answers, wrong_cards)


def get_cards_firstcorrect(words):
    correct_card = random.choice(words)
    while True:
        wrong_card1 = random.choice(words)
        wrong_card2 = random.choice(words)
        if correct_card not in [wrong_card1, wrong_card2] and wrong_card1 != wrong_card2:
            break
    cards = [correct_card, wrong_card1, wrong_card2]
    return cards


def ask_word(correct, answers):
    print(f"\nWord: {correct['Word']}\nTranslation: ", end="")
    for i in range(3):
        print(f"{chr(65 + i)}: {answers[i]['Translation']}", end="    ")
    print()


def ask_translation(correct, answers):
    print(f"\nTranslation: {correct['Translation']}\nWord: ", end="")
    for i in range(3):
        print(f"{chr(65 + i)}: {answers[i]['Word']}", end="    ")
    print()


def get_answer():
    while True:
        answer = input("Answer: ").upper()
        if answer in ['A', 'B', 'C', 'E']:
            return answer


def print_result(count_correct_answers, wrong_cards):
    print('\n\n')
    print(f"You answered correctly {count_correct_answers} times.")
    print(f"You answered wrong {len(wrong_cards)} times.")
    if len(wrong_cards) > 0:
        print('Words you answered wrong:')
        for card in wrong_cards:
            print(f"Word: {card['Word']}\t{card['Translation']}")
