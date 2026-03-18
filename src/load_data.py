from pathlib import Path


DATA_PATH = Path("data/raw/corpus.txt")


def load_corpus(file_path: Path) -> str:
    with file_path.open("r", encoding="utf-8") as file:
        text = file.read()
    return text


def main() -> None:
    text = load_corpus(DATA_PATH)

    print("Corpus loaded successfully.")
    print(f"Total characters: {len(text)}")
    print()
    print("Preview:")
    print(text[:500])


if __name__ == "__main__":
    main()