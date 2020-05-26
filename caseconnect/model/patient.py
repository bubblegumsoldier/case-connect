class Patient:
    """
    The Patient object. The initialization will not happen here. For this take a look at the
    CSVDataReader class.
    """
    def __init__(self,
        id,
        main_diagnosis,
        secondary_diagnosis,
        text
        #...
        ):
        self.id = id
        self.main_diagnosis = main_diagnosis
        self.secondary_diagnosis = secondary_diagnosis
        self.text = text