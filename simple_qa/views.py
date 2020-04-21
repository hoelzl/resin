from django.shortcuts import render
from simple_qa.simple_qa_model import answer_question


def question(request):
    return render(request, 'simple_qa/question.html')


def answer(request):
    print(repr(request))
    the_question = request.GET.get('question')
    the_context = request.GET.get('context')
    answer_bert, answer_bert_large = answer_question(the_question, the_context)
    return render(request,
                  'simple_qa/answer.html',
                  {
                      'question': the_question,
                      'answer_bert': answer_bert['answer'],
                      'answer_bert_large': answer_bert_large['answer'],
                  })
