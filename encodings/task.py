
import json, codecs, re, string
from pprint import pprint

countries = {
            'newsafr.json' : ['Африка', 'UTF-8'],
            'newscy.json' : ['Кипр', 'KOI8-R'],
            'newsfr.json' : ['Франция', 'iso8859_5']
            # 'newsit.json' : ['Италия', 'cp1251']
            }

def open_read(file_name, country_encoding):
    with open(file_name, encoding = country_encoding) as json_file:
        region = json.load(json_file)
        new_block = region['rss']['channel']['item']
        counter = 0
        newslines = ''
        for each in new_block:
            news_text = each ['description']['__cdata']
            news_text_wo_tags = re.sub("<.*>", "", news_text)
            news_text_clean = re.sub(r'[^\w\s]','', news_text_wo_tags)
            newslines += news_text_clean
    return(newslines)

def split_into_words(newslines):
    all_words = []
    for each_word in newslines.split():
        all_words.append(each_word.strip().lower())
    return(all_words)

def count_words_function(all_words):
    count_words = {}
    for every_word in all_words:
        if len(every_word) >= 6:
            try: count_words[every_word] += 1
            except: count_words[every_word] = 1
    return(count_words)

for each_country in countries.keys():
    newslines = open_read(each_country, countries[each_country][1])
    all_words = split_into_words(newslines)
    count_words = count_words_function(all_words)
    sorted_count_words = sorted(count_words.keys(), key = count_words.__getitem__, reverse = True)
    print('Топ новостных слов для {0}: \n{1}'.format(countries[each_country][0], sorted_count_words[:10]))
    print('\n')
