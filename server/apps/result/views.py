from django.forms import formset_factory
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from requests import Response

from _keenthemes import KTLayout
from .forms import UserAnswerForm
from .models import Quiz, UserAnswer, Question, Option, QuizResult, UserAnswerOption


def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    result_answer_formset = formset_factory(UserAnswerForm, extra=len(questions))
    answers_formset = result_answer_formset(request.POST or None)
    if request.method == "POST":
        result = QuizResult(quiz=quiz, participant=request.user.participant)
        result.save()
        if answers_formset.is_valid():
            for question, answer_form in zip(questions, answers_formset):
                answer = answer_form.save(commit=False)
                answer.participant = request.user.participant
                answer.result = result
                answer.question = question
                answer.save()
                selected_options = request.POST.getlist(f"answers_{question.id}")
                for selected_option in selected_options:
                    option = get_object_or_404(Option, id=selected_option)
                    UserAnswerOption.objects.create(user_answer=answer, option=option)
            return redirect('home')

    context = {
        'quiz': quiz,
        'questions': questions,
        'answers_formset': answers_formset,
        'question_form_pairs': zip(questions, answers_formset)
    }
    context = KTLayout.init(context)
    return render(request, 'result/take_quiz.html', context)


# def take_quiz(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     questions = quiz.questions.prefetch_related('options')
#
#     if request.method == 'POST':
#         participant = request.user.participant  # Assuming you have a Participant model related to User
#         quiz_result, created = QuizResult.objects.get_or_create(
#             quiz=quiz, participant=participant
#         )
#         score = 0
#         for question in questions:
#             answer_id = request.POST.get(f'question_{question.id}', None)
#             if answer_id:
#                 answer = Option.objects.get(id=answer_id)
#                 UserAnswer.objects.create(
#                     participant=participant,
#                     question=question,
#                     answer=answer,
#                     result=quiz_result
#                 )
#                 if answer.is_correct:
#                     score += question.marks
#         quiz_result.score = score
#         quiz_result.passed = score >= quiz.passing_score if quiz.passing_score else None
#         quiz_result.save()
#         return redirect('quiz_result', quiz_result_id=quiz_result.id)
#
#     context = {'quiz': quiz, 'questions': questions}
#     return render(request, 'result/take_quiz.html', context)


def quiz_result(request, quiz_result_id):
    quiz_result = get_object_or_404(QuizResult, id=quiz_result_id)
    return render(request, 'result/quiz_result.html', {'quiz_result': quiz_result})
