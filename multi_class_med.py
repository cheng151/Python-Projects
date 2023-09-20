class Hospital:
    def __init__(self, hospital_name):
        self._hospital_name = hospital_name
        self._patients = []
    
    def get_hospital_name():
        return self._hospital_name
    
    def add_new_patient(self, name, medical_history):
        patient_object = Patients(name, medical_history)
        self._patients.append(patient_object)



class Patients:
    def __init__(self, name, medical_history):
        self._name = name
        self._medical_history = medical_history

    def get_name(self):
        return self._name
    
    def get_medical_history(self):
        return self._medical_history

hospital = Hospital("Prisma")
hospital.add_new_patient("Chris", "Healthy")