class Patient:
    """
    The Patient object. The initialization will not happen here. For this take a look at the
    CSVDataReader class.
    """
    def __init__(self,
        id,
        kuerzel,
        alter,
        geschlecht,
        hauptdiagnose,
        nebendiagnose,
        vorherige_erkrankungen,
        sonstige_anamnese,
        leistungsschwaeche,
        atembeschwerden,
        husten,
        sonstige_untersuchungsbefunde,
        blutdruck,
        puls,
        temperatur,
        sp_o2,
        bmi,
        pulmo,
        abdomen,
        diagnostik,
        laborwerte,
        lungenfunktion,
        roentgen,
        medikation
        #...
        ):
        self.id = id
        self.kuerzel = kuerzel
        self.alter = alter
        self.geschlecht = geschlecht
        self.hauptdiagnose = hauptdiagnose
        self.nebendiagnose = nebendiagnose
        self.vorherige_erkrankungen = vorherige_erkrankungen
        self.sonstige_anamnese = sonstige_anamnese
        self.leistungsschwaeche = leistungsschwaeche
        self.atembeschwerden = atembeschwerden
        self.husten = husten
        self.sonstige_untersuchungsbefunde = sonstige_untersuchungsbefunde
        self.blutdruck = blutdruck
        self.puls = puls
        self.temperatur = temperatur
        self.sp_o2 = sp_o2
        self.bmi = bmi
        self.pulmo = pulmo
        self.abdomen = abdomen
        self.diagnostik = diagnostik
        self.laborwerte = laborwerte
        self.lungenfunktion = lungenfunktion
        self.roentgen = roentgen
        self.medikation = medikation