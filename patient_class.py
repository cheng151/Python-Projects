class Patients:
    def __init__(self, patient, weight, height, medical_history):
        self._patient = patient
        self._weight = weight
        self._height = height
        self._medical_history = medical_history

    def __str__(self):
        return f"{self._patient} weighs {self._weight} is {self._height}. And has {self._medical_history}."


    def get_weight(self):
        return self._weight
    
    def get_height(self):
        return self._height
    
    
    def set_medical_history(self, illness):
        self._medical_history = illness


    def get_medical_history(self):
        return self._medical_history
    
def main():
    patient = get_patient()
    print(patient)

def get_patient():
    name = input("Name: ")
    weight = float(input("Weight: "))
    height = int(input("Height: "))
    medical_history = input("Illness: ")
    return Patients(name, weight, height, medical_history)


if __name__ == "__main__":
    main()
