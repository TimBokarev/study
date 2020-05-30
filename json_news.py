
import json


def news_reader(file_name):

    with open(file_name) as f:
        file_content = f.read()
        content = json.loads(file_content)

    text = content['rss']['channel']['items']

    news_extract = []
    for news_list in text:
        news_line_extract = news_list['description']
        news_extract.append(news_line_extract)

    return news_extract

# print(news_reader('newsafr.json'))


def words_counter(news_string):

    words = []
    for news in news_string:
        words.append(news.split())

    final_words = []
    for w_list in words:
        final_words = final_words + w_list

# убираем лишние слова, меньше 6 букв
    words_7plus_list = []
    for word_in_test in final_words:
        if len(word_in_test) > 6:
            words_7plus_list.append(word_in_test)

    count_dict = {}
    for w in words_7plus_list:
        count_dict[w] = words_7plus_list.count(w)

    freq = []
    for w1 in count_dict:
        freq.append(count_dict[w1])
    freq.sort(reverse=True)
    top_10 = freq[0:10:1]
    print(top_10)

    for w2 in count_dict:
        if count_dict[w2] in top_10:
            print(f"{w2} - {count_dict[w2]}")


words_counter(news_reader('newsafr.json'))


# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.