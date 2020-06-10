
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


def words_counter(news_string):

    # print(news_string)
    words = []
    for news in news_string:
        words.append(news.split())

    final_words = []
    for w_list in words:
        final_words = final_words + w_list

# убираем лишние слова, меньше 6 букв и переводим все в нижний регистр
    words_7plus_list = []
    for word_in_test in final_words:
        if len(word_in_test) > 6:
            word_in_test = word_in_test.lower()
            words_7plus_list.append(word_in_test)
    # print(words_7plus_list)

    count_dict = {}
    for w in words_7plus_list:
        count_dict[w] = words_7plus_list.count(w)

    sorted_list = sorted(count_dict.items(), key=lambda x: (x[1], x[0]))
    k = -1
    while k != -11:
        print(sorted_list[k])
        k = k - 1


words_counter(news_reader('newsafr.json'))


# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
#
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.