# summarise.py

# This code can be drastically improved
from summarizer import Summarizer
import re
import csv


# Check for missing [Facts] or [Ratio of the decision]

# Apply summariser for 3 sentences. Calculate number of words. Add number of words to facts and arguments separately.
# Find the 3 averages
# Add the summariser text to a separate file called summary.txt

def main():

    model = Summarizer()


    directory = "/content/drive/MyDrive/semantic-segmentation-master/finetune.txt"
    summary = "/content/drive/MyDrive/semantic-segmentation-master/summary.txt"


    facts = list() # Might be better to use tuples
    ratio = list()
    facts_wc = list()
    ratio_wc = list()

    facts_words = 0
    ratio_words = 0

    data = [['num_words_facts', 'num_words_ratio', 'num_words_total']]

    with open(directory, 'r', encoding = "utf-8") as text:
        for line in text:
            if line[:7] == "[Facts]":
                fax = (line[7:]).strip()
                fax_summary = model(fax, num_sentences=3)
                facts.append(fax_summary)
                facts_words += get_num_words(fax_summary)
                facts_wc.append(get_num_words(fax_summary))
            elif line[:23] == "[Ratio of the decision]":
                arg = (line[23:]).strip()
                arg_summary = model(arg, num_sentences=3)
                ratio.append(arg_summary)
                ratio_words += get_num_words(arg_summary)
                ratio_wc.append(get_num_words(arg_summary))
            else: continue

    with open(summary, 'w') as file:

      if len(facts) == len(ratio):

          print(len(facts))


          for i in range(0, len(facts)):
              file.write('[Facts] ' + (facts[i])[:-1] + '\n' + '[Ratio of the decision] ' + (ratio[i])[:-1] + '\n' * 2)

              data_entry = [str(facts_wc[i]), str(ratio_wc[i]), str(facts_wc[i] + ratio_wc[i])]
              data.append(data_entry)


          print("Average facts word count: ", end='')
          print(facts_words/len(facts))
          print("Average ratio word count: ", end='')
          print(ratio_words/len(ratio))
          print("Total average word count : ", end='')
          print((facts_words + ratio_words)/ len(facts))

          file_path = "/content/drive/MyDrive/semantic-segmentation-master/data.csv"

          with open(file_path, 'w', newline='') as file:
              writer = csv.writer(file)
              writer.writerows(data)





      else: print("Fail")


def get_num_words(text):
    sentences = re.split(r"[.!?]+", text)
    words = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            words.extend(re.split(r"\s+", sentence))

    return len(words)

main()