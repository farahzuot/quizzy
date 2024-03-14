from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, FormView

from _keenthemes.__init__ import KTLayout
from _keenthemes.libs.theme import KTTheme
from server.apps.quiz.forms import OptionFormSet, QuestionForm, QuizForm
from server.apps.quiz.models import Option, Question, Quiz


# Create your views here.


class CreateQuizSettings(FormView):
    form_class = QuizForm
    template_name = "quiz/quiz_create_settings.html"

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.author = self.request.user.author
        quiz.save()
        self.request.session["quiz_id"] = str(quiz.id)
        return redirect("quiz:add_question")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)
        return context


class AddQuestion(View):
    template_name = "quiz/quiz_add_question.html"
    css_files = ["css/create_quiz.css"]
    js_files = ["plugins/custom/formrepeater/formrepeater.bundle.js",
                "js/create_quiz.js"]

    def get(self, request):
        quiz_id = self.get_quiz_id(request)
        if not quiz_id:
            return redirect("create_quiz_settings")
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

    def post(self, request):
        quiz_id = self.get_quiz_id(request)
        if not quiz_id:
            return redirect("create_quiz_settings")
        context = self.get_context_data(request)
        if self.forms_are_valid(request, context):
            self.save_question_and_options(context, quiz_id)
            return redirect("quiz:add_question")
        return render(request, self.template_name, context)

    def forms_are_valid(self, request, context):
        return (
            context['question_form'].is_valid()
            and context['option_formset'].is_valid()
        )

    def save_question_and_options(self, context, quiz_id):
        question = context['question_form'].save(commit=False)
        question.quiz = get_object_or_404(Quiz, id=quiz_id)
        question.save()
        for form in context['option_formset']:
            option_text = form.cleaned_data.get("option_text")
            is_correct = form.cleaned_data.get("is_correct")
            if option_text:
                Option.objects.create(
                    question=question,
                    option_text=option_text,
                    is_correct=is_correct,
                )

    def get_quiz_id(self, request):
        return request.session.get("quiz_id")

    def get_context_data(self, request):
        question_form = QuestionForm(request.POST or None)
        option_formset = OptionFormSet(request.POST or None)
        questions_list = Question.objects.filter(quiz__id=self.get_quiz_id(request))
        context = {
            "question_form": question_form,
            "option_formset": option_formset,
            "questions_list": questions_list,
        }
        context = KTLayout.init(context)
        for css_file in self.css_files:
            KTTheme.addCssFile(css_file)
        for js_file in self.js_files:
            KTTheme.addJavascriptFile(js_file)
        return context


class ListQuizView(ListView):
    model = Quiz
    template_name = "quiz/quiz_list.html"
    context_object_name = "quizzes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)
        return context
