# -*- coding: utf-8 -*-

# --- Setări Generale de Afișaj ---
LATIME = 1280
INALTIME = 720
FPS = 60

# --- Setări de Dimensiune ---
DIMENSIUNE_CELULA = 220 
MARGINE_SIMBOL = 28 

# --- Setări Animație (Fluidă + Evidențiere) ---
# Viteza de rotire (pixeli pe secundă)
VITEZA_SPIN = 4000
# Cât de repede "sare" rola în poziția finală (0.1 = 10% din distanță pe frame)
VITEZA_OPRIRE = 0.1 
# Cât de mult crește un simbol câștigător (1.2 = 120% din mărimea originală)-
FACTOR_MARIRE_CASTIG = 1.2
# Cât de repede are loc animația de mărire/micșorare (0.1 = 10% pe frame)
VITEZA_MARIRE = 0.1     

# --- Numele Simbolurilor (pentru lizibilitate) ---
WILD = 'tiganu'
SCATTER = 'caruta'
SAPTE = 'seven'
FEMEIE = 'gagica'
CAL = 'cal'
SALBA = 'salba'
INEL = 'ghiul'
POTCOAVA = 'potcoava'
ACORDEON = 'acordeon'
TAMBURINA = 'tamburina'

# --- Pasul 1: Tabelul de Plată (Câștiguri pe Linie) ---
TABEL_PLATA = {
    SAPTE:     {3: 50,  4: 200, 5: 1000},
    FEMEIE:    {3: 25,  4: 100, 5: 500},
    CAL:       {3: 20,  4: 80,  5: 400},
    SALBA:     {3: 10,  4: 40,  5: 200},
    INEL:      {3: 8,   4: 30,  5: 150},
    POTCOAVA:  {3: 8,   4: 30,  5: 150},
    ACORDEON:  {3: 5,   4: 20,  5: 100},
    TAMBURINA: {3: 5,   4: 20,  5: 100},
}

# --- Plată SCATTER ---
PLATA_SCATTER = {
    3: 5,
    4: 20,
    5: 50
}

# --- Pasul 2: Benzile de Role Virtuale (Matematica RTP) ---
BENZI_ROLE = {
    0: [ACORDEON, INEL, CAL, TAMBURINA, POTCOAVA, FEMEIE, ACORDEON, INEL, 
        TAMBURINA, CAL, ACORDEON, POTCOAVA, WILD, TAMBURINA, INEL, 
        ACORDEON, SALBA, SAPTE, TAMBURINA, ACORDEON, SCATTER, POTCOAVA],
    1: [ACORDEON, INEL, CAL, TAMBURINA, POTCOAVA, FEMEIE, ACORDEON, INEL, 
        TAMBURINA, CAL, ACORDEON, POTCOAVA, WILD, TAMBURINA, INEL, 
        ACORDEON, SALBA, FEMEIE, TAMBURINA, ACORDEON, SCATTER, POTCOAVA],
    2: [ACORDEON, INEL, CAL, TAMBURINA, POTCOAVA, FEMEIE, ACORDEON, INEL, 
        TAMBURINA, CAL, ACORDEON, POTCOAVA, WILD, TAMBURINA, INEL, 
        ACORDEON, SALBA, SAPTE, TAMBURINA, ACORDEON, SCATTER, POTCOAVA],
    3: [ACORDEON, INEL, CAL, TAMBURINA, POTCOAVA, FEMEIE, ACORDEON, INEL, 
        TAMBURINA, CAL, ACORDEON, POTCOAVA, WILD, TAMBURINA, INEL, 
        ACORDEON, SALBA, FEMEIE, TAMBURINA, ACORDEON, SCATTER, POTCOAVA],
    4: [ACORDEON, INEL, CAL, TAMBURINA, POTCOAVA, FEMEIE, ACORDEON, INEL, 
        TAMBURINA, CAL, ACORDEON, POTCOAVA, WILD, TAMBURINA, INEL, 
        ACORDEON, SALBA, SAPTE, TAMBURINA, ACORDEON, SCATTER, POTCOAVA]
}

# --- Linii de Plată ---
LINII_PLATA = {
    'linia_1': [1, 1, 1, 1, 1], # Rândul din mijloc
    'linia_2': [0, 0, 0, 0, 0], # Rândul de sus
    'linia_3': [2, 2, 2, 2, 2], # Rândul de jos
    'linia_4': [0, 1, 2, 1, 0], # Forma 'V'
    'linia_5': [2, 1, 0, 1, 2]  # Forma 'V' inversat
}

# --- Mapare Nume Fișiere Grafice ---
CALE_FUNDAL = 'grafica/grafica/background.png'
CALE_MASCA = 'grafica/grafica/masca.png' 

MAPARE_GRAFICA = {
    WILD: 'grafica/grafica/tiganu.png',
    SCATTER: 'grafica/grafica/caruta.png',
    SAPTE: 'grafica/grafica/0_seven.png',
    FEMEIE: 'grafica/grafica/gagica.png',
    CAL: 'grafica/grafica/cal.png',
    SALBA: 'grafica/grafica/salba.png',
    INEL: 'grafica/grafica/ghiul.png',
    POTCOAVA: 'grafica/grafica/potcoava 50 copy.png',
    ACORDEON: 'grafica/grafica/acordeon..png',
    TAMBURINA: 'grafica/grafica/tamburina.png'
}

# --- Setări Miză ---
MIZE_POSIBILE = [0.10, 0.20, 0.50, 1.00, 2.00, 5.00, 10.00]
MIZA_INITIALA_INDEX = 3 

# --- SECȚIUNE NOUĂ ADĂUGATĂ ---
# --- Setări Audio ---
# Asigură-te că ai un folder 'audio' cu aceste fișiere
CALE_SUNET_SPIN = 'sunet/spin.wav'
CALE_SUNET_CASTIG = 'sunet/win.wav'
CALE_SUNET_CLICK = 'sunet/click.wav'