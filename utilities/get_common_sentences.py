# Finds the common sentences that were attempted for translation for a given
# language and direction
import json
import os

# language = 'dinka'
# direction = 'ek'

# TODO: Add gitksan, natugu when WSG data available
# TODO: Check kalamang
languages = ['chokwe', 'chuvash', 'dinka', 'dogri', 'gitksan', 'guarani', 'ilokano',
             'kabuverdianu', 'kachin', 'kalamang', 'kimbundu', 'latgalian', 'minangkabau',
             'mizo', 'natugu', 'wolof']



directions = ['ek', 'ke']

# method to get a dict that maps All test sentences to experiment sentences
def get_indices_dict(test_dir, test_filename):
    try:
        # Open the sentences split file
        split_dir = f'../splits/{language}/'
        split_file = f'test_examples_{direction}.json'
        with open(split_dir + split_file) as split:
            split_data = json.load(split)
            if 'kalamang' in split_dir:
                split_data = [ex for ex in split_data if 'original' in ex]
        with open(test_dir + test_filename) as f:
            test_data = json.load(f)
        my_dict = dict()
        for test_idx, ex in enumerate(test_data):
            for split_idx, test_ex in enumerate(split_data):
                if test_ex['original'] == ex['source']:
                    my_dict[split_idx] = test_idx
        return my_dict
    except FileNotFoundError as error:
        return None
    
# method to write files with the common sentences
def write_common_output(test_dir, test_filename, common_filename, common_set, dict_map):
    with open(test_dir + test_filename) as f:
        test_data = json.load(f)
    new_output = []
    for i in common_set:
        new_output.append(test_data[dict_map[i]])
    with open(os.path.join(test_dir, common_filename), 'w') as outfile:
        json_format = json.dumps(new_output, indent=4, ensure_ascii=False)
        outfile.write(json_format)
    return len(new_output)

sentence_count = dict()
for language in languages:
    for direction in directions:
        # Open the 4 input files for processing
        file_dir = f'../baselines/outputs/{language}/{direction}/'
        baseline_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05.json'
        w_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2.json'

        # File names are slightly different for the languages where we did not use the dictionaries
        # and are slightly different when we used openai vs azure_openai
        if language in ['chokwe'] and direction in ['ke']:
            baseline_filename = f'{language}_results_test_openai_gpt-4-turbo-preview_temp_0.05.json'
            ws_filename = f'{language}_results_test_openai_gpt-4-turbo-preview_temp_0.05_reference_sentences_2.json'
            wsg_filename = f'{language}_results_test_openai_gpt-4-turbo-preview_temp_0.05_reference_sentences_2_reference_book_passages_1_lcs_book_type_full_long.json'
        elif language in ['kalamang'] and direction in ['ek']:
            w_filename = f'{language}_results_test_openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2.json'
            ws_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2_reference_sentences_2.json'
            wsg_filename = f'{language}_results_test_openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2_reference_sentences_2_reference_book_passages_1_lcs_book_type_full_long.json'
        elif language in ['kalamang'] and direction in ['ke']:
            ws_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2_reference_sentences_2.json'
            wsg_filename = f'{language}_results_test_openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2_reference_sentences_2_reference_book_passages_1_lcs_book_type_full_long.json'
        elif language in ['guarani', 'natugu']:
            ws_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2_reference_sentences_2.json'
            wsg_filename = f'{language}_results_test_openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2_reference_sentences_2_reference_book_passages_1_lcs_book_type_full_long.json'
        elif language in ['gitksan']:
            ws_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_sentences_2.json'
            wsg_filename = f'{language}_results_test_openai_gpt-4-turbo-preview_temp_0.05_reference_sentences_2_reference_book_passages_1_lcs_book_type_full_long.json'
        elif language in ['chokwe', 'dinka', 'dogri', 'kachin', 'kimbundu']:
            ws_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_sentences_2.json'
            wsg_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_sentences_2_reference_book_passages_1_lcs_book_type_full_long.json'
        else:
            ws_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2_reference_sentences_2.json'
            wsg_filename = f'{language}_results_test_azure-openai_gpt-4-turbo-preview_temp_0.05_reference_wordlist_2_reference_sentences_2_reference_book_passages_1_lcs_book_type_full_long.json'


        # Create map of full test split sentences to test experiment sentences
        baseline_dict = get_indices_dict(file_dir, baseline_filename)
        w_dict = get_indices_dict(file_dir, w_filename)
        ws_dict = get_indices_dict(file_dir, ws_filename)
        wsg_dict = get_indices_dict(file_dir, wsg_filename)

        # Get sentences in common among all 4 experiments
        baseline_set = set(baseline_dict.keys())
        ws_set = set(ws_dict.keys())
        wsg_set = set(wsg_dict.keys())

        if w_dict:
            w_set = set(w_dict.keys())
            common_set = set.intersection(baseline_set, w_set, ws_set, wsg_set)
        else:
            common_set = set.intersection(baseline_set, ws_set, wsg_set)

        # Now we have the indices in the test split that are common to the four experiments
        # Get examples for the common indices
        # new_split_data = [split_data[i] for i in sorted(common_set)]

        # Define file names for common outputs
        common_baseline_filename = f'{language}_common.json'
        common_w_filename = f'{language}_common_W.json'
        common_ws_filename = f'{language}_common_WS.json'
        common_wsg_filename = f'{language}_common_WSG.json'

        # Output results with just common sentences
        base_num = write_common_output(file_dir, baseline_filename, common_baseline_filename, common_set, baseline_dict)
        if w_dict:
            w_num = write_common_output(file_dir, w_filename, common_w_filename, common_set, w_dict)
            assert base_num == w_num
        ws_num = write_common_output(file_dir, ws_filename, common_ws_filename, common_set, ws_dict)
        wsg_num = write_common_output(file_dir, wsg_filename, common_wsg_filename, common_set, wsg_dict)
        assert base_num == ws_num
        assert base_num == wsg_num

        print(f'{language}-{direction}: found {base_num} sentences in common')
        sentence_count[language] = dict()
print("Done")