# Dictionary to store course details
courses = {}

# Dictionary to store student enrollments
enrollments = {}

def add_course(course_id, course_name):
    if course_id in courses:
        print("Course already exists.")
    else:
        courses[course_id] = course_name
        print("Course added successfully.")

def enroll_student(student_name, course_id):
    if course_id not in courses:
        print("Course does not exist.")
        return
    
    if student_name not in enrollments:
        enrollments[student_name] = []
    
    if course_id in enrollments[student_name]:
        print("Student already enrolled in this course.")
    else:
        enrollments[student_name].append(course_id)
        print("Student enrolled successfully.")

def drop_course(student_name, course_id):
    if student_name not in enrollments:
        print("Student not found.")
        return
    
    if course_id in enrollments[student_name]:
        enrollments[student_name].remove(course_id)
        print("Course dropped successfully.")
    else:
        print("Student not enrolled in this course.")

def view_enrolled_courses(student_name):
    if student_name not in enrollments or not enrollments[student_name]:
        print("No courses enrolled.")
    else:
        print("Enrolled Courses:")
        for course_id in enrollments[student_name]:
            print(f"{course_id} - {courses[course_id]}")

def menu():
    while True:
        print("\n1. Add Course")
        print("2. Enroll Student")
        print("3. Drop Course")
        print("4. View Courses")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            cid = input("Course ID: ")
            cname = input("Course Name: ")
            add_course(cid, cname)

        elif choice == "2":
            name = input("Student Name: ")
            cid = input("Course ID: ")
            enroll_student(name, cid)

        elif choice == "3":
            name = input("Student Name: ")
            cid = input("Course ID: ")
            drop_course(name, cid)

        elif choice == "4":
            name = input("Student Name: ")
            view_enrolled_courses(name)

        elif choice == "5":
            print("Exiting program...")
            break

menu()      