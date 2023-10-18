from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .forms import IrisPredictionForm
from .models import PredResults
import joblib  # Assuming you have already trained and saved your scikit-learn model

import joblib

# from .forms import RegistrationForm


def login_view(request):
    # if request.method == "POST":
    #     email = request.POST["email"]
    #     password = request.POST["password"]

    #     # Authenticate the user based on email and password
    #     user = authenticate(request, username=email, password=password)

    #     if user is not None:
    #         # User is authenticated, log them in
    #         login(request, user)
    #         return redirect("index")  # Redirect to the desired page after successful login
    #     else:
    #         # Authentication failed, show an error message or handle it as needed
    #         error_message = "Invalid email or password. Please try again."
    #         return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")


def register(request):
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    # else:
    #     form = RegistrationForm()

    return render(request, 'register.html')

def index(request):
    return render(request, "index.html")


def Recommend(request):
    return render(request, "recommend.html")

def Courses(request):
    return render(request, "courses.html")



def iris_predict(request):
    if request.method == 'POST':
        form = IrisPredictionForm(request.POST)
        if form.is_valid():
            # Get input values
            cet = form.cleaned_data['cet']
            gpa = form.cleaned_data['gpa']
            strand = form.cleaned_data['strand']

            # Prepare input data for prediction
            input_data = [[cet, gpa, strand]]

            # Use your model to make predictions
            model = joblib.load(r"C:\Users\acer\Desktop\Cougramtion\model.pkl")  # Load your trained model
            decision_function_scores = model.decision_function(input_data)

            # Get the top 3 predicted courses
            top_3_courses_indices = decision_function_scores[0].argsort()[-3:][::-1]
            top_3_predicted_classes = model.classes_[top_3_courses_indices]

            # Save the predictions to the database
            pred_results = []

            for predicted_class in top_3_predicted_classes:
                pred_result = PredResults(
                    cet=cet,
                    gpa=gpa,
                    strand=strand,
                    classification=predicted_class
                )
                pred_result.save()
                pred_results.append(predicted_class)

            
            return render(request, 'result.html', {
                'predicted_classes': pred_results,
                'cet': cet,
                'gpa': gpa,
                'strand': strand,
            })
    else:
        form = IrisPredictionForm()
    return render(request, 'recommend.html', {'form': form})




