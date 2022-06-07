import os
from itertools import accumulate

def char_per_word(words):
    return [*map(lambda w: len(w)+1, words)]

def word_count(counts:list):
    return accumulate(counts, lambda x, y: x + y if x + y <= 280 else y)
    
def zip_counts(counts:list, accum:iter):
    return zip(counts, accum)

def slices_idx(pairs:zip):
    edges = [*filter(lambda p: p[0] == p[1], pairs)] + [-1]
    return [slice(edges[n], edges[n+1]) for n in range(len(edges)-1)]
    
def slice_text(words, slices:list):
    return [words[s] for s in slices]


class TextManipulation:
    def __init__(self, in_path:str, out_path:str):
        self.in_path = in_path
        self.out_path = out_path

    def read_text(self):
        with open(self.in_path, 'r') as txt:
            all_text = txt.read().replace('\n', '')
        return all_text.split(' ')

    def process_text(self, itr):
        w1 = char_per_word(itr)
        w2 = word_count(w1)
        w3 = zip_counts(w1, w2)
        w4 = slices_idx(w3)
        return slice_text(itr, w4)

    def save_text(self, itr):
        with open(self.out_path, 'w') as txt:
            for i in itr:
                txt.write(i.join(''))
                txt.write("\n\n")

if __name__ == '__main__':
    txt = "../tests/input_text.txt"
    result = "../tests/output_text.txt"

    xt = ExtractText(txt, result)
    chunks = xt.read_text()
    xt.save_text(chunks)
