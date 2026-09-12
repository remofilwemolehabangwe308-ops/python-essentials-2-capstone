import random

def generate_data_file():
    names = ["Lisa", "John", "Mary", "Thabo", "Lerato", "Peter", "Sarah", "David"]

    records = []
    for i in range(8):
        name = random.choice(names)
        score = random.randint(0,100)
        messy_name = random.choice([name.title(), name.lower(), name.upper()])
        messy_name = " " + messy_name + " "
        data = f"{messy_name},{score}"
        records.append(data)

    with open("data/students.txt", "w") as file:
        for record in records:
            file.write(record + "\n")


def load_students():
    tidy_records = []
    with open("data/students.txt", "r") as file:
        for record in file:
            record = record.strip()
            parts = record.split(",")

            name = parts[0].strip().title()
            score = int(parts[1].strip())
            tidy_records.append((name, score))
    return tidy_records


def export_report(text):
    with open("data/report.txt", "w") as file:
        file.write(text)

import datetime 

def log_event(message):
     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     with open("data/activity.log", "a") as file:
         file.write(f"[{timestamp}] {message}\n")


    




    
        
        
            

        


        
    