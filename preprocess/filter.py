"""
pre-training on BERT takes a lot of resources and time
for efficiency, select relevant data from COHA
and use these samples in the domain-specific pre-training stage
"""
import os
import re
from nltk import tokenize

# decade/directory number (from 1 to 10)
NUM = 6
current_decade = '19' + str(NUM) + '0'
if current_decade == '19100':
    current_decade = '2000'

CHAR_SET = 'utf-8'

# 16 words in the human similarity dataset (PWHS: pairwise human similarity)
PWHS = ["federal", "spine", "optical", "compact", "signal", "leaf", "net", "coach", "sphere", "mirror",
        "card", "virus", "disk", "brick", "virtual", "energy", "environmental", "users", "virtual", "disk"]

# words from GEMS dataset (incomplete)
GEMS = ["environmental", "users", "virtual"]

FAILED_GEMS = ["disk", "tenure", "coach", "address"]


# TODO: currently only run on a single word "coach"
# filter_keywords = PWHS + GEMS
filter_keywords = [FAILED_GEMS[2]]

CORPUS_DIR = 'C:/Users/Mizuk/Documents/phD/csc2611/COHA/raw/'
OUT_DIR = 'C:/Users/Mizuk/Documents/phD/csc2611/COHA/filtered/coach/'

# read in files
sub_dir_list = []
for dirpath, dirnames, files in os.walk(CORPUS_DIR):
    sub_dir_list.append(dirpath)

current_dir = sub_dir_list[NUM]
current_out_dir = os.path.join(OUT_DIR, current_decade)
print("current directory: {}".format(current_dir))
print("output directory: {}".format(current_out_dir))

all_counter = 0
use_counter = 0
full_list = []
for file_name in os.listdir(current_dir):
    file_path = os.path.join(current_dir, file_name)
    if file_path.endswith(".txt"):
        all_counter += 1
        print("processing {}".format(file_path))
        # input("correct?")
        with open(file_path, 'r', encoding=CHAR_SET) as fr:
            text = fr.read()
            # check filter keywords
            save = False
            for search_word in filter_keywords:
                if save:
                    break
                elif search_word in text:
                    print("search_word is {}".format(search_word))
                    save = True
            if save:
                if use_counter != 0:
                    full_list.append("\n")
                use_counter += 1
                for sent in tokenize.sent_tokenize(text):
                    if not sent.startswith('@@'):
                        sent = sent.replace("@", '')
                        sent = re.sub(' +', ' ', sent)
                        sent += "\n"
                        full_list.append(sent)
    # separate document

print("total number of files processed in {0}s: {1}".format(current_decade, all_counter))
print("number of usable files after filtering: {}".format(use_counter))

full_text_per_decade = current_decade + '.txt'
output_path_agg = output_path = os.path.join(current_out_dir, full_text_per_decade)
print("writing to: {}".format(output_path_agg))
with open(output_path_agg, 'w', encoding=CHAR_SET) as fw:
    # write sentence in lines
    fw.writelines(full_list)