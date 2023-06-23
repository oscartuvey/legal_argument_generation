from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel, GPT2TokenizerFast, GPT2Tokenizer
from nltk.translate.bleu_score import sentence_bleu

def load_model(model_path):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    return model


def load_tokenizer(tokenizer_path):
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return tokenizer

def generate_text(model_path, sequence, max_length):

    model = load_model(model_path)
    tokenizer = load_tokenizer(model_path)
    ids = tokenizer.encode(f'{sequence}', return_tensors='pt')
    final_outputs = model.generate(
        ids,
        do_sample=True,
        max_length=max_length,
        pad_token_id=model.config.eos_token_id,
        top_k=50,
        top_p=0.95,
    )
    print(tokenizer.decode(final_outputs[0], skip_special_tokens=True))

def main():
    model_path = "/content/drive/MyDrive/output"
    max_len = 1000

    input_facts=[]
    gold_argument=[]

    with open("fintune.txt","r") as f:
        for line in f:
            if line.startswith("[Facts]"):
                input_facts.append(line.strip())
            else:
                gold_argument.append(line.strip())

    total_bleu=0
    gold_argument=[]

    for i in range(len(input_facts)):
        output=generate_text(model_path, input_facts[i], max_len)
        output=output.replace(input_facts[i],"")
        bleu=sentence_bleu(gold_argument[i].split(), output.split())
        print('BLEU score -> {}'.format(bleu))
        total_bleu=total_bleu+bleu


    avg_bleu=total_bleu/len(input_facts)