# main.py
from flask import Flask, request, render_template, jsonify
from net_salary import calculate_net_salary
from gross_salary import calculate_gross_salary

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_simple', methods=['POST'])
def calculate_simple():
    try:
        salary = float(request.form.get('salary'))
        calculation_type = request.form.get('type')
        meal_tickets = int(request.form.get('meal_tickets') or 0)
        ticket_value = float(request.form.get('ticket_value') or 0)
        tax_exempt = request.form.get('tax_exempt') == 'yes'
        dependents = int(request.form.get('dependents') or 0)
        children = int(request.form.get('children') or 0)
        gross_min_salary = float(request.form.get('gross_min_salary') or 3700)  # Valoare implicită: 3700 lei

        if calculation_type == 'net':
            net_salary, cas, cass, iv, ticket_tax = calculate_net_salary(
                salary, meal_tickets, ticket_value, tax_exempt, dependents, children, gross_min_salary
            )
            steps = [
                f"Salariu brut introdus: {salary:.2f} lei",
                f"- CAS (25%): {cas:.2f} lei",
                f"- CASS (10%): {cass:.2f} lei",
                f"- IV (10% din baza impozabilă): {iv:.2f} lei" if not tax_exempt else "- Scutit de impozit pe venit",
                f"- Impozit pe tichete de masă: {ticket_tax:.2f} lei",
                f"Salariu net calculat: {net_salary:.2f} lei",
            ]
            result = net_salary
        elif calculation_type == 'gross':
            gross_salary, cas, cass, iv, ticket_tax = calculate_gross_salary(
                salary, dependents, children, meal_tickets, ticket_value, tax_exempt, gross_min_salary
            )
            steps = [
                f"Salariu net introdus: {salary:.2f} lei",
                f"Salariu brut calculat: {gross_salary:.2f} lei",
                f"- CAS (25%): {cas:.2f} lei",
                f"- CASS (10%): {cass:.2f} lei",
                f"- IV (10% din baza impozabilă): {iv:.2f} lei" if not tax_exempt else "- Scutit de impozit pe venit",
                f"- Impozit pe tichete de masă: {ticket_tax:.2f} lei",
            ]
            result = gross_salary
        else:
            raise ValueError("Tip de calcul invalid.")

        return render_template('index.html', result=f"{result:.2f}", steps=steps)
    except Exception as e:
        return render_template('index.html', result=f"Eroare: {str(e)}")

@app.route('/calculate_advanced', methods=['POST'])
def calculate_advanced():
    try:
        full_salary = float(request.form.get('full_salary'))
        meal_tickets = int(request.form.get('meal_tickets') or 0)
        ticket_value = float(request.form.get('ticket_value') or 0)
        dependents = int(request.form.get('dependents') or 0)
        children = int(request.form.get('children') or 0)
        tax_exempt = request.form.get('tax_exempt') == 'yes'
        gross_min_salary = float(request.form.get('gross_min_salary') or 3700)

        # Calcul deduceri avansate (exemplu)
        ticket_total = meal_tickets * ticket_value
        dependent_deduction = dependents * 300
        child_deduction = children * 500 if tax_exempt else 0

        deductions = ticket_total + dependent_deduction + child_deduction

        CAS_RATE = 0.25
        CASS_RATE = 0.10
        IV_RATE = 0.10

        cas = full_salary * CAS_RATE
        cass = full_salary * CASS_RATE

        taxable_base = full_salary - cas - cass - deductions
        iv = taxable_base * IV_RATE if not tax_exempt else 0

        net_salary = full_salary - cas - cass - iv + ticket_total - (ticket_total * IV_RATE)

        steps = [
            f"Salariu complet: {full_salary:.2f} lei",
            f"Tichete de masă: {ticket_total:.2f} lei",
            f"Deduceri pentru persoane în întreținere: {dependent_deduction:.2f} lei",
            f"Deduceri pentru copii (scutire): {child_deduction:.2f} lei",
            f"Total deduceri: {deductions:.2f} lei",
            f"- CAS (25%): {cas:.2f} lei",
            f"- CASS (10%): {cass:.2f} lei",
            f"- IV (10% din baza impozabilă): {iv:.2f} lei" if not tax_exempt else "- Scutit de impozit pe venit",
            f"- Impozit pe tichete de masă: {(ticket_total * IV_RATE):.2f} lei",
            f"Salariu net calculat: {net_salary:.2f} lei",
        ]

        return render_template('index.html', result=f"{net_salary:.2f}", steps=steps)
    except Exception as e:
        return render_template('index.html', result=f"Eroare: {str(e)}")

@app.route('/calculate_net_salary', methods=['POST'])
def calculate_net_salary_endpoint():
    try:
        data = request.get_json()
        gross_salary = data.get('gross_salary')
        meal_tickets = data.get('meal_tickets', 0)
        ticket_value = data.get('ticket_value', 0.0)
        tax_exempt = data.get('tax_exempt', False)
        dependents = data.get('dependents', 0)
        children = data.get('children', 0)
        gross_min_salary = data.get('gross_min_salary', 3700)

        if not gross_salary:
            return jsonify({"error": "Parametrul 'gross_salary' este necesar."}), 400

        net_salary, cas, cass, iv, ticket_tax = calculate_net_salary(
            gross_salary, meal_tickets, ticket_value, tax_exempt, dependents, children, gross_min_salary
        )

        response = {
            "gross_salary": gross_salary,
            "net_salary": net_salary,
            "deductions": {
                "CAS (25%)": cas,
                "CASS (10%)": cass,
                "IV (10% baza impozabilă)": iv if not tax_exempt else 0,
                "Impozit tichete de masă": ticket_tax,
            },
            "steps": [
                f"Salariu brut introdus: {gross_salary:.2f} lei",
                f"- CAS (25%): {cas:.2f} lei",
                f"- CASS (10%): {cass:.2f} lei",
                f"- IV (10% din baza impozabilă): {iv:.2f} lei" if not tax_exempt else "- Scutit de impozit pe venit",
                f"- Impozit pe tichete de masă: {ticket_tax:.2f} lei",
                f"Salariu net calculat: {net_salary:.2f} lei",
            ]
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
