import csv


def get_words(filename):
    words = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tran = row['Translation / Definition'].encode(
                'cp1251').decode("utf-8", "replace")
            words.append({'Word': row['Word'], 'Translation': tran})

    return words