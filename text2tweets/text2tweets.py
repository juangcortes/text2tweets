import os
from itertools import accumulate

def char_per_word(words:list):
    """Gets a list with strings, returns another list with character counts
    plus one."""
    return [len(w)+1 for w in words]

def word_count(counts:list):
    """Gets a list with character counts from char_per_word, returns a list 
    with the accumulated sum if the character count is equal or less to
    140 or the original number."""
    return [*accumulate(counts, lambda x, y: x + y if x + y <= 140 else y)]

def slices_idx(wc:list):
    """Get the accumulated counts list from word_count, returns slices with
    140 characters or less."""
    end_word = [0]
    pairs = [(wc[n], wc[n+1]) for n in range(len(wc)-1)]
    for idx, pair in enumerate(pairs):
        prv, nxt = pair
        if prv>nxt:
            end_word.append(idx+1)
    end_word.append(-1)
    return [slice(end_word[n], end_word[n+1]) for n in range(len(end_word)-1)]

def slice_text(words, slices:list):
    """Takes the read text and the slices created in slices_idx, returns a
    generator with sliced texts."""
    for s in slices:
        yield words[s] 

class TextManipulation:
    def __init__(self, in_path:str, out_path:str):
        self.in_path = in_path
        self.out_path = out_path
        self._text = None

    def read_text(self):
        with open(self.in_path, 'r') as txt:
            self._text = txt.read().replace('\n', ' ').split()
        return self

    def process_text(self):
        try:
            w1 = char_per_word(self._text)
        except TypeError:
            raise FileError("You need to read the file first.")
        else:
            w2 = word_count(w1)
            w3 = slices_idx(w2)
            self._text = slice_text(self._text, w3)
            return self

    def save_text(self):
        if self._text:
            with open(self.out_path, 'w') as txt:
                for i in self._text:
                    txt.write(' '.join(i))
                    txt.write("\n\n")

    def save_json(self):
        if self._text:
            res = {"generated_tweets":{f"tweet_{idx}": f"{' '.join(i)}" \
                    for idx, i in enumerate(self._text)}}
            with open(self.out_path, 'w') as txt:
                txt.writelines(res)
