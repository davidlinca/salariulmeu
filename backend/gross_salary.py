# backend/gross_salary.py

def calculate_gross_salary(net_salary):
    """
    Calculează salariul brut pe baza salariului net.
    Args:
        net_salary (float): Salariul net.
    Returns:
        float: Salariul brut calculat.
    """
    CAS_RATE = 0.25  # Asigurări Sociale (CAS)
    CASS_RATE = 0.10  # Asigurări Sociale de Sănătate (CASS)
    IV_RATE = 0.10  # Impozit pe venit (IV)

    # Calculăm salariul brut pe baza formulei inverse
    gross_salary = net_salary / (1 - CAS_RATE - CASS_RATE - IV_RATE)
    return round(gross_salary, 2)
