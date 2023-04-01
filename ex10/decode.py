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
        decoded += word[0]
    return decoded

def leet(s) -> str:
    return s.translate(str.maketrans("0647135", "OGATLES"))

def atbash(s) -> str:
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))

def _noop(s) -> str:
    return s

lines = {
    "Veh jxyi unuhsysu oek mybb xqlu je mhyju jxu fqiimeht yd q iocrebkc.jnj vybu.": rot10,
    "Q29uZ3JhdHVsYXRpb25zIG9uIGRlY29kaW5nIHRoaXMgbGluZSwgdGhlIGZpcnN0IGxldHRlciBpczogaw==": b64,
    "xlmtizgfozgrlmh lm wvxlwrmt gsrh ormv, gsv gsriw ovggvi rh: s": atbash,
    "67 79 78 71 82 65 84 85 76 65 84 73 79 78 83 79 78 68 69 67 79 68 73 78 71 84 72 73 83 76 73 78 69 84 72 69 78 69 88 84 67 72 65 82 65 67 84 69 82 73 83 50": ascii,
    "Charlie Oscar November Golf Romeo Alpha Tango Uniform Lima Alpha Tango India Oscar November Sierra ... Oscar November ... Delta Echo Charlie Oscar Delta India November Golf ... Tango Hotel India Sierra ... Lima India November Echo ... Tango Hotel Echo ... November Echo X-Ray Tango ... Lima Echo Tango Tango Echo Romeo ... India Sierra ... Juliett": nato_alphabet,
    "C0N6r47U14710N5 0N D3C0D1N6 7H15 11N3 7H3 N3X7 13773r 15 F": leet,
    "RSOEBLNZAYNDQOT QT IKITREUM OEBO YEUM, NKG AYTN PGSZNMBRT: K": _noop,
}

for line, solve in lines.items():
    print(solve(line))
