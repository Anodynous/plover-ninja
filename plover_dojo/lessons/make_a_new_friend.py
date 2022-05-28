#!/usr/bin/env python3

from datetime import date

from plover_dojo.storage import get_most_common_words_that_have_not_been_used_yet

class MakeANewFriend:
    def __init__(self):
        pass

    # TODO: Make this a class method?
    def make_lesson(self):
        frequency_word_tuples = get_most_common_words_that_have_not_been_used_yet()
        longest_word_len = 0
        for _, word in frequency_word_tuples:
            word_len = len(word)
            if word_len > longest_word_len:
                longest_word_len = word_len
        padding = longest_word_len + 5

        word_list = []
        for frequency, word in frequency_word_tuples:
            text = f'{word:{padding}} word #{frequency}'
            word_list.append(text)
        word_list = '\n'.join(word_list)

        today = date.today()
        file_name_today = today.strftime('%Y%m%d')
        report_text_today = today.strftime('%m/%d/%Y')

        with open(f'/tmp/{file_name_today}_make_a_new_friend.txt', 'w') as f:
            text = f"""Dojo Lesson
{report_text_today}

Make some new friends today! Here are the most common words
that haven't appeared in your writing yet. Give them a try!

{word_list}

🐦🥋
"""
            f.write(text)
