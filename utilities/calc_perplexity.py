from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import torch
from tqdm import tqdm
import json

languages = ['chokwe', 'chuvash', 'dinka', 'dogri', 'gitksan', 'guarani', 'ilokano',
             'kabuverdianu', 'kachin', 'kalamang', 'kimbundu', 'latgalian', 'minangkabau',
             'mizo', 'natugu', 'wolof']

language = ['chuvash']

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f'Device: {device}')
model_id = "openai-community/gpt2-large"
model = GPT2LMHeadModel.from_pretrained(model_id).to(device)
tokenizer = GPT2TokenizerFast.from_pretrained(model_id)

max_length = model.config.n_positions
stride = 512

output_data = []
for language in languages:
    filename = f'../resources/{language}/grammar_book_for_claude_long.txt'
    with open(filename) as f:
        book = f.read()
    print(f'{language} : {len(book)}')
    encodings = tokenizer(book, return_tensors="pt")
    seq_len = encodings.input_ids.size(1)

    nlls = []
    prev_end_loc = 0
    for begin_loc in tqdm(range(0, seq_len, stride)):
        end_loc = min(begin_loc + max_length, seq_len)
        trg_len = end_loc - prev_end_loc  # may be different from stride on last loop
        input_ids = encodings.input_ids[:, begin_loc:end_loc].to(device)
        target_ids = input_ids.clone()
        target_ids[:, :-trg_len] = -100

        with torch.no_grad():
            outputs = model(input_ids, labels=target_ids)

            # loss is calculated using CrossEntropyLoss which averages over valid labels
            # N.B. the model only calculates loss over trg_len - 1 labels, because it internally shifts the labels
            # to the left by 1.
            neg_log_likelihood = outputs.loss

        nlls.append(neg_log_likelihood)

        prev_end_loc = end_loc
        if end_loc == seq_len:
            break

    ppl = torch.exp(torch.stack(nlls).mean())
    # print(f'{language} perplexity: {ppl}')
    data = {"language": language, "ppl": ppl.item(), "num_tokens": seq_len, "book_length": len(book)}
    print(data)
    output_data.append(data)

with open('perplex_output.json', 'w') as f:
    f.write(json.dumps(output_data, indent=4))

