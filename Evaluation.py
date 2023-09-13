# Input: two .txt files where the corresponding lines of both files start with either [Facts] or [Ratio of the decision]
# Output: one .txt file which contains the evaluation scores
# The user must install the sentence-transformers package before running the code

import re
import string
from sentence_transformers import SentenceTransformer, util

def main():
    model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

    model_output_path = '/content/drive/MyDrive/semantic-segmentation-master/GPT-2_summary_3s_output.txt'
    gold_standard_path = '/content/drive/MyDrive/semantic-segmentation-master/GPT-2_summary_3s_test.txt'

    pct_word_overlap = list()
    semantic_similarity = list()

    with open(model_output_path, 'r') as model_output_text, open(gold_standard_path, 'r') as gold_standard_text:
        for model_output_line, gold_standard_line in zip(model_output_text, gold_standard_text):

            model_output_line = model_output_line.strip()
            gold_standard_line = gold_standard_line.strip()

            if (model_output_line.startswith('[Ratio of the decision]')):

                model_output_line, gold_standard_line = remove_label(model_output_line, gold_standard_line)

                model_output_embedding = model.encode(model_output_line)
                gold_standard_embedding = model.encode(gold_standard_line)
                semantic_similarity.append(util.dot_score(model_output_embedding, gold_standard_embedding))

                model_output_words = get_words(model_output_line)
                gold_standard_words = get_words(gold_standard_line)

                num_words_same = len(set(model_output_words).intersection(gold_standard_words))
                pct_word_overlap.append((num_words_same / (len(model_output_words) + len(gold_standard_words) - num_words_same)) * 100)

    evaluation_file = "/content/drive/MyDrive/semantic-segmentation-master/evaluation.txt"

    average_overlap = sum(pct_word_overlap) / len(pct_word_overlap)
    average_similarity = sum(semantic_similarity) / len(semantic_similarity)

    with open(evaluation_file, 'w') as file:
        file.write(f"Average percentage word overlap = {average_overlap}%\n")
        file.write(f"Average semantic similarity = {average_similarity}")

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

def get_words(text):
    word_list = list()

    words = re.split(r'\s+', text)
    for word in words:
        word = remove_punctuation(word.lower())
        word_list.append(word)

    return word_list

def remove_label(text1, text2):
    return text1[23:].strip(), text2[23:].strip()

main()
