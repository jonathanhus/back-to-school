# Build the wordlist (dictionary) file. 
# Uses output from https://github.com/dylandilu/Panlex-Lexicon-Extractor?tab=readme-ov-file

import os
import json

language = "ibatan"
iso_code = "ivb"

resource_dir = os.path.join('..', 'resources', language)
forn_to_eng_lexicon_file = os.path.join(resource_dir, iso_code + "_eng_lexicon.txt")
eng_to_forn_lexicon_file = os.path.join(resource_dir, "eng_" + iso_code + "_lexicon.txt")


wordlist = dict()
wordlist['ke'] = dict()
wordlist['ek'] = dict()


# Go thru sentences in lexicon file
# Add entries in dict. if one word translates to 
# multiple words, separate each target word with a semicolon ";"

# Add foreign to English
with open(forn_to_eng_lexicon_file) as lex:
    lines = [line.strip() for line in lex]

for translation in lines:
    word_pair = translation.split("\t")
    assert len(word_pair) == 2, "word pairs should be separated by a single tab"
    # Kalamang-to-English has POS and English translation for each word
    # We do not have POS for other languages, so entering empty string to
    # maintain formatting
    if word_pair[0] in wordlist['ke']:
        wordlist['ke'][word_pair[0]][1] = wordlist['ke'][word_pair[0]][1] + "; " + word_pair[1]
    else:
        wordlist['ke'][word_pair[0]] = ["", word_pair[1]]

# Add English to foreign
with open(eng_to_forn_lexicon_file) as lex:
    lines = [line.strip() for line in lex]

for translation in lines:
    word_pair = translation.split("\t")
    assert len(word_pair) == 2, "word pairs should be separated by a single tab"
    if word_pair[0] in wordlist['ek']:
        wordlist['ek'][word_pair[0]] = wordlist['ek'][word_pair[0]] + "; " + word_pair[1]
    else:
        wordlist['ek'][word_pair[0]] = word_pair[1]



# Write files
with open(os.path.join(resource_dir, 'wordlist.json'), 'w') as outfile:
    json_format = json.dumps(wordlist, indent=4, ensure_ascii=False)
    outfile.write(json_format)

