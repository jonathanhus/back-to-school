<div align="center">    
 
## Back to School: Translation Using Grammar Books

[Back to School](https://arxiv.org/abs/2410.15263)

</div>

### Abstract

Machine translation systems for high resource
languages perform exceptionally well and produce
high quality translations. Unfortunately,
the vast majority of languages lack the quantity
of parallel sentences needed to train such systems.
These under-represented languages are
not entirely without resources, as bilingual dictionaries
and grammar books may be available
as linguistic reference material. With current
large language models (LLMs) supporting near
book-length contexts, we can use the available
material to ensure advancements are shared
among all of the world’s languages. In this
paper, we use dictionaries and grammar books
to improve machine translation. We evaluate
on 16 typologically diverse low-resource languages,
showing encouraging improvements.


### Background

In Machine Translation from One Book ([MTOB](https://arxiv.org/abs/2309.16575)), the authors used linguistic reference material such as a dictionary and a grammar book to prompt a Large Language Model to translate between English and Kalamang. We started with their baseline and expanded upon it to support additional languages.


### Set up

The splits and resources directories store the grammar books, dictionaries, and parallel sentences for the supported languages. This data is provided in the language.zip file.  To extract the data, enter the following commands:
```
cd utilities
bash unzip_data.sh
# when prompted for the password, enter password
```

Note: The authors of MTOB and the maintainers of FLORES+ explicitly request that this reference data, and the parallel sentences in particular, are not publicly hosted as plain text. This is to ensure that the resources are not web-scraped where they could potentially be included in the training data of future models, which would taint results of MT tests. In accordance with their requests, and with the same spirit in mind, we have password encrypted all reference material that we have posted and request that any users of our data do the same.