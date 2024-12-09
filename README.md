![GitHub_readme](https://github.com/user-attachments/assets/6019ba88-16d8-4306-9e4e-969a38cd02c8)

UBB-FSEGA IE - Proiect Testarea produselor software

Componenta echipei:
Linca David-Alexandru (Project Manager)
Mare Bogdan-Rareș (Programator)
Kish Andrei-Cezar (Programator)
Lăzăroiu Robert-Codruț (Tester)

# Salary Calculator

Acest proiect este un calculator pentru salariul net și brut, dezvoltat cu Python și Flask.

---

## **Cum să instalezi și să configurezi proiectul**

### 1. Instalează Flask

- Creează un fișier `requirements.txt` în directorul proiectului și adaugă: Flask==2.3.2
- Rulează comanda pentru a instala Flask:
  pip install -r requirements.txt

### 2. Asigură-te că structura fișierelor este următoarea:

- salary_calculator/
  ├── backend/
  │ ├── main.py
  │ ├── net_salary.py
  │ ├── gross_salary.py
  ├── requirements.txt
  └── README.md

## 3 Ce fac fișierele

1. main.py
   Serverul Flask principal.
   Expune două endpoint-uri API:
   /calculate_net_salary: Calculează salariul net pe baza salariului brut și a deducerilor.
   /calculate_gross_salary: Calculează salariul brut pe baza salariului net dorit.

2. net_salary.py
   Conține funcția calculate_net_salary, care calculează salariul net scăzând deducerile din salariul brut.

3. gross_salary.py
   Conține funcția calculate_gross_salary, care determină salariul brut plecând de la salariul net dorit și deduceri.

4. requirements.txt
   Include dependențele necesare (în acest caz, Flask).

## 4 Cum să rulezi proiectul

1. Pornește serverul Flask

## Navighează în directorul backend:

cd backend

## Rulează serverul:

python main.py

Serverul va porni la: http://127.0.0.1:5000.

2. Testează endpoint-urile
   Poți folosi Postman sau cURL pentru a trimite cereri POST la următoarele URL-uri:

## Endpoint pentru salariul net

URL: http://127.0.0.1:5000/calculate_net_salary

## Body (JSON):

{
"gross_salary": 5000,
"deductions": {
"impozit": 500,
"contributie_sanatate": 250,
"contributie_pensie": 350
}
}

## Răspuns așteptat:

{
"net_salary": 3900.0
}

## Endpoint pentru salariul brut

URL: http://127.0.0.1:5000/calculate_gross_salary

## Body (JSON):

{
"net_salary": 3900,
"deductions": {
"impozit": 500,
"contributie_sanatate": 250,
"contributie_pensie": 350
}
}

## Răspuns așteptat:

{
"gross_salary": 5000.0
}

## Idei de testare

1. TESTARE DE BAZA
   Introduceți date corecte:
   Testați calculul salariului net și brut cu valori valide pentru salariu și deduceri.
   Verificați dacă răspunsurile API corespund calculelor corecte.
2. TESTARE DE VALIDARE A INTRARILOR

## Valori lipsă sau invalide:

Trimiteți cereri fără gross_salary sau net_salary și verificați răspunsurile de eroare.
Exemplu răspuns pentru date lipsă:
{
"error": "Salariul brut și deducerile sunt necesare."
}

## Tipuri greșite de date:

Trimiteți valori non-numerice pentru salariu (ex: text sau obiecte) și verificați răspunsurile API. 3. Testare limite

## Introduceți valori foarte mari

Testați salarii brute/nete de ordinul sutelor de mii și verificați dacă API-ul funcționează corect. 4. Probleme întâmpinate și soluții

## 404 Not Found:

Cauzată de introducerea unui URL incorect în Postman. Asigurați-vă că URL-ul este exact:
http://127.0.0.1:5000/calculate_net_salary

## Mesaj "Not Found" la cereri GET:

Endpoint-urile sunt configurate doar pentru cereri POST. Dacă încercați să accesați direct din browser, veți primi acest mesaj.

## Eroare SSL (WRONG_VERSION_NUMBER):

# Cauzată de utilizarea HTTPS pe serverul care rulează pe HTTP. Utilizați http:// în loc de https://.

Cauzată de utilizarea HTTPS pe serverul care rulează pe HTTP. Utilizați http:// în loc de https://.
