# mt-hackathon-winter-2024
Resources/tutorials for the BYU MATRIX lab Machine Translation Hackathon for Winter 2024 Semester.

# Preprocessing
## tokenizer.py

Requirements:
```
pip install sentencepiece
```

This python file contains 3 functions related to tokenization of text. To use any of these functions in your scripts, you can simply include the `tokenizer.py` file in the same directory as your script and import the functions like this:

```
from tokenizer import *
```

Or you can simply copy the functions and use them wherever you want!

To train a sentencepiece model using the python api, use the `train_sp_model` function and provide these arguments:
```
path_to_text: Path to the text file.
model_prefix: Prefix of the SentencePiece model file.
vocab_size: Vocabulary size.
character_coverage: Character coverage.
model_type: Model type. Choose from 'unigram', 'bpe', 'char', 'word'.
```

To encode a string of text into sentencepiece units (called pieces), use the `encode_sentence_as_pieces` function and provide these arguments:
```
sp_model_path: Path to the SentencePiece model file.
text: Input text as a string.
```

To decode a python List of sentencepiece pieces, use the `decode_pieces` function and provide these arguments:
```
sp_model_path: Path to the SentencePiece model file.
pieces: List of SentencePieces.
```

## tag_for_multilingual.py
If you are going to be training a multilingual model, the simplest form of this is to add tags representing the target language to every source file line. The `tag_for_multilingual.py` script tags a single input file with a provided token.

Remember to add any tags you use to the user_defined_symbols of your sentecepiece tokenizer when training that.

```
usage: tag_for_multilingual.py [-h] file_in file_out tag_token

Tag each line in a text file with a given token.

positional arguments:
  file_in     Path to the input text file.
  file_out    Path to the output text file. 
  tag_token   Token to add to the beginning of each line. I recommend a <target_language_name> style tag.
```

# opennmt/

Requirements:
```
pip install OpenNMT-py
```

## opennmt/example_train.sh
This bash script is an example of the commands you use to train an OpenNMT model. This script also contains links to the OpenNMT documentation and quickstart guide. You must bulid a vocab before you train, hence there are two lines being ran.

## opennmt/example_inference.sh
This bash script is an example of the command you use to run your model inference on an input text file.

## opennmt/example_config.yaml
This is an example training configuration file. OpenNMT uses YAML for the config and it contains any necessary information needed to fully train a model.



# eda.ipynb
This is simply the notebook I used to do some very basic EDA (Exploratory Data Analysis). It's here if you would like to look at it.
