import base64

def rot10(s) -> str:
    s = s.lower()
    return "".join(chr((ord(c) - ord("a") + 10) % 26 + ord("a")) if c.isalpha() else c for c in s)

def b64(s) -> str:
    return base64.b64decode(s).decode()

def ascii(s) -> str:
    return "".join(chr(int(c)) for c in s.split())

def nato_alphabet(s) -> str:
    decoded = ""
    for word in s.split(" "):
        if "." in word:
            continue
        decoded += word[0]
    return decoded

def leet(s) -> str:
    return s.translate(str.maketrans("0647135", "OGATLES"))

def atbash(s) -> str:
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))

from string import ascii_uppercase
from itertools import product
from re import findall

def uniq(seq):
    seen = {}
    return [seen.setdefault(x, x) for x in seq if x not in seen]

def partition(seq, n):
    return [seq[i : i + n] for i in range(0, len(seq), n)]


# https://rosettacode.org/wiki/Playfair_cipher#Python (translated to python3)
def _playfair(key, from_ = 'J', to = None):
    if to is None:
        to = 'I' if from_ == 'J' else ''

    def canonicalize(s):
        return "".join(filter(str.isupper, s.upper())).replace(from_, to)

    # Build 5x5 matrix.
    m = partition(uniq(canonicalize(key + ascii_uppercase)), 5)

    # Pregenerate all forward translations.
    enc = {}

    # Map pairs in same row.
    for row in m:
        for i, j in product(range(5), repeat=2):
            if i != j:
                enc[row[i] + row[j]] = row[(i + 1) % 5] + row[(j + 1) % 5]

    # Map pairs in same column.
    for c in zip(*m):
        for i, j in product(range(5), repeat=2):
            if i != j:
                enc[c[i] + c[j]] = c[(i + 1) % 5] + c[(j + 1) % 5]

    # Map pairs with cross-connections.
    for i1, j1, i2, j2 in product(range(5), repeat=4):
        if i1 != i2 and j1 != j2:
            enc[m[i1][j1] + m[i2][j2]] = m[i1][j2] + m[i2][j1]

    # Generate reverse translations.
    dec = dict((v, k) for k, v in enc.items())

    def sub_enc(txt):
        lst = findall(r"(.)(?:(?!\1)(.))?", canonicalize(txt))
        return " ".join(enc[a + (b if b else 'X')] for a, b in lst)

    def sub_dec(encoded):
        return " ".join(dec[p] for p in partition(canonicalize(encoded), 2))

    return sub_enc, sub_dec


def playfair(s: str, key: str = "XZUFWCDIRBKMEGHYVPLASTNOQ") -> str:
    enc, dec = _playfair(key)
    return dec(s)

lines = {
    "Veh jxyi unuhsysu oek mybb xqlu je mhyju jxu fqiimeht yd q iocrebkc.jnj vybu.": rot10,
    "Q29uZ3JhdHVsYXRpb25zIG9uIGRlY29kaW5nIHRoaXMgbGluZSwgdGhlIGZpcnN0IGxldHRlciBpczogaw==": b64,
    "xlmtizgfozgrlmh lm wvxlwrmt gsrh ormv, gsv gsriw ovggvi rh: s": atbash,
    "67 79 78 71 82 65 84 85 76 65 84 73 79 78 83 79 78 68 69 67 79 68 73 78 71 84 72 73 83 76 73 78 69 84 72 69 78 69 88 84 67 72 65 82 65 67 84 69 82 73 83 50": ascii,
    "Charlie Oscar November Golf Romeo Alpha Tango Uniform Lima Alpha Tango India Oscar November Sierra ... Oscar November ... Delta Echo Charlie Oscar Delta India November Golf ... Tango Hotel India Sierra ... Lima India November Echo ... Tango Hotel Echo ... November Echo X-Ray Tango ... Lima Echo Tango Tango Echo Romeo ... India Sierra ... Juliett": nato_alphabet,
    "C0N6r47U14710N5 0N D3C0D1N6 7H15 11N3 7H3 N3X7 13773r 15 F": leet,
    "RSOEBLNZAYNDQOT QT IKITREUM OEBO YEUM, NKG AYTN PGSZNMB RT: K": playfair, # I lost my mind here.
}

for line, solve in lines.items():
    print(solve(line))
