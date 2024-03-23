import os
import sentencepiece as spm

def train_sp_model(path_to_text, model_prefix, vocab_size, character_coverage, model_type, user_defined_symbols=None):
    '''
    Train a SentencePiece model on the given text lines.

    Args:
        path_to_text: Path to the text file.
        model_prefix: Prefix of the SentencePiece model file.
        vocab_size: Vocabulary size.
        character_coverage: Character coverage.
        model_type: Model type. Choose from 'unigram', 'bpe', 'char', 'word'.

    Returns:
        The path to the trained SentencePiece model file.
    '''
    # Validate input arguments
    try:
        assert isinstance(path_to_text, str) and os.path.exists(path_to_text)
    except AssertionError:
        print(f'Invalid path to text file: {path_to_text}')
        return
    try:
        assert isinstance(model_prefix, str)
    except AssertionError:
        print('Invalid model prefix.')
        return
    try:
        assert isinstance(vocab_size, int) and vocab_size > 0 and vocab_size <= 512000
    except AssertionError:
        print('Invalid vocabulary size.')
        return
    try:
        assert isinstance(character_coverage, float) and character_coverage > 0.0 and character_coverage <= 1.0
    except AssertionError:
        print('Invalid character coverage. Please provide a float between 0.0 and 1.0.')
        return
    try:
        assert model_type in ['unigram', 'bpe', 'char', 'word']
    except AssertionError:
        print('Invalid model type. Choose from "unigram", "bpe", "char", "word".')
        return

    # Begin training the SentencePiece model
    print('Training SentencePiece model...')

    if user_defined_symbols is not None:
        try:
            assert isinstance(user_defined_symbols, list)
        except AssertionError:
            print('Invalid user-defined tokens. Please provide a list of strings.')
            return

        print(f"Found user-defined tokens: {user_defined_symbols}")

        spm.SentencePieceTrainer.train(' '.join([
            f'--input={path_to_text}',
            f'--model_prefix={model_prefix}',
            f'--vocab_size={vocab_size}',
            f'--character_coverage={character_coverage}',
            f'--model_type={model_type}',
            f'--user_defined_symbols={",".join(user_defined_symbols)}'
        ]))
    else:
        spm.SentencePieceTrainer.train(' '.join([
            f'--input={path_to_text}',
            f'--model_prefix={model_prefix}',
            f'--vocab_size={vocab_size}',
            f'--character_coverage={character_coverage}',
            f'--model_type={model_type}'
        ]))

def encode_sentence_as_pieces(sp_model_path, text):
    '''
    Tokenize the given text into SentencePieces.

    Args:
        sp_model_path: Path to the SentencePiece model file.
        text: Input text as a string.

    Returns:
        List of SentencePieces.
    '''
    return spm.SentencePieceProcessor(model_file=sp_model_path).encode_as_pieces(text)

def decode_pieces(sp_model_path, pieces):
    '''
    Decode SentencePieces into text.

    Args:
        sp_model_path: Path to the SentencePiece model file.
        pieces: List of SentencePieces.

    Returns:
        Decoded text.
    '''
    return spm.SentencePieceProcessor(model_file=sp_model_path).decode_pieces(pieces)

def testing():
    path_to_text = '/Users/ammonshurtz/byu/machine-translation-lab/hackathon-winter-24/americasnlp2024/ST1_MachineTranslation/data/aymara-spanish/train.es'
    model_prefix = 'spanish_bpe'
    vocab_size = 4096
    character_coverage = 1.0
    model_type = 'bpe'
    train_sp_model(path_to_text, model_prefix, vocab_size, character_coverage, model_type)

    sp_model_path = 'spanish_bpe.model'
    text = 'Hola, ¿cómo estás?\nEstoy bien, gracias.\n¡Hasta luego!\n'

    pieces = encode_sentence_as_pieces(sp_model_path, text)
    print(pieces)

    decoded_text = decode_pieces(sp_model_path, pieces)
    print(decoded_text)

if __name__ == '__main__':
    testing()