def calculate_net_salary(gross_salary):
    """
    Calculează salariul net pe baza salariului brut.
    Args:
        gross_salary (float): Salariul brut.
    Returns:
        tuple: Salariu net, CAS, CASS, IV, DP.
    """
    CAS_RATE = 0.25  # Asigurări Sociale (CAS)
    CASS_RATE = 0.10  # Asigurări Sociale de Sănătate (CASS)
    IV_RATE = 0.10  # Impozit pe venit (IV)

    # Calculăm contribuțiile
    cas = gross_salary * CAS_RATE
    cass = gross_salary * CASS_RATE

    # Calculăm deducerea personală conform legislației
    if gross_salary <= 2000:
        dp = 740  # Deducerea maximă pentru salarii sub 2000
    elif 2000 < gross_salary <= 3600:
        dp = 740 - ((gross_salary - 2000) / 1600) * (740 - 300)  # Scade liniar
    elif 3600 < gross_salary <= 4000:
        dp = 300 - ((gross_salary - 3600) / 400) * 300  # Scade spre 0
    else:
        dp = 0  # Pentru salarii peste 4000, deducerea este 0

    dp = max(dp, 0)  # Asigurăm că deducerea nu este negativă

    # Calculăm baza impozabilă
    taxable_income = gross_salary - cas - cass - dp

    # Impozitul pe venit (IV)
    iv = taxable_income * IV_RATE if taxable_income > 0 else 0

    # Calculăm salariul net
    net_salary = gross_salary - cas - cass - iv

    return round(net_salary, 2), round(cas, 2), round(cass, 2), round(iv, 2)
