# Student Gradebook

classes= {
    'class1': {
        'name':'One',
        'no.students': 9,
        'teacher-assigned':'Mr.Hank',
        'students': {
            "Anil":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Anita":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "John":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Smith":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Jake":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Anna":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Stephenie":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Skyle":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Hanaa":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
        }

    },
    'class2': {
            'name':'One',
            'no.students': 10,
            'teacher-assigned':'Mr.John',
            'students': {
            "Jun":{'roll_no': 10,
                    'attendance': 50,
                    'performance':'good',

                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Aniz":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Anuz":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Dop":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Justin":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Skyler":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Taylor":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "June":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            "Mina":{'roll_no': 10,
                    'subjects' :{"English": 85, "Mathematics": 92, "Spanish": 70, "History":66, "Social": 67, "Science": 60, "Economics": 50, "Philosophy": 55}, 
                    },
            }
    },
} 


def student_handbook():
    print("--- STUDENT HANDBOOK ---")
    student = input("Enter the name of student: ")
    for class_key, class_data in classes.items():
        if student in class_data['students']:
            print(f"{student}")
            print("",['students']['roll_no'])
            print(f"{['students']['attendance']}")

    print("Do you want to add another students: Type Y/N ")
    choice = input('--> ').upper()
    if choice == "Y":
        name = input("Student name: ")
        roll_no = input("Roll no: ")
        clas  = input("Enter the class: ")
        subjects = input("Subjects: ")
        marks = input("Marks: ")
        if clas  in classes:
            classes[class_key]['students'][name] = {
            'roll_no' : roll_no,
            'subjects' : {subjects : marks},


        }
    elif choice == "N":
        print("Please come again. ")
        return
    else:
        print("Invalid input. Type Y/N only. ")



student_handbook()