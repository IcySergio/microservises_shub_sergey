from rapidfuzz.distance import Levenshtein

def match(query: str, corpus: Corpus, threshold: int = 3) -> bool:
    return any(Levenshtein.distance(query, part) <= threshold for part in corpus.content)