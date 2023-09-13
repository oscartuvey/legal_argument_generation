import os
import string

# TODO change var names
# encoding = "utf-8"

def main():
    directory = 'Preprocessing/Rhetorical_Role_Labelling/data'

    index_path = 'Preprocessing/Rhetorical_Role_Labelling/finetune_labelled.txt'

    path = os.path.join(directory, 'text')

    with open(index_path, 'w') as file:
        for file_name in os.listdir(path):

            facts = ""
            ratio = ""

            file_path = os.path.join(path, file_name)

            with open(file_path, 'r') as text:
                for line in text:

                    # Removes punctuation. Does it need to be all lower case? Ask Procheta
                    line = line.lower().translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).strip()

                    if (line):
                        label = get_label(line)
                        if label == 'facts':
                            facts += ((line[:-5]).strip() + '. ')
                        
                        if label == 'ratio of the decision':
                            ratio += ((line[:-21]).strip() + '. ')

            file.write('[Facts] ' + facts[:-1] + '\n' + '[Ratio of the decision] ' + ratio[:-1] + '\n' * 2)

# Can you refer to the remove label function in another script? Check the colab code
def get_label(text):
    label_transformations = {
        'argument': lambda x: x[-8:],
        'precedent': lambda x: x[-9:],
        'statute': lambda x: x[-7:],
        'facts': lambda x: x[-5:],
        'ratio of the decision': lambda x: x[-21:],
        'ruling by lower court': lambda x: x[-21:],
        'ruling by present court': lambda x: x[-23:],
    }

    for label, transformation in label_transformations.items():
        if text.endswith(label):
            return transformation(text)

    return None

main()
