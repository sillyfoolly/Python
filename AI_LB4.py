import pandas as pd

df = pd.read_csv("gne-release-v1.0.tsv", sep="\t", encoding="utf-8")
headlines = list(df["headline"])

def clean(hdln):
    hdln = hdln.replace("'", "")
    hdln = hdln.replace('"', "")
    hdln = hdln.replace("…", "")
    hdln = hdln.replace("”", "")
    hdln = hdln.replace("`", "")
    hdln = hdln.replace("’", "")
    hdln = hdln.replace("“", "")
    hdln = hdln.replace("(", "")
    hdln = hdln.replace(")", "")
    hdln = hdln.replace("#", "")
    return hdln

headlines = [e.strip() for e in headlines]
headlines = [clean(e) for e in headlines]

from collections import Counter
from nltk import ngrams
from nltk.tokenize import word_tokenize

tokens = []
bigrams = []
trigrams = []

line_length = []

for line in headlines:
    line = line.lower()
    tkns = word_tokenize(line)
    line_length.append(len(tkns))
    tokens.extend(tkns)
    bgrms = list(ngrams(tkns, 2))
    bigrams.extend(bgrms)
    trgms = list(ngrams(tkns, 3))
    trigrams.extend(trgms)

token_freq = Counter(tokens)
bigram_freq = Counter(bigrams)
trigram_freq = Counter(trigrams)

token_total = sum(token_freq.values())
bigram_total = sum(bigram_freq.values())
trigram_total = sum(trigram_freq.values())

token_rel_freq = {k: (v / token_total) + 1 for (k, v) in token_freq.items()}
bigram_rel_freq = {k: (v / bigram_total) + 1 for (k, v) in bigram_freq.items()}
trigram_rel_freq = {k: (v / trigram_total) + 1 for (k, v) in trigram_freq.items()}

import random
def simple_generator(n):
    assert n in [2, 3]
    weights = []
    seed = random.choice(list(tokens))
    if n == 2:
        bgms = {k: v for (k, v) in bigrams if v == seed}
        wds = [e for e in bgms.keys()]
        if wds:
            for elem1 in bigram_rel_freq.keys():
                for elem2, elem3 in bgms.items():
                    if((elem1[0] == elem2) and (elem1[1] == elem3)):
                        weights.append(bigram_rel_freq[elem1])
            return random.choices(population=wds, weights=weights)[0]
        else:
            tokens_A = []
            for elem in token_rel_freq.items():
                weights.append(elem[1])
                tokens_A.append(elem[0])
            return random.choices(population=list(tokens_A), weights=weights)[0]
    elif n == 3:
        tgms = {k: v for (k, v, t) in trigrams if t == seed}
        wds = [e for e in tgms.keys()]
        if wds:
            for elem1 in trigram_rel_freq.keys():
                for elem2, elem3 in tgms.items():
                    if((elem1[0] == elem2) and (elem1[1] == elem3) and (elem1[2] == seed)):
                        weights.append(trigram_rel_freq[elem1])
            return random.choices(population=wds, weights=weights)[0]
        else:
            tokens_A = []
            for elem in token_rel_freq.items():
                weights.append(elem[1])
                tokens_A.append(elem[0])
            return random.choices(population=list(tokens_A), weights=weights)[0]

sentence = []
for i in range(50):
    w = simple_generator(2)
    sentence.append(w)
print("--->>> ", sentence)

sentence = []
for i in range(50):
    w = simple_generator(3)
    sentence.append(w)
print("--->>> ", sentence) 