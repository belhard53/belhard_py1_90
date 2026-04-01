import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Таблица студентов
cursor.execute('''
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL
    
)
''')

# Таблица курсов
cursor.execute('''
CREATE TABLE Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL
)
''')

# Вспомогательная таблица для связи многие-ко-многим
cursor.execute('''
CREATE TABLE Student_Courses (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
)
''')

# Вставляем студентов
cursor.executemany(
    "INSERT INTO Students (student_id, student_name) VALUES (?, ?)",
    [
        (1, 'Ruslan'),
        (2, 'Anna'),
        (3, 'Ivan'),
        (4, 'Maria'),
        (5, 'Dmitriy')
    ]
)

# Вставляем курсы
cursor.executemany(
    "INSERT INTO Courses (course_id, course_name) VALUES (?, ?)",
    [
        (2, 'Math'),
        (4, 'Physics'),
        (5, 'Literature'),
        (6, 'IT'),
        (7, 'History')
    ]
)

# Связи студенты-курсы (многие-ко-многим)
cursor.executemany(
    "INSERT INTO Student_Courses (student_id, course_id) VALUES (?, ?)",
    [
        (1, 2),   # Ruslan -> Math
        (1, 4),   # Ruslan -> Physics
        (1, 5),   # Ruslan -> Literature
        (2, 2),   # Anna -> Math
        (2, 5),   # Anna -> Literature
        (2, 6),   # Anna -> IT
        (3, 4),   # Ivan -> Physics
        (3, 6),   # Ivan -> IT
        (4, 7),   # Maria -> History
        (4, 5),   # Maria -> Literature
        (5, 2),   # Dmitriy -> Math
        (5, 4),   # Dmitriy -> Physics
        (5, 6),   # Dmitriy -> IT
        (5, 7)    # Dmitriy -> History
    ]
)

conn.commit()

# Запрос: вывести студентов и их курсы
cursor.execute('''
SELECT s.student_name, c.course_name
FROM Students s
JOIN Student_Courses sc ON s.student_id = sc.student_id
JOIN Courses c ON sc.course_id = c.course_id
ORDER BY s.student_name
''')


rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
