import re
from random import choice

def get_next_sentence(previous_list_string):
    previous_set = list(re.findall(r"\d+", previous_list_string))
    previous_set = set(int(x) for x in previous_set)
    all_sentences_set = set(sentence for sentence in range(1, 6))
    not_used_sentences = list(all_sentences_set - previous_set)
    new_number = choice(not_used_sentences)
    return new_number