from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        # Coletando dados do formulário
        study_hours_per_day = float(request.form.get("study_hours_per_day"))
        social_media_hours = float(request.form.get("social_media_hours"))
        netflix_hours = float(request.form.get("netflix_hours"))
        part_time_job = bool(int(request.form.get("part_time_job")))
        attendance_percentage = int(request.form.get("attendance_percentage"))
        sleep_hours = float(request.form.get("sleep_hours"))
        diet_quality = int(request.form.get("diet_quality"))
        exercise_frequency = int(request.form.get("exercise_frequency"))
        parental_education_level = int(request.form.get("parental_education_level"))
        internet_quality = int(request.form.get("internet_quality"))
        mental_health_rating = int(request.form.get("mental_health_rating"))
        extracurricular_participation = bool(int(request.form.get("extracurricular_participation")))

        # Preparando os dados para o modelo
        dados = pd.DataFrame([{
            "study_hours_per_day": study_hours_per_day,
            "social_media_hours": social_media_hours,
            "netflix_hours": netflix_hours,
            "part_time_job": part_time_job,
            "attendance_percentage": attendance_percentage,
            "sleep_hours": sleep_hours,
            "diet_quality": diet_quality,
            "exercise_frequency": exercise_frequency,
            "parental_education_level": parental_education_level,
            "internet_quality": internet_quality,
            "mental_health_rating": mental_health_rating,
            "extracurricular_participation": extracurricular_participation
        }])

        # Carregando o modelo e fazendo a predição
        model = joblib.load("model/students_habits_perfomance.pkl")
        predicted = model.predict(dados)
        resultado = round(predicted[0], 2)

    return render_template("index.html", resultado=resultado)