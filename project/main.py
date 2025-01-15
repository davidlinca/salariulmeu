from flask import Flask, request, render_template, jsonify, session, redirect, url_for
from net_salary import calculate_net_salary
from gross_salary import calculate_gross_salary
import json

# Inițializare aplicație Flask
app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'secret_key_for_sessions'  # Necesara pentru sesiuni

# Încarcă traducerile din fișiere JSON
def load_translations(language):
    try:
        with open(f'translations/{language}.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        with open('translations/ro.json', 'r', encoding='utf-8') as file:  # Limba implicită
            return json.load(file)

@app.before_request
def set_language():
    if 'lang' not in session:
        session['lang'] = 'ro'  # Limba implicită este româna
    elif session['lang'] not in ['ro', 'en', 'fr']:
        session['lang'] = 'ro'  # Fallback in caz de limba invalida

# Ruta pentru pagina principală (index.html - landing page)
@app.route('/')
def index():
    language = session.get('lang', 'ro')
    translations = load_translations(language)
    return render_template('index.html', translations=translations, language=language)

@app.route('/calculator.html')
def calculator():
    language = session['lang']
    translations = load_translations(language)
    return render_template('calculator.html', translations=translations, language=language)

@app.route('/about.html')
def about():
    language = session.get('lang', 'ro')
    translations = load_translations(language)
    return render_template('about.html', translations=translations, language=language)

@app.route('/set_language', methods=['POST', 'GET'])
def set_language_route():
    if request.method == 'POST':
        lang = request.form.get('language')
        current_url = request.form.get('current_url')
    else:
        lang = request.args.get('lang')
        current_url = None

    if lang in ['ro', 'en', 'fr']:
        session['lang'] = lang
        print(f"Limba actualizată la: {session['lang']}")  # Debugging

    return redirect(current_url or request.referrer or url_for('index'))

@app.route('/set_language/<lang>', methods=['GET'])
def set_language_with_url(lang):
    if lang in ['ro', 'en', 'fr']:
        session['lang'] = lang  # Actualizează limba selectată
        print(f"Limba actualizată la: {session['lang']}")  # Debugging
    return redirect(request.referrer or url_for('index'))


# Endpoint pentru calculatorul simplu (HTML)
@app.route('/calculate_simple', methods=['POST'])
def calculate_simple():
    try:
        salary = float(request.form.get('salary'))
        calculation_type = request.form.get('type')
        language = session['lang']
        translations = load_translations(language)

        if calculation_type == 'net':
            net_salary, cas, cass, iv = calculate_net_salary(salary)
            steps = [
                f"{translations['gross_salary_introduced']}: {salary:.2f} lei",
                f"- {translations['cas']} (25%): {cas:.2f} lei",
                f"- {translations['cass']} (10%): {cass:.2f} lei",
                f"- {translations['iv']} (10%): {iv:.2f} lei",
                f"{translations['net_salary_calculated']}: {net_salary:.2f} lei",
            ]
            result = net_salary
        elif calculation_type == 'gross':
            gross_salary, cas, cass, iv, steps = calculate_gross_salary(salary)
            result = gross_salary
        else:
            raise ValueError(translations['invalid_calculation'])

        return render_template('calculator.html', result=f"{result:.2f}", steps=steps, translations=translations, language=language)
    except Exception as e:
        language = session['lang']
        translations = load_translations(language)
        return render_template('calculator.html', result=f"Eroare: {str(e)}", translations=translations, language=language)

# Endpoint pentru calculatorul avansat (HTML)
@app.route('/calculate_advanced', methods=['POST'])
def calculate_advanced():
    try:
        full_salary = float(request.form.get('full_salary'))
        meal_tickets = int(request.form.get('meal_tickets') or 0)
        ticket_value = float(request.form.get('ticket_value') or 0)
        dependents = int(request.form.get('dependents') or 0)
        children = int(request.form.get('children') or 0)
        tax_exempt = request.form.get('tax_exempt') == 'yes'
        language = session['lang']
        translations = load_translations(language)

        ticket_total = meal_tickets * ticket_value
        dependent_deduction = dependents * 300
        child_deduction = children * 500 if tax_exempt else 0
        deductions = ticket_total + dependent_deduction + child_deduction

        steps = [
            f"{translations['full_salary']}: {full_salary:.2f} lei",
            f"{translations['meal_tickets']}: {ticket_total:.2f} lei",
            f"{translations['dependents_deduction']}: {dependent_deduction:.2f} lei",
            f"{translations['child_deduction']}: {child_deduction:.2f} lei",
            f"{translations['total_deductions']}: {deductions:.2f} lei",
        ]

        net_salary = full_salary - deductions
        steps.append(f"{translations['net_salary_calculated']}: {net_salary:.2f} lei")

        return render_template('calculator.html', result=f"{net_salary:.2f}", steps=steps, translations=translations, language=language)
    except Exception as e:
        language = session['lang']
        translations = load_translations(language)
        return render_template('calculator.html', result=f"Eroare: {str(e)}", translations=translations, language=language)

# Endpoint pentru calcul net via JSON
@app.route('/calculate_net_salary', methods=['POST'])
def calculate_net_salary_endpoint():
    try:
        data = request.get_json()
        gross_salary = data.get('gross_salary')
        language = session['lang']
        translations = load_translations(language)

        if not gross_salary:
            return jsonify({"error": translations['missing_parameter']}), 400

        net_salary, cas, cass, iv = calculate_net_salary(gross_salary)

        response = {
            "gross_salary": gross_salary,
            "net_salary": net_salary,
            "deductions": {
                translations['cas']: cas,
                translations['cass']: cass,
                translations['iv']: iv,
            },
            "steps": [
                f"{translations['gross_salary_introduced']}: {gross_salary:.2f} lei",
                f"- {translations['cas']} (25%): {cas:.2f} lei",
                f"- {translations['cass']} (10%): {cass:.2f} lei",
                f"- {translations['iv']} (10%): {iv:.2f} lei",
                f"{translations['net_salary_calculated']}: {net_salary:.2f} lei",
            ]
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint pentru calcul brut via JSON
@app.route('/calculate_gross_salary', methods=['POST'])
def calculate_gross_salary_endpoint():
    try:
        data = request.get_json()
        net_salary = data.get('net_salary')
        language = session['lang']
        translations = load_translations(language)

        if not net_salary:
            return jsonify({"error": translations['missing_parameter']}), 400

        gross_salary, cas, cass, iv, steps = calculate_gross_salary(net_salary)

        response = {
            "net_salary": net_salary,
            "gross_salary": gross_salary,
            "steps": steps
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
