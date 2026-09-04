from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Herb


#  Welcome Page
def welcome(request):
    return render(request, 'herbs/welcome.html')


#  Herb List Page (4 cards page)
def herb_list(request):
    herbs = Herb.objects.all()
    return render(request, "herbs/herb_list.html", {"herbs": herbs})


#  Herb Detail Page
def herb_detail(request, id):
    herb = get_object_or_404(Herb, id=id)
    return render(request, "herbs/herb_detail.html", {"herb": herb})


#  Chatbot  )
def chatbot(request):
    message = request.GET.get("message", "").lower()
    herbs = Herb.objects.all()

    # search by herb name
    for herb in herbs:
        if herb.name.lower() in message:
            return JsonResponse({
                "reply": f"{herb.name}: {herb.description} Useful for: {herb.diseases}"
            })

    # search by disease
    for herb in herbs:
        if herb.diseases.lower() in message:
            return JsonResponse({
                "reply": f"{herb.name} is useful for {herb.diseases}"
            })

    return JsonResponse({
        "reply": "Sorry, I couldn't find information about that herb."
    })


# 🌿 Quiz Page (temporary placeholder)
import random
import json
from django.shortcuts import render

def quiz_page(request):

    all_questions = [
        {"question": "Which herb is best for hair growth?", "options": ["Neem", "Amla", "Tulsi", "Aloe Vera"], "answer": "Amla"},
        {"question": "Which herb improves skin glow?", "options": ["Turmeric", "Pepper", "Clove", "Cumin"], "answer": "Turmeric"},
        {"question": "Which herb helps with cold and cough?", "options": ["Tulsi", "Rose", "Mint", "Amla"], "answer": "Tulsi"},
        {"question": "Which herb is known as Indian ginseng?", "options": ["Ashwagandha", "Neem", "Amla", "Brahmi"], "answer": "Ashwagandha"},
        {"question": "Which herb improves memory power?", "options": ["Brahmi", "Turmeric", "Ginger", "Pepper"], "answer": "Brahmi"},
        {"question": "Which herb helps in digestion?", "options": ["Ginger", "Rose", "Mint", "Tulsi"], "answer": "Ginger"},
        {"question": "Which herb is best for acne treatment?", "options": ["Neem", "Amla", "Tulsi", "Mint"], "answer": "Neem"},
        {"question": "Which herb is rich in Vitamin C?", "options": ["Amla", "Turmeric", "Ashwagandha", "Brahmi"], "answer": "Amla"},
        {"question": "Which herb helps reduce stress?", "options": ["Ashwagandha", "Neem", "Tulsi", "Rose"], "answer": "Ashwagandha"},
        {"question": "Which herb is best for skin hydration?", "options": ["Aloe Vera", "Pepper", "Cumin", "Clove"], "answer": "Aloe Vera"},
    ]

    if request.method == "POST":
        questions_json = request.POST.get("questions_data")

        # 🛡️ prevent crash if empty
        if not questions_json:
            questions = random.sample(all_questions, 3)
            return render(request, "herbs/quiz.html", {
                "questions": questions,
                "result": "Session expired. Please try again.",
                "questions_json": json.dumps(questions)
            })

        questions = json.loads(questions_json)
        score = 0

        for i, q in enumerate(questions):
            if request.POST.get(f"q{i}") == q["answer"]:
                score += 1

        result = f"Your Score: {score} / 3"

    else:
        questions = random.sample(all_questions, 3)
        result = None

    return render(request, "herbs/quiz.html", {
        "questions": questions,
        "result": result,
        "questions_json": json.dumps(questions)
    })

    if request.method == "POST":
        questions = json.loads(request.POST.get("questions_data"))
        score = 0

        for i, q in enumerate(questions):
            if request.POST.get(f"q{i}") == q["answer"]:
                score += 1

        result = f"Your Score: {score} / 3"

    else:
        questions = random.sample(all_questions, 3)
        result = None

    return render(request, "herbs/quiz.html", {
        "questions": questions,
        "result": result,
        "questions_json": json.dumps(questions)
    })


# 🌿 Granny Remedy Page (temporary placeholder)
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# import json
# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def granny_chat(request):

    # GET request (from your HTML)
    if request.method == "GET":
        user_message = request.GET.get("message", "").strip()

    # POST support (optional)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip()
        except:
            return JsonResponse({"reply": "Invalid request"})
    else:
        return JsonResponse({"reply": "Invalid request"})

    if not user_message:
        return JsonResponse({"reply": "Ask something beta 🌿"})

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"""
Give a simple Ayurvedic home remedy in 2-3 lines for: {user_message}

Keep it short and clear.
""",
                "stream": False
            },
            timeout=90
        )

        data = response.json()

        #  FIX: safe extraction
        reply = data.get("response", "").strip()

        if not reply:
            reply = "🌿 Try simple remedies like coconut oil massage and healthy diet."

        return JsonResponse({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({"reply": "Granny is resting 😴"})
def granny_page(request):
    return render(request, "herbs/granny.html")