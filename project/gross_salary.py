def calculate_gross_salary(net_salary):
    """
    Calculează salariul brut pornind de la salariul net.
    Args:
        net_salary (float): Salariul net.
    Returns:
        tuple: Salariu brut, CAS, CASS, IV, detalii (detalii intermediare pentru calcul).
    """
    CAS_RATE = 0.25
    CASS_RATE = 0.10
    IV_RATE = 0.10

    # Aproximare inițială pentru brut
    gross_salary = net_salary / (1 - CAS_RATE - CASS_RATE - IV_RATE)

    while True:
        # Calculăm contribuțiile pentru brut estimat
        cas = gross_salary * CAS_RATE
        cass = gross_salary * CASS_RATE

        # Calculăm deducerea personală (presupunem 0 pentru acest exemplu simplu)
        dp = 0

        # Baza impozabilă
        taxable_income = gross_salary - cas - cass - dp

        # Impozitul pe venit
        iv = taxable_income * IV_RATE if taxable_income > 0 else 0

        # Salariul net calculat
        calculated_net = gross_salary - cas - cass - iv

        # Verificăm dacă diferența dintre netul calculat și cel dorit este acceptabilă
        if abs(calculated_net - net_salary) < 0.01:
            break

        # Ajustăm brutul estimat
        gross_salary += (net_salary - calculated_net) / 2

    details = [
        f"Salariu net introdus: {net_salary:.2f} lei",
        f"- CAS (25%): {cas:.2f} lei",
        f"- CASS (10%): {cass:.2f} lei",
        f"- IV (10% din baza impozabilă): {iv:.2f} lei",
        f"Salariu brut calculat: {gross_salary:.2f} lei"
    ]

    return round(gross_salary, 2), round(cas, 2), round(cass, 2), round(iv, 2), details
