import re


class Manipulate_string:
    def __init__(self):
        self.c = -1

    def manipulate(self, m):
        self.c += 1
        return f'{m.group(0).upper()}' if (self.c) % 2 == 0 else f'{m.group(0).lower()}'

    def output(self, string):
        o = re.sub('[A-Za-z]', lambda m: self.manipulate(m), string)
        return o


if __name__ == '__main__':
    string = "He is a Good Boy"
    manipulate_string = Manipulate_string()
    output = manipulate_string.output(string)
    print(output)
