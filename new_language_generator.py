import pandas

LANGUAGE = 'german'

with open(f'data/{LANGUAGE}_words.txt') as file:
    data = file.read()
    words_raw = data.split('\n')
    words_list = [word.split(" ")[0] for word in words_raw]
    words_dict = {f'{LANGUAGE}': words_list}
    df = pandas.DataFrame(words_dict)
    df.to_csv(f'data/{LANGUAGE}_words.csv')