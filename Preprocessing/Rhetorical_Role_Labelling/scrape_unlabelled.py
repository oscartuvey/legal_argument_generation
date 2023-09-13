import os
import string
import unicodedata

# TODO change var names
# encoding = "utf-8"

def main():
    directory = '/content/drive/MyDrive/semantic-segmentation-master/infer'


    predictions_file = 'predictions.txt'

    index_path = "/content/drive/MyDrive/semantic-segmentation-master/finetune_git.txt"
    predictions_path = os.path.join(directory, predictions_file)

    path = os.path.join(directory, 'data')

    with open(index_path, 'a') as file:
        for file_name in os.listdir(path):

            facts = ""
            ratio = ""
            predictions = find_line_starting_with(predictions_path, file_name[:-4]) # Removes '.txt'

            labels = predictions.split(',')

            file_path = os.path.join(path, file_name)

            index = 0

            with open(file_path, 'r') as text:
                for line in text:

                    # Removes punctuation
                    line = line.lower().translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).strip()

                    if (line):
                        line = remove_control_characters(line)
                        if (labels[index] == 'Facts'):
                            facts += (line + '. ')
                        
                        if (labels[index] == 'Ratio of the decision'):
                            ratio += (line + '. ')

                        # Does index need to be here?
                        index+=1
                        
            file.write('[Facts] ' + facts[:-1] + '\n' + '[Ratio of the decision] ' + ratio[:-1] + '\n' * 2)

def find_line_starting_with(file_path, search_text):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(search_text):
                return line[len(search_text):].strip()  # or do something with the line. Check if this needs to be stripped

    return None  # return None if the line is not found

def remove_control_characters(text):
    return ''.join(c for c in text if unicodedata.category(c)[0] != 'C')


# Can you refer to the remove label function in another script? Check the colab code

main()