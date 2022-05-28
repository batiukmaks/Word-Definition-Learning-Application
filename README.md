# The program to learn words and/or their definitions

## **Description**
This program helps to learn words, saved in a CSV file.
It has two modes:
- Quiz mode
- Learning word by word

### <u>Quiz mode</u>
Program randomly chooses a word (or translation/definition) and 2 wrong answers. Then the program asks you to choose the right translation (or the word accordingly), printing possible answers (A, B and C).
- If your answer is correct, you get a point
- If your answer is wrong, the program saves this word with its translation/definition

If you exit the program, you'll get the summary of your session: number of correct answers, number of wrong answers and the list of words with translations/definitions, answered wrong.

### <u>Learning word by word</u>
Program shuffles all the words and asks you, printing the word (or translation, program chooses randomly) and waiting for your response:
- If you know the answer, type 'A' and wait for the next word.
- If you don't know the answer, type 'S', get the right answer and go further.

If you exit the program or the program has already asked you all the words, you'll see the summary of your session: number of answered questions, number of skipped questions and the list of skipped words with their translations/definitions.

As you see, this learning mode relies on your honesty.

## **Usage**
To start running the program you have to provide the filename.csv in command line
> Example: `python words.py static/wordslist.csv` or `python3 words.py static/wordslist.csv`

## **Inspiration**
My English teacher gave us a coursework task: read at least 30 pages of a book and learn 100 new words from it.
Just learning words by heart is boring. As well, when I learn words by heart in particular order, I'll know them in this order as well, but if someone asks me a word randomly - my chance of failure increases.
That's why I had to change the way of learning new words, so the idea of such a program came to my mind.