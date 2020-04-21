from transformers import pipeline

nlp = pipeline('question-answering')
nlp_large = pipeline('question-answering',
                     model='bert-large-cased-whole-word-masking-finetuned-squad')


def answer_question(question, context):
    # Ensure that question and context are strings, not lists of strings.
    question = str(''.join(question))
    context = str(''.join(context))
    answer_bert = nlp(question=question, context=context)
    answer_bert_large = nlp_large(question=question, context=context)
    # print(answer_bert)
    # print(answer_bert_large)
    return answer_bert, answer_bert_large
