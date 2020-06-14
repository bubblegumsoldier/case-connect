from json import loads
from csv import reader, writer
from os import mkdir
from xlsxwriter.workbook import Workbook


class ResultsDataWriter:
    """
    Converts the retrieval results into CSV & Excel files for better usability.
    Results have to be in JSON file format.
    CSV file will have following structure:
    - Row 0: Titles     -> e.g Attribut, Ähnlichkeitsfunktion, Referenzpatient, Patient 1, , , , Patient 2 ...
    - Row 1: Subtitles  -> e.g. Bezeichnung, Werte, Ähnlichkeit, Gewichtete Ähnlichkeit ...
    - Row 2: Global Similarities -> e.g Globale Ähnlichkeiten, , , , 120.12, 117.32, ...
    - Row 3 & ff: Attribute description in first column and values to given titles of first row for each patient
    """

    def __init__(self):
        self.attribute_row_indices = dict()
        self.attribute_info = dict()

    def save_results(self, json_file, patient_name):
        """
        Prepares data into list-like structure, that can be saved into CSV and Excel files.
        
        Data will be written to CSV file in Folder "output_csv".
        Data will be written to Excel file in Folder "output_excel".
        If folders are missing, they will be created.
        
        :param json_file: results in JSON format
        :param patient_name: used for CSV/ Excel file titles
        """

        csv_file = open("./example_data/AttributeGewichtung.csv", 'r')  # needed for similarity functions column
        csv_reader = reader(csv_file, delimiter=';')

        next(csv_reader)  # skip header

        # Content of "AttributeGewichtung.csv" will be written to class list self.attribute_info
        # Only similarity function and default weight for each given attribute are necessary
        for row in csv_reader:
            self.attribute_info[row[0]] = {"sim": row[-1],
                                           "weight": row[1]}

        csv_file.close()

        # create folder 'output_csv' if it does not exist
        try:
            mkdir('./output_csv/')
        except:
            Exception

        # create new file 'output_Patient[ID].csv'
        csv_file = open("./output_csv/output_" + patient_name + ".csv", 'w')

        data = loads(json_file)

        # initialize first 3 rows
        # row 0: Titles
        # row 1: Subtitles
        # row 2: Global similarities
        rows = [[], [], []]

        rows[0].append("Attribut")
        rows[0].append("Ähnlichkeitsfunktion")
        rows[0].append("Gewichtung")
        rows[0].append("Referenzpatient")

        rows[1].append("Bezeichnung")
        rows[1].append("Bezeichnung")
        rows[1].append("Wert")
        rows[1].append("Werte")

        rows[2].append("Globale Gewichtung")  # -> row 2
        rows[2].append("")
        rows[2].append("")
        rows[2].append("")

        index = len(rows)

        # create new line for each attribute of patient 0
        # fill first column with attribute ID
        # fill second column with corresponding similarity function descriptions
        # fill third column with corresponding default weights
        # fourth column is reserved for reference patient attribute values, still missing
        for name in data[0]["patient"]:
            rows.append([name])
            rows[-1].append(self.attribute_info[name]["sim"])
            rows[-1].append(self.attribute_info[name]["weight"])
            rows[-1].append("n/a")  # values of reference patient (still missing)
            self.attribute_row_indices[name] = index
            index += 1

        index = 0

        for patient in data:

            index += 1

            # Titles
            rows[0].append("Patient " + str(index))
            rows[0].append("")  # -> local similarity value
            rows[0].append("")  # -> weighted local similarity value
            rows[0].append("")  # -> reasoning

            # Subtitles
            rows[1].append("Werte")
            rows[1].append("Ähnlichkeit")
            rows[1].append("Gewichtete Ähnlichkeit")
            rows[1].append("Begründung")

            # Global similarities
            rows[2].append(self.convert_number(patient["global_similarity"]["overall_score"]))
            rows[2].append("")
            rows[2].append(rows[2][-2])
            rows[2].append("")

            # fill all three columns with patient data
            for attribute_name in patient["patient"].keys():
                row_index = self.attribute_row_indices[attribute_name]
                rows[row_index].append(self.convert_number(patient["patient"][attribute_name]))
                rows[row_index].append(self.get_similarity(patient, attribute_name))
                rows[row_index].append(self.get_weighted_similarity(patient, attribute_name))
                rows[row_index].append(self.get_reasons(patient, attribute_name)[:-1])

        self.saveas_CSV(rows, csv_file)
        self.saveas_XLSX(rows, patient_name)

    def saveas_CSV(self, data: list, csv_file: open):
        """
        Saves data to CSV file

        :param data: data that will be saved to csv file
        :param csv_file: open csv file
        """

        csv_writer = writer(csv_file, delimiter=';', lineterminator='\n')

        for r, row in enumerate(data):
            csv_writer.writerow(row)

        csv_file.close()

    def saveas_XLSX(self, data: list, patient_name: str):
        """
        Saves data to excel file

        :param data: data that will be saved to excel file
        :param patient_name: patient name that is used for file title
        """

        file_path = './output_excel/' + patient_name + '.xlsx'

        try:
            mkdir('./output_excel/')
        except:
            Exception

        workbook = Workbook(file_path)
        worksheet = workbook.add_worksheet()

        for r, row in enumerate(data):
            for c, item in enumerate(row):
                worksheet.write(r, c, str(item))

        workbook.close()

    def convert_number(self, value) -> str:
        """
        Converts number format from "x,xxx.xx" to "x.xxx,xx"\n
        Replaces each '.' with an ',' and vice-versa

        - **Parameters**::

            value: value that will be casted into float

        - **Return**::

            str_tmp : value is returned as string, if value is not castable, value is returned unchanged

        """
        try:
            value = float(value)
        except:
            ValueError
            return value

        str_tmp = ""

        for token in str(value):
            if token == ".":
                str_tmp += ","
            elif token == ",":
                str_tmp += "."
            else:
                str_tmp += token

        return str_tmp

    def get_similarity(self, patient, attribute_name):
        """
        Searches for similarity value corresponding to "column_id" == attribute_name

        - **Parameters**::

            patient: dict-like object
            attribute_name: value corresponding to key "column_id"

        - **Return**::

            if attribute_name is found : self.convert_number(attribute["default_weighted_score"])
            else : n/a

        """
        for attribute in patient["global_similarity"]["local_similarity_wrappers"]:

            if attribute["column_id"] == attribute_name:
                return self.convert_number(attribute["local_similarity"]["score"])

        return "n/a"

    def get_reasons(self, data, attribute_name, collect_reasons=False):
        """
            Searches recursively for similarity reasons corresponding to "column_id" == attribute_name

            - **Parameters**::

                data: dict-like object
                attribute_name: value corresponding to key "column_id"
                collect_reasons: True, when attribute_name is found, ensures that reasons are collected in string

            - **Return**::

                reasons : number is returned as string

        """
        reasons = ""

        if type(list()) == type(data):
            for item in data:
                reasons += self.get_reasons(item, attribute_name, collect_reasons)

        elif type(dict()) == type(data):
            for key in data.keys():
                if key == "column_id":
                    if data["column_id"] == attribute_name:
                        reasons += self.get_reasons(data["local_similarity"], attribute_name, True)
                elif key == "reason" and collect_reasons:
                    return reasons + data["reason"] + "\n"
                elif key == "non_matches":
                    return reasons
                else:
                    reasons += self.get_reasons(data[key], attribute_name, collect_reasons)

        return reasons

    def get_weighted_similarity(self, patient, attribute_name):
        """
        Searches for weighted similarity value corresponding to "column_id" == attribute_name

        - **Parameters**::

            patient: dict-like object
            attribute_name: value corresponding to key "column_id"

        - **Return**::

            if attribute_name is found : self.convert_number(attribute["default_weighted_score"])
            else : n/a

        """

        for attribute in patient["global_similarity"]["local_similarity_wrappers"]:

            if attribute["column_id"] == attribute_name:
                return self.convert_number(attribute["default_weighted_score"])

        return "n/a"
