#!/bin/sh

# Script to create dictionaries from Panlex

cd /projects/antonis/antonis/Panlex

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language kea --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language kea --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language ilo --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language ilo --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language min --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language min --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language git --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language git --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language arp --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language arp --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language wol --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language wol --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language ntu --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language ntu --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language dik --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language dik --target_language eng --output_directory ~/

#python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language chv --output_directory ~/
#python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language chv --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language cjk --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language cjk --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language kmb --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language kmb --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language ltg --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language ltg --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language kac --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language kac --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language gug --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language gug --target_language eng --output_directory ~/

python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language eng --target_language lus --output_directory ~/
python /projects/antonis/antonis/Panlex/panlex_extract_lexicon.py --source_language lus --target_language eng --output_directory ~/
