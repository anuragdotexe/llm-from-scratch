from pathlib import Path
import sentencepiece as spm


INPUT_FILE = Path("data/cleaned/corpus_cleaned.txt")
MODEL_PREFIX = "tokenizer/tokenizer"
VOCAB_SIZE = 3167


def train_tokenizer():
    spm.SentencePieceTrainer.train(
        input=str(INPUT_FILE),
        model_prefix=MODEL_PREFIX,
        vocab_size=VOCAB_SIZE,
        model_type="bpe",
        character_coverage=1.0,
        bos_id=1,
        eos_id=2,
        unk_id=0
    )


if __name__ == "__main__":
    train_tokenizer()
    print("Tokenizer training complete.")