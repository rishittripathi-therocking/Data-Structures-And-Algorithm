# python3

import sys

# def read_input():
#     return (input().rstrip(), input().rstrip())
#
# def print_occurrences(output):
#     print(' '.join(map(str, output)))
#
# def get_occurrences(pattern, text):
#     return [
#         i
#         for i in range(len(text) - len(pattern) + 1)
#         if text[i:i + len(pattern)] == pattern
#     ]
#
# if __name__ == '__main__':
#     print_occurrences(get_occurrences(*read_input()))

def calculate_hash(word):
    print(word)
    hashkey = 0
    for i in range(len(word)):
        hashkey += (ord(word[i]) * (263 ** i))% 1000000007
    print(hashkey)
    return hashkey
def recalculate_hash(remove_letter, add_letter, previous_hash, phrase_length):
    print(remove_letter, add_letter, ord(remove_letter), ord(add_letter))
    new_hash = ((((263 * previous_hash) + ord(add_letter) - (ord(remove_letter) * (263**(phrase_length-1))))%1000000007) + 1000000007) %1000000007
    print(new_hash)
    return new_hash

def compare(word, phrase):
    assert len(word) == len(phrase)
    for i in range(0, len(phrase)):
        if word[i] != phrase[i]:
            return False
    return True

if __name__ == "__main__":
    phrase = sys.stdin.readline().rstrip('\n')
    data = sys.stdin.readline()
    phrase_hash = calculate_hash(phrase)
    word_hash = 0
    result = []
    for i in range(0, len(data) - len(phrase)):
        if i == 0:
            word_hash = calculate_hash(data[len(data) - len(phrase) - 1:len(data)-1])
        else:
            word_hash = recalculate_hash(data[-(i+1)], data[len(data) - len(phrase) - i - 1], word_hash, len(phrase))

        if word_hash == phrase_hash:
            if compare(data[len(data) - len(phrase) - i - 1:-(i+1)], phrase):
                result.append(len(data) - len(phrase) - i - 1)

    for i in range(len(result)):
        print(result[-(1-i)], end=' ')