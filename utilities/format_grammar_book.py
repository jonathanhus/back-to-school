# Script to summarize a grammar book
# Grammar book is chunked into sections and then uses GPT
# to summarize each section. The summarized sections are then 
# concatenated into a single summarized grammar book.
# Input files:
#   - grammar_book_cleanup.txt: original grammar book (some material like cover
#                               page and table of contents have been removed)
#   - toc.txt: listing of grammar book sections. Taken from original grammar book
#              table of contents. Section numbers and headings were manually fixed
#              so that toc.txt matches full grammar book

from os import path
from openai import OpenAI
from tqdm import tqdm

language = 'ibatan'
grammar_dir = '../resources/'

grammar_book_file = path.join(grammar_dir, language, 'grammar_book_cleanup.txt')
grammar_book_toc = path.join(grammar_dir, language, 'toc.txt')

with open(grammar_book_file) as f:
    grammar_book = f.read()
    print(f'book size: {len(grammar_book)}')

# Get indices of the grammar book, using the table of contents
def get_section_indices():
    with open(grammar_book_toc) as f:
        toc = [line.rstrip() for line in f]

    prev = 0
    section_indices = []
    for section in toc:
        # print(section)
        idx = grammar_book.find(section)
        # print(f'{idx}: {section}')
        # Check that section was found
        if idx == -1:
            print(section)
        # Check that sections are in order
        if idx < prev:
            print(f'Section: {section}')
        prev = idx
        section_indices.append(idx)

    assert len(section_indices) == len(toc)
    return section_indices

# Split grammar book into sections
def split_book_into_sections():
    book_indices = get_section_indices()
    sections = []
    for i in range(len(book_indices) - 1):
        excerpt = grammar_book[book_indices[i]:book_indices[i+1]]
        sections.append(excerpt)
    # Append last section
    sections.append(grammar_book[book_indices[-1]:])
    return sections

def summarize_grammar(text):
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant, skilled in language translation."},
                {"role": "user", "content": f"""I want to summarize a full length 
                grammar book to assist with translation of a low-resource language.
                I will provide you with the sections to summarize. You will be asked
                to do the translations and the grammar summaries will be provided to you
                to assist with the translations. It is important that you keep information
                that is necessary to translate between English and the low-resource language.
                The grammar book was digitized using OCR, so there may be errors from that 
                process. Do not ask for additional information. Please summarize the
                following text, keeping only the information necessary to assist
                you with the translation: {text}"""}
            ],
            max_tokens=500  # Max length of summary
        )
        return response.choices[0].message.content
    except Exception as err:
        return f"EXCEPTION on section {text[0:20]} : {repr(err)}"


# Summarize each section
sections = split_book_into_sections()
summaries = [summarize_grammar(section) for section in tqdm(sections, desc="Summarizing sections")]

# Write the summaries to a new file
grammar_book_summary_file = path.join(grammar_dir, language, 'summarized_grammar_book.txt')
with open(grammar_book_summary_file, 'w') as summary_file:
    for summary in summaries:
        summary_file.write(summary + "\n\n")

print("Done")