MODEL_PATH=path_to_model.pt # .pt file
SRC_PATH=my_src.es
PRED_PATH=my_tgt.aym

onmt_translate -model $MODEL_PATH -src $SRC_PATH -output $PRED_PATH -verbose