### Download

Use `bash unzip_data.sh` in the utilities directory. This will extract the data and populate this directory.

### Splits

This directory contains `train` and `test` splits for the supported languages. For each language the following files are provided:
- train_examples_ek.json: Parallel sentences translated from English to X, which are used in the prompt
- train_examples_ke.json: Parallel sentences translated from X to English, which are used in the prompt
- test_examples_ek.json: Parallel sentences translated from English to X, which are used for testing
- test_examples_ke.json: Parallel sentences translated from X to English, which are used for testing