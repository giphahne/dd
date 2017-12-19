import string 

def load_words(word_file="/usr/share/dict/words"):
    with open(word_file, 'r') as f:
        return set(map(
            lambda x: x.strip(),
            f.readlines()
        ))
    

def base_score_text(reference_words, text):
    text_words = text.split()
    return sum(list(map(
        lambda x: 1 if x.lower() in reference_words else 0,
        (t for t in text_words)
    )))








freqs = {
    "e": 0.12702,
    "t": 0.09056,
    "a": 0.08167,
    "o": 0.07507,
    "i": 0.06966,
    "n": 0.06749,
    "s": 0.06327,
    "h": 0.06094,
    "r": 0.05987,
    "d": 0.04253,
    "l": 0.04025,
    "c": 0.02782,
    "u": 0.02758,
    "m": 0.02406,
    "w": 0.02360,
    "f": 0.02228,
    "g": 0.02015,
    "y": 0.01974,
    "p": 0.01929,
    "b": 0.01492,
    "v": 0.00978,
    "k": 0.00772,
    "j": 0.00153,
    "x": 0.00150,
    "q": 0.00095,
    "z": 0.00074,
}
