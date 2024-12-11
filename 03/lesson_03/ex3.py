from student import Student
from group import CourseGroup

# Создаем экземпляр основного студента
main_student = Student("Иван", "Иванов", 20, "2-й")

# Создаем список сокурсников
classmates = [
    Student("Анна", "Петрова", 21, "2-й"),
    Student("Сергей", "Сидоров", 20, "2-й"),
    Student("Ольга", "Кузнецова", 22, "2-й"),
]

# Создаем экземпляр CourseGroup
course_group = CourseGroup(main_student, classmates)

# Форматированный вывод информации о группе
classmate_names = [f"{classmate.first_name} {classmate.last_name}" for classmate in course_group.classmates]
classmates_list = ", ".join(classmate_names)

print(f"{course_group.student.first_name} {course_group.student.last_name}, {course_group.student.age} лет, учится на курсе {course_group.student.course} вместе с: {classmates_list}")