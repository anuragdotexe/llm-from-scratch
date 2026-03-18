from pathlib import Path
import re


RAW_DATA_PATH = Path("data/raw/corpus.txt")
CLEANED_DATA_PATH = Path("data/cleaned/corpus_cleaned.txt")


def load_text(file_path: Path) -> str:
    with file_path.open("r", encoding="utf-8") as file:
        return file.read()


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n +", "\n", text)
    return text.strip()


def save_text(file_path: Path, text: str) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as file:
        file.write(text)


def main() -> None:
    raw_text = load_text(RAW_DATA_PATH)
    cleaned_text = clean_text(raw_text)
    save_text(CLEANED_DATA_PATH, cleaned_text)

    print("Cleaning complete.")
    print(f"Raw characters: {len(raw_text)}")
    print(f"Cleaned characters: {len(cleaned_text)}")
    print()
    print("Preview:")
    print(cleaned_text[:500])


if __name__ == "__main__":
    main()