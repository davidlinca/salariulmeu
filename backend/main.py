# backend/main.py

from flask import Flask, request, render_template
from net_salary import calculate_net_salary
from gross_salary import calculate_gross_salary

# Inițializare aplicație Flask
app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    """
    Redă pagina principală HTML.
    """
    return render_template('index.html')


@app.route('/calculate_simple', methods=['POST'])
def calculate_simple():
    """
    Procesează calculul pentru calculatorul simplu.
    """
    try:
        salary = float(request.form.get('salary'))
        calculation_type = request.form.get('type')

        if calculation_type == 'net':
            net_salary, cas, cass, iv = calculate_net_salary(salary)
            steps = [
                f"Salariu brut introdus: {salary:.2f} lei",
                f"- CAS (25%): {cas:.2f} lei",
                f"- CASS (10%): {cass:.2f} lei",
                f"- IV (10% din baza impozabilă): {iv:.2f} lei",
                f"Salariu net calculat: {net_salary:.2f} lei",
            ]
            result = net_salary
        elif calculation_type == 'gross':
            gross_salary = calculate_gross_salary(salary)
            steps = [
                f"Salariu net introdus: {salary:.2f} lei",
                f"Salariu brut calculat: {gross_salary:.2f} lei",
            ]
            result = gross_salary
        else:
            raise ValueError("Tip de calcul invalid.")

        return render_template('index.html', result=f"{result:.2f}", steps=steps)
    except Exception as e:
        return render_template('index.html', result=f"Eroare: {str(e)}")


@app.route('/calculate_advanced', methods=['POST'])
def calculate_advanced():
    """
    Procesează calculul pentru calculatorul avansat.
    """
    try:
        full_salary = float(request.form.get('full_salary'))
        meal_tickets = int(request.form.get('meal_tickets') or 0)
        ticket_value = float(request.form.get('ticket_value') or 0)
        dependents = int(request.form.get('dependents') or 0)
        children = int(request.form.get('children') or 0)
        tax_exempt = request.form.get('tax_exempt') == 'yes'

        # Calculăm deducerile avansate
        ticket_total = meal_tickets * ticket_value
        dependent_deduction = dependents * 300
        child_deduction = children * 500 if tax_exempt else 0

        deductions = ticket_total + dependent_deduction + child_deduction

        # Generăm explicațiile pas cu pas
        steps = [
            f"Salariu complet: {full_salary:.2f} lei",
            f"Tichete de masă: {ticket_total:.2f} lei",
            f"Deduceri pentru persoane în întreținere: {dependent_deduction:.2f} lei",
            f"Deduceri pentru copii (scutire): {child_deduction:.2f} lei",
            f"Total deduceri: {deductions:.2f} lei",
        ]

        net_salary = full_salary - deductions
        steps.append(f"Salariu net calculat: {net_salary:.2f} lei")

        return render_template('index.html', result=f"{net_salary:.2f}", steps=steps)
    except Exception as e:
        return render_template('index.html', result=f"Eroare: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
