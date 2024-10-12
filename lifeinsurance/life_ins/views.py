from django.shortcuts import render
from life_ins.models import Question
from django.core.paginator import Paginator

def index(request):
    return render(request, "life_ins/index.html")

# Create your views here.
def read_questions(request):
    """
    問題を一覧表示する
    """
    questions = Question.objects.all().order_by("freq")

    # Paginate the questions, 10 per page
    paginator = Paginator(questions, 10)  # Show 10 questions per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "life_ins/questions.html", {"questions": questions})
