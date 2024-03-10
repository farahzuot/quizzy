import re

from django.forms import inlineformset_factory
from django.http import QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
from server.apps.quiz.forms import QuizForm, QuestionForm, OptionFormSet
from server.apps.quiz.models import Quiz, Option, Question


# Create your views here.

class CreateQuiz(TemplateView):
    template_name = 'quiz/quiz_create.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        """
        # Example to get page name. Refer to dashboards/urls.py file.
        url_name = resolve(self.request.path_info).url_name

        if url_name == 'dashboard-2':
            # Example to override settings at the runtime
            settings.KT_THEME_DIRECTION = 'rtl'
        else:
            settings.KT_THEME_DIRECTION = 'ltr'
        """

        # A function to init the global layout. It is defined in _keenthemes/__init__.py file
        context = KTLayout.init(context)
        KTTheme.addCssFile('css/create_quiz.css')
        KTTheme.addJavascriptFile('plugins/custom/formrepeater/formrepeater.bundle.js')
        KTTheme.addJavascriptFile('js/create_quiz.js')
        return context


def create_quiz_settings(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.author = request.user.author
            quiz.save()
            request.session['quiz_id'] = str(quiz.id)
            return redirect('quiz:add_question')
    else:
        form = QuizForm()

    context = {'form': form}
    context = KTLayout.init(context)

    return render(request, 'quiz/quiz_create_settings.html', context)


def add_question(request):
    quiz_id = request.session.get('quiz_id')
    if not quiz_id:
        return redirect('create_quiz_settings')

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        option_formset = OptionFormSet(request.POST)
        if question_form.is_valid() and option_formset.is_valid():
            question = question_form.save(commit=False)
            question.quiz = get_object_or_404(Quiz, id=quiz_id)
            question.save()
            for form in option_formset:
                option_text = form.cleaned_data.get('option_text')
                is_correct = form.cleaned_data.get('is_correct')
                if option_text:
                    Option.objects.create(question=question, option_text=option_text, is_correct=is_correct)
            return redirect('quiz:add_question')

    else:
        question_form = QuestionForm()
        option_formset = OptionFormSet()
    context = {'question_form': question_form, 'option_formset': option_formset}
    context = KTLayout.init(context)
    KTTheme.addCssFile('css/create_quiz.css')
    KTTheme.addJavascriptFile('plugins/custom/formrepeater/formrepeater.bundle.js')
    KTTheme.addJavascriptFile('js/create_quiz.js')
    return render(request, 'quiz/quiz_add_question.html', context)


class ListQuizView(ListView):
    model = Quiz
    template_name = 'quiz/quiz_list.html'
    context_object_name = 'quizzes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)
        return context
