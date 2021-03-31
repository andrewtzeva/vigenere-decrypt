from collections import Counter
import string



def letter_to_index(letter):
    letter = letter.lower()
    if not letter.isalpha():
        return -1
    return string.ascii_lowercase.index(letter)


def index_to_letter(index):
    letters_dict = dict(enumerate(string.ascii_lowercase))
    return letters_dict[index]


def letter_distribution(string):
    return Counter(string)


def split_string(string, r, index):
    string_length = len(string)
    new_string = ''

    for i in range(string_length):
        if i % r == index:
            new_string += string[i]

    return new_string


def arg_max(num_list):
    max_elem = num_list[0]
    max_index = 0
    for i in range(len(num_list)):
        if num_list[i] > max_elem:
            max_elem = num_list[i]
            max_index = i

    return max_index


def most_common_letter(s):
    letter_distr = letter_distribution(s)
    most_common = max(letter_distr, key = letter_distr.get)
    return most_common