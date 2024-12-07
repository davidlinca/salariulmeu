# backend/net_salary.py

def calculate_net_salary(gross_salary):
    """
    Calculează salariul net pe baza salariului brut.
    Args:
        gross_salary (float): Salariul brut.
    Returns:
        tuple: Salariu net, CAS, CASS, IV.
    """
    CAS_RATE = 0.25  # Asigurări Sociale (CAS)
    CASS_RATE = 0.10  # Asigurări Sociale de Sănătate (CASS)
    IV_RATE = 0.10  # Impozit pe venit (IV)

    # Calculăm contribuțiile
    cas = gross_salary * CAS_RATE
    cass = gross_salary * CASS_RATE
    iv = (gross_salary - cas - cass) * IV_RATE  # Impozit aplicat pe baza impozabilă

    # Calculăm salariul net
    net_salary = gross_salary - cas - cass - iv
    return round(net_salary, 2), round(cas, 2), round(cass, 2), round(iv, 2)
