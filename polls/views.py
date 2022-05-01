from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import TextFrom
from .models import EnglishWord
from .naverAPI import get_translate
from django.contrib.auth import authenticate, login, logout
from .models import User
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def main(request):
    return render(request, 'polls/main.html')

def index(request):
    return render(request, 'polls/inputword.html')

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username = username, password = password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
    return render(request, 'polls/login2.html')

def logout_view(request):
    logout(request)
    return redirect("polls:Login")

def signup_view(request):
    if request.method =="POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]

        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.student_id = student_id
        user.save()
        return redirect("polls:Login")
    return render(request, "polls/signup.html")

def Word(request):
    if request.method == 'POST':
        word_value = request.POST.getlist('word')
        trans = get_translate(word_value[0])
        # save_word = EnglishWord()
        # save_word.english_word = word_value
        # save_word.save()
    return render(request,'polls/Word.html',{'word_value':word_value})
