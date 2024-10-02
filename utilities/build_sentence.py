# Build sentence pairs using dev sets from Flores 200
# Uses dev for train and devtest for test
# Ultimately, I need sentence pairs for the following:
#   - train: provided as examples to the LLM as part of the prompt
#   - test: provided as the translation task to the LLM as part of the prompt 

import json
import random
from pathlib import Path

language = "ibatan"
iso_code = "ivb"

# Specify language and output directories
base_dir = "../resources/" + language + "/"
base_dir = "../resources/" + language + "/split3/"
output_dir = "../splits/" + language + "/"

# These work for most resources
# eng_input_file = "dev.eng_Latn"
# forn_input_file = "dev." + iso_code + "_Latn"
# eng_test_input_file = "devtest.eng_Latn"
# forn_test_input_file = "devtest." + iso_code + "_Latn"

eng_input_file = "train_eng.txt"
forn_input_file = "train_iva.txt"
eng_test_input_file = "test_eng.txt"
forn_test_input_file = "test_iva.txt"


# Names of train and test files
# Same names used for different languages
eng2forn_train_file = "train_examples_ek.json"
eng2forn_test_file = "test_examples_ek.json"
forn2eng_train_file = "train_examples_ke.json"
forn2eng_test_file = "test_examples_ke.json"

# Create training data

with open(base_dir + eng_input_file) as eng, open(base_dir + forn_input_file) as forn:
    eng_sentences = [line.rstrip('\n') for line in eng]
    forn_sentences = [line.rstrip('\n') for line in forn]

assert len(eng_sentences) == len(forn_sentences), "Files don't contain same number of sentences"

# Create English to foreign language parallel sentences
eng2forn_translations = []
for idx in range(len(eng_sentences)):
    eng2forn_translations.append({"original": eng_sentences[idx],
                                 "translation": forn_sentences[idx],
                                 "original_id": idx
                                })
    
# Create foreign language to English parallel sentences
forn2eng_translations = []
for pair in eng2forn_translations:
    forn2eng_translations.append({"original": pair['translation'],
                                 "translation": pair['original'],
                                 "original_id": pair['original_id']
                                 })

eng2forn_translations_train = eng2forn_translations
forn2eng_translations_train = forn2eng_translations

# Create test data

with open(base_dir + eng_test_input_file) as eng, open(base_dir + forn_test_input_file) as forn:
    eng_sentences = [line.rstrip('\n') for line in eng]
    forn_sentences = [line.rstrip('\n') for line in forn]

assert len(eng_sentences) == len(forn_sentences), "Files don't contain same number of sentences"

# Create random ordering of parallel sentences
random.seed(42)
indices = list(range(len(eng_sentences)))
random.shuffle(indices)

# Create English to foreign language parallel sentences
eng2forn_translations = []
for idx in indices:
    eng2forn_translations.append({"original": eng_sentences[idx],
                                 "translation": forn_sentences[idx],
                                 "original_id": idx
                                })
    
# Create foreign language to English parallel sentences
forn2eng_translations = []
for pair in eng2forn_translations:
    forn2eng_translations.append({"original": pair['translation'],
                                 "translation": pair['original'],
                                 "original_id": pair['original_id']
                                 })

# Select 50 examples to use as test set
# Matches number of test examples in MTOB
# Test set has 50 examples
# eng2forn_translations_train = eng2forn_translations[50:]
# eng2forn_translations_test = eng2forn_translations[:50]
# forn2eng_translations_train = forn2eng_translations[50:]
# forn2eng_translations_test = forn2eng_translations[:50]

# Use full set of test examples
if len(eng2forn_translations) > 1012:
    print("That's a lot of test sentences!")
    eng2forn_translations_test = eng2forn_translations[0:1012]
    forn2eng_translations_test = forn2eng_translations[0:1012]
else:
    eng2forn_translations_test = eng2forn_translations
    forn2eng_translations_test = forn2eng_translations

# Modify test sentences to be in the expected format
for example in eng2forn_translations_test:
    example['ground_truth'] = example['translation']
    example['translation'] = "--------------------"

for example in forn2eng_translations_test:
    example['ground_truth'] = example['translation']
    example['translation'] = "--------------------"

# Create output directory if it does not exist
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Write files
with open(output_dir + eng2forn_train_file, 'w') as outfile:
    json_format = json.dumps(eng2forn_translations_train, indent=4, ensure_ascii=False)
    outfile.write(json_format)

with open(output_dir + eng2forn_test_file, 'w') as outfile:
    json_format = json.dumps(eng2forn_translations_test, indent=4, ensure_ascii=False)
    outfile.write(json_format)

with open(output_dir + forn2eng_train_file, 'w') as outfile:
    json_format = json.dumps(forn2eng_translations_train, indent=4, ensure_ascii=False)
    outfile.write(json_format)

with open(output_dir + forn2eng_test_file, 'w') as outfile:
    json_format = json.dumps(forn2eng_translations_test, indent=4, ensure_ascii=False)
    outfile.write(json_format)

print("done")