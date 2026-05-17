patients = []

def add_patient(name, age, condition, doctor):

    patient_id = len(patients) + 1

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "condition": condition,
        "doctor": doctor
    }

    patients.append(patient)

    print(f"Patient {name} (ID: {patient_id}) added under Dr. {doctor}.")

def view_patients():

    for p in patients:
        print(p)

def search_patient(name):

    results = [p for p in patients if p["name"].lower() == name.lower()]

    if results:
        print("Found:", results)

    else:
        print(f"No patient found with name: {name}")

def main():

    add_patient("Nimal", 35, "Diabetes", "Dr. Silva")

    add_patient("Amali", 28, "Hypertension", "Dr. Perera")

    view_patients()

    search_patient("Nimal")

    search_patient("Kamal")

main()