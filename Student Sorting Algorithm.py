
students = [
    {"id": 'DBU1601452', "name": "Petros ", "dept": "software", "cgpa": 4.0},
    {"id": 'DBU1601603', "name": "Behailu", "dept": "computer science", "cgpa": 3.96},
    {"id": 'DBU1601333', "name": "Abebe", "dept": "engineering", "cgpa": 2.8},
    {"id": 'DBU1601201', "name": "Debebe", "dept": "Medicine", "cgpa": 3.9},
    {"id": 'DBU1601589', "name": "Eyerus", "dept": "Civil enginering", "cgpa": 3.2},
    {"id": 'DBU1601108', "name": "Fikrte", "dept": "computer science", "cgpa": 3.7},
    {"id": 'DBU1601093', "name": "Gebrye", "dept": "information.te", "cgpa": 2.9},
    {"id": 'DBU1601687', "name": "Helina", "dept": "computer science", "cgpa": 3.3},
    {"id": 'DBU1601060', "name": "Gemechu", "dept": "Data science", "cgpa": 3.6},
    {"id": 'DBU1601471', "name": "goitom", "dept": "information.te", "cgpa": 3.1}
]
while True:
    print("@@@@@@@@@@@@@@@@@@@@@\nplease choice sorting method !!!\n1: Bubble sort(by ID)\n2: insertion sort(by name)\n3: selection sort(by CGPA)\n4: exit\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    ch=int(input("what you want: "))
    if ch==1:
        def sort_students_by_id(ar):
            for i in range(len(ar)-1):
                for j in range(0, len(ar)-i-1):
                    if ar[j]["id"] > ar[j+1]["id"]:
                        ar[j], ar[j+1] = ar[j+1], ar[j]

        # Display function with headers
        def display_students(title, student_list):
            print(f"\n{title}")
            print("ID\t\tName\t\tDepartment\t\t\tCGPA")
            for s in student_list:
                print(f"{s['id']}\t{s['name']}\t\t{s['dept']}\t\t\t{s['cgpa']}")

        # Show unsorted
        display_students("Unsorted Students:", students)

        # Sort and show sorted
        sort_students_by_id(students)
        display_students("Sorted Students by ID:", students)


    elif ch==2:
        def sort_students_by_name(ar):
            for i in range(1, len(ar)):
                key = ar[i]
                j = i - 1
                while j >= 0 and ar[j]["name"] > key["name"]:
                    ar[j + 1] = ar[j]
                    j = j - 1
                ar[j + 1] = key

        # Display function with headers
        def display_students(title, student_list):
            print(f"\n{title}")
            print("ID\t\tName\t\tDepartment\t\t\tCGPA")
            for s in student_list:
                print(f"{s['id']}\t{s['name']}\t\t{s['dept']}\t\t\t{s['cgpa']}")

        # Show unsorted
        display_students("Unsorted Students:", students)

        # Sort and show sorted
        sort_students_by_name(students)
        display_students("Sorted Students by NAME:", students)

    elif ch==3:
        def sort_students_by_cgpa_desc(ar):
            for i in range(len(ar)):
                maxindex = i  # we'll look for max CGPA
                for j in range(i + 1, len(ar)):
                    if ar[j]["cgpa"] > ar[maxindex]["cgpa"]:  # > for descending
                        maxindex = j
                if maxindex != i:
                    ar[i], ar[maxindex] = ar[maxindex], ar[i]
        # Display function with headers
        def display_students(title, student_list):
            print(f"\n{title}")
            print("ID\t\tName\t\tDepartment\t\t\tCGPA")
            for s in student_list:
                print(f"{s['id']}\t{s['name']}\t\t{s['dept']}\t\t\t{s['cgpa']}")

        # Show unsorted
        display_students("Unsorted Students:", students)

        # Sort and show sorted
        sort_students_by_cgpa_desc(students)
        display_students("Sorted Students by CGPA:", students)
       
    elif ch==4:
       print("thank you!!! the program is terminated !!!")
       exit()
    else:
        print("invalid input!!! please enter correct choice ???")
