from django.shortcuts import render

# Datos de alumnos 
alumnat = [
    {"id": 1, "nom": "Bilal", "cognom1": "El Moudden", "cognom2": "El Maslouhi", "correu": "bilal@gmail.com", "moduls_matriculats": "9"},
    {"id": 2, "nom": "Marc", "cognom1": "Cuzcano", "cognom2": "Reynaldo", "correu": "mcuzcano@gmail.com", "moduls_matriculats": "7"},
    {"id": 3, "nom": "Marco Antonio", "cognom1": "Soliz", "cognom2": "Lazarte", "correu": "msoliz@gmail.com", "moduls_matriculats": "8"},
    {"id": 4, "nom": "Angelo", "cognom1": "Frank", "cognom2": "Yachi", "correu": "angeloyachi@gmail.com", "moduls_matriculats": "8"},

]

# Datos de profesores 
professors = [
    {"id": 1, "nom": "Roger", "cognom1": "Sobrino", "cognom2": "Gil", "correu": "roger@gmail.com", "curs": "DAW2", "tutor": "Sí", "moduls": "2"},
    {"id": 2, "nom": "Oriol", "cognom1": "Roca", "cognom2": "Martínez", "correu": "laura@gmail.com", "curs": "DAW1", "tutor": "No", "moduls": "3"},
    {"id": 3, "nom": "Juanma", "cognom1": "Biel", "cognom2": "Sanchez", "correu": "marc@gmail.com", "curs": "DAM1", "tutor": "Sí", "moduls": "4"},
]

# Vista Principal
def home(request):
    return render(request, 'home.html', {'students': alumnat, 'teachers': professors})

# Vista principal de Alumnos
def students_list(request):
    return render(request, 'students_list.html', {'students': alumnat})

# Vista principal de Profesores
def teachers_list(request):
    return render(request, 'teachers_list.html', {'teachers': professors})

# Vista individual de Alumno
def student_detail(request, id):
    student = next((a for a in alumnat if a["id"] == id), None)
    return render(request, 'student_detail.html', {'student': student})

# Vista individual de Profesor
def teacher_detail(request, id):
    teacher = next((p for p in professors if p["id"] == id), None)
    return render(request, 'teacher_detail.html', {'teacher': teacher})
