# Script to get counts regarding the words, sentences, and grammar
# book resources for the languages
# Things to count:
#   - Words: in resources directory, count number of translations
#   - Sentences: in splits directory, count number of train and test senetences
#   - Grammar: TBD (maybe size of grammar book)

import json

languages = ['arapaho', 'chokwe', 'chuvash', 'dinka', 'dogri', 'gitksan', 'guarani', 'ilokano', 'kabuverdianu', 'kachin', 'kalamang', 'kimbundu', 'latgalian', 'minangkabau', 'mizo', 'natugu', 'wolof']


# Specify language and output directories
# base_dir = "../resources/" + language + "/"
# output_dir = "../splits/" + language + "/"


def count_sentences(language):
    splits_dir = "../splits/" + language + "/"
    with open(splits_dir + "test_examples_ek.json") as file:
        test_ek = json.load(file)
    with open(splits_dir + "test_examples_ke.json") as file:
        test_ke = json.load(file)
    with open(splits_dir + "train_examples_ek.json") as file:
        train_ek = json.load(file)
    with open(splits_dir + "train_examples_ke.json") as file:
        train_ke = json.load(file)
    assert len(test_ke) == len(test_ek), f"Mismatched test sentences for {language}"
    assert len(train_ke) == len(train_ek), f"Mismatched train sentences for {language}"
    return {'language': language, 'train sentences': len(train_ke), 'test sentences': len(test_ke)}

def count_words(language):
    resources_dir = "../resources/" + language + "/"
    stats = {'language': language}
    try:
        with open(resources_dir + 'wordlist.json') as file:
            dictionary = json.load(file)
            stats['e->k words'] = len(dictionary['ek'])
            stats['k->e words'] = len(dictionary['ke'])
    except FileNotFoundError:
        # print(f"No dictionary for {language}")
        stats['e->k words'] = "None"
        stats['k->e words'] = "None"
    return stats

def count_grammar_book(language):
    resources_dir = "../resources/" + language +"/"
    stats = {'language': language}
    token_count = 0
    try:
        with open(resources_dir + 'grammar_book_for_claude_long.txt') as file:
            for line in file:
                tokens = line.split()
                token_count += len(tokens)
            stats['words'] = token_count
    except FileNotFoundError:
        stats['words'] = "No grammar book"
    return stats

for language in languages:
    print(count_sentences(language))

for language in languages:
    print(count_words(language))

for language in languages:
    print(count_grammar_book(language))
