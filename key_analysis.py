
from utils import *
from vigenere_cipher import *
from caesar_cipher import *
import re


def ic(string):
    N = len(string)
    denom = N * (N - 1)

    numer = 0
    count = letter_distribution(string)

    for i in range(26):
        letter = index_to_letter(i).upper()
        n = count[letter]
        numer += n * (n - 1)

    ic = numer / denom

    return ic


def avg_ic(ics):
    sum = 0
    for ic in ics:
        sum += ic

    avg_ic = sum / len(ics)

    return avg_ic


def relative_shifts(r, string):
    columns = []
    for i in range(r):
        s = split_string(string, r, i)
        columns.append(s)

    return imc(columns)


def imc(columns):
    max_indexes = []
    for m in range(1, len(columns)):
        all_imcs = []
        for k in range(26):
            first_column_shifted = c_encrypt(columns[0], k).upper()
            c1 = len(first_column_shifted)
            c2 = len(columns[m])
            denom = c1 * c2

            count1 = letter_distribution(first_column_shifted)
            count2 = letter_distribution(columns[m])

            numer = 0

            for i in range(26):
                letter = index_to_letter(i).upper()
                f1 = count1[letter]
                f2 = count2[letter]

                numer += f1 * f2

            index_m_coin = numer / denom
            all_imcs.append(index_m_coin)
        arg_max_imc = arg_max(all_imcs)
        max_indexes.append(arg_max_imc)

    return max_indexes


def key_length(string):
    avg_ics = []
    for r in range(2, 12):
        ics = []
        for i in range(r):
            s = split_string(string, r, i)
            index_coin = ic(s)
            ics.append(index_coin)
        avg_ics.append(avg_ic(ics))

    return arg_max(avg_ics) + 2


def decrypt(s):
    s = re.sub(r'[^a-zA-Z]', '', s).replace(' ', '').replace('_', '').upper()
    r = key_length(s)
    rel_shifts = relative_shifts(r, s)
    possible_first_key_chars = guess_first_key_char(s, r)
    for i in range(len(possible_first_key_chars)):
        key = possible_first_key_chars[i]
        first_index = letter_to_index(possible_first_key_chars[i])
        for j in range(len(rel_shifts)):
            key += index_to_letter((first_index + rel_shifts[j]) % 26)
        key = key.upper()
        plain_text = v_decrypt(s, key).upper()

        print('{} - Key: {}, Plain-text: {}'.format(i + 1, key, plain_text))


def guess_first_key_char(s, r):
    most_common_eng_chars = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D']
    possible_first_chars = []
    first_column = split_string(s, r, 0)
    most_common = most_common_letter(first_column)

    most_common_index = letter_to_index(most_common)

    for i in range(len(most_common_eng_chars)):
        assumed = most_common_eng_chars[i]
        assumed_index = letter_to_index(assumed)
        dist = (most_common_index - assumed_index) % 26
        assumed_first_key_char = index_to_letter(dist)
        possible_first_chars.append(assumed_first_key_char)

    return possible_first_chars
