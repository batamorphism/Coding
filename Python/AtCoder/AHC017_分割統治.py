from collections import defaultdict

def main():
    dict_of = defaultdict(None)
    if dict_of[0] is None:
        print("None")
    dict_of[1] = []
    print(dict_of[1])