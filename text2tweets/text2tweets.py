import os

class ExtractText:
    def __init__(self, in_path:str, out_path:str):
        self.in_path = in_path
        self.out_path = out_path

    def read_text(self):
        with open(self.in_path, 'r') as txt:
            all_text = txt.read().replace('\n', '')

            idx = [(n*280, (n+1)*280) for n in range(1+len(all_text)//280)]
            for i in idx:
               yield all_text[slice(i[0], i[1])]
    
    def save_text(self, itr):
        with open(self.out_path, 'w') as txt:
            for i in itr:
                txt.write(i)
                txt.write("\n\n")

if __name__ == '__main__':
    txt = "../tests/input_text.txt"
    result = "../tests/output_text.txt"

    xt = ExtractText(txt, result)
    chunks = xt.read_text()
    xt.save_text(chunks)
