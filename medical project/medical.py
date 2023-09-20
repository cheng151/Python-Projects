class Patients:
    def __init__(self, name, weight, height, medical_history):
        self._name = name
        self._weight = weight
        self._height = height
        self._medical_history = medical_history

    # getter for name
    def get_name(self):
        return self._name
    
    # setter for new patient
    def set_name(self, new_name):
        self._name = new_name

    def get_weight(self):
        return self._weight
    
    def get_height(self):
        return self._height
    
    
    def set_medical_history(self, illness):
        self._medical_history = illness


    def get_medical_history(self):
        return self._medical_history

patient = Patients("Chris", 145, 66, "Healthy")
print(patient._name)
print(patient._weight)
print(patient._height)
print(patient._medical_history)