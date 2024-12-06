import tkinter as tk
from tkinter import ttk

TAX_RATES = {
    "România": {
        "impozit": 0.10,
        "asigurari_sociale": 0.25,
        "asigurare_sanatate": 0.10,
        "deducere_personală_sub_26": 0.05,
        "deducere_personală_persoane_intretinere": 0.03
    },
    "Germania": {
        "praguri": [0.14, 0.42, 0.45],
        "praguri_venit": [9408, 57051, 270500],
        "asigurari_sociale": 0.20,
        "asigurare_sanatate": 0.08,
        "deducere_personală_persoane_intretinere": 0.02
    },
    "Franța": {
        "praguri": [0.11, 0.30, 0.41, 0.45, 0.49],
        "praguri_venit": [10064, 25659, 73369, 157806, float('inf')],
        "asigurari_sociale": 0.20,
        "asigurare_sanatate": 0.07,
        "deducere_personală_persoane_intretinere": 0.02
    },
    "Spania": {
        "praguri": [0.19, 0.24, 0.30, 0.37, 0.45, 0.47],
        "praguri_venit": [12450, 20200, 35200, 60000, 300000, float('inf')],
        "asigurari_sociale": 0.20,
        "asigurare_sanatate": 0.07,
        "deducere_personală_persoane_intretinere": 0.02
    }
}

def calcul_taxe_progresive(venit, praguri, praguri_venit, asigurari_sociale, asigurare_sanatate, deducere_personală_persoane_intretinere, persoane_intretinere):
    taxa_impozit = 0
    venit_ramas = venit
    
    for i in range(len(praguri)):
        if venit_ramas <= 0:
            break
        if i == 0:
            if venit_ramas <= praguri_venit[i]:
                taxa_impozit += venit_ramas * praguri[i]
                venit_ramas = 0
            else:
                taxa_impozit += praguri_venit[i] * praguri[i]
                venit_ramas -= praguri_venit[i]
        else:
            if venit_ramas <= (praguri_venit[i] - praguri_venit[i-1]):
                taxa_impozit += venit_ramas * praguri[i]
                venit_ramas = 0
            else:
                taxa_impozit += (praguri_venit[i] - praguri_venit[i-1]) * praguri[i]
                venit_ramas -= (praguri_venit[i] - praguri_venit[i-1])
    
    deducere_personală = deducere_personală_persoane_intretinere * persoane_intretinere
    venit_impozabil = venit * (1 - deducere_personală)
    taxa_asigurari_sociale = venit * asigurari_sociale
    taxa_asigurare_sanatate = venit * asigurare_sanatate
    
    taxa_totala = taxa_impozit + taxa_asigurari_sociale + taxa_asigurare_sanatate
    return taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate

def calcul_taxe_romania(venit, varsta, persoane_intretinere):
    rates = TAX_RATES["România"]
    impozit = rates["impozit"]
    asigurari_sociale = rates["asigurari_sociale"]
    asigurare_sanatate = rates["asigurare_sanatate"]
    
    # Deducere personală
    deducere_personală = 0
    if varsta < 26:
        deducere_personală = rates["deducere_personală_sub_26"]
    elif persoane_intretinere > 0:
        deducere_personală = rates["deducere_personală_persoane_intretinere"] * persoane_intretinere
    
    venit_impozabil = venit * (1 - deducere_personală)
    taxa_impozit = venit_impozabil * impozit
    taxa_asigurari_sociale = venit * asigurari_sociale
    taxa_asigurare_sanatate = venit * asigurare_sanatate
    
    taxa_totala = taxa_impozit + taxa_asigurari_sociale + taxa_asigurare_sanatate
    return taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate

def calcul_taxe_germania(venit, persoane_intretinere):
    rates = TAX_RATES["Germania"]
    taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate = calcul_taxe_progresive(venit, rates["praguri"], rates["praguri_venit"], rates["asigurari_sociale"], rates["asigurare_sanatate"], rates["deducere_personală_persoane_intretinere"], persoane_intretinere)
    return taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate

def calcul_taxe_franta(venit, persoane_intretinere):
    rates = TAX_RATES["Franța"]
    taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate = calcul_taxe_progresive(venit, rates["praguri"], rates["praguri_venit"], rates["asigurari_sociale"], rates["asigurare_sanatate"], rates["deducere_personală_persoane_intretinere"], persoane_intretinere)
    return taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate

def calcul_taxe_spania(venit, persoane_intretinere):
    rates = TAX_RATES["Spania"]
    taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate = calcul_taxe_progresive(venit, rates["praguri"], rates["praguri_venit"], rates["asigurari_sociale"], rates["asigurare_sanatate"], rates["deducere_personală_persoane_intretinere"], persoane_intretinere)
    return taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate

def afisare_taxe(tara, taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate, venit_net):
    rezultat_label.config(text=f"Taxa totală pentru {tara}: {taxa_totala:.2f} unități monetare")
    detalii_label.config(text=f"Impozit: {taxa_impozit:.2f} unități monetare\n"
                              f"Asigurări sociale: {taxa_asigurari_sociale:.2f} unități monetare\n"
                              f"Asigurare de sănătate: {taxa_asigurare_sanatate:.2f} unități monetare\n"
                              f"Venit net: {venit_net:.2f} unități monetare")

def calcul_taxe():
    venit_anual = float(venit_entry.get())
    tara = tara_combobox.get()
    
    if tara == "România":
        varsta = int(varsta_entry.get())
        persoane_intretinere = int(persoane_intretinere_entry.get())
        taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate = calcul_taxe_romania(venit_anual, varsta, persoane_intretinere)
    elif tara == "Germania":
        persoane_intretinere = int(persoane_intretinere_entry.get())
        taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate = calcul_taxe_germania(venit_anual, persoane_intretinere)
    elif tara == "Franța":
        persoane_intretinere = int(persoane_intretinere_entry.get())
        taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate = calcul_taxe_franta(venit_anual, persoane_intretinere)
    elif tara == "Spania":
        persoane_intretinere = int(persoane_intretinere_entry.get())
        taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate = calcul_taxe_spania(venit_anual, persoane_intretinere)
    else:
        rezultat_label.config(text="Opțiune invalidă!")
        return
    
    venit_net = venit_anual - taxa_totala
    afisare_taxe(tara, taxa_totala, taxa_impozit, taxa_asigurari_sociale, taxa_asigurare_sanatate, venit_net)

# Crearea ferestrei principale
root = tk.Tk()
root.title("Calculator de Taxe")
root.geometry("400x400")

# Stilizarea interfeței
style = ttk.Style()
style.theme_use("clam")

# Frame principal
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Etichete și câmpuri de intrare
venit_label = ttk.Label(main_frame, text="Venit anual:")
venit_label.grid(row=0, column=0, sticky=tk.W, pady=5)
venit_entry = ttk.Entry(main_frame)
venit_entry.grid(row=0, column=1, pady=5)

tara_label = ttk.Label(main_frame, text="Selectați țara:")
tara_label.grid(row=1, column=0, sticky=tk.W, pady=5)
tara_combobox = ttk.Combobox(main_frame, values=["România", "Germania", "Franța", "Spania"])
tara_combobox.grid(row=1, column=1, pady=5)
tara_combobox.set("România")

varsta_label = ttk.Label(main_frame, text="Vârsta:")
varsta_label.grid(row=2, column=0, sticky=tk.W, pady=5)
varsta_entry = ttk.Entry(main_frame)
varsta_entry.grid(row=2, column=1, pady=5)

persoane_intretinere_label = ttk.Label(main_frame, text="Persoane în întreținere:")
persoane_intretinere_label.grid(row=3, column=0, sticky=tk.W, pady=5)
persoane_intretinere_entry = ttk.Entry(main_frame)
persoane_intretinere_entry.grid(row=3, column=1, pady=5)

# Buton de calcul
calcul_button = ttk.Button(main_frame, text="Calculează Taxe", command=calcul_taxe)
calcul_button.grid(row=4, column=0, columnspan=2, pady=10)

# Etichetă pentru rezultat
rezultat_label = ttk.Label(main_frame, text="")
rezultat_label.grid(row=5, column=0, columnspan=2, pady=10)

# Etichetă pentru detalii
detalii_label = ttk.Label(main_frame, text="")
detalii_label.grid(row=6, column=0, columnspan=2, pady=10)

# Rularea aplicației
root.mainloop()