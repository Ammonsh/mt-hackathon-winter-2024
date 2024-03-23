# Docs: https://opennmt.net/OpenNMT-py/options/train.html
# Quickstart: https://opennmt.net/OpenNMT-py/quickstart.html

# Install: pip install OpenNMT-py

onmt_build_vocab -config example_config.yaml -n_sample 32000 # Change -n_sample to -1 to use all the data to create the vocab. This is recommended if you've used pre-tokenized your data.
onmt_train -config example_config.yaml