# gross_salary.py

def calculate_personal_deduction(gross_salary, dependents, children, gross_min_salary):
    """
    Calculează deducerea personală în funcție de salariul brut, numărul de persoane în întreținere și copii.
    """
    deduction_table = {
        0: {
            (0, 50): 20.0,
            (51, 100): 19.5,
            (101, 150): 19.0,
            (151, 200): 18.5,
            (201, 250): 18.0,
            (251, 300): 17.5,
            (301, 350): 17.0,
            (351, 400): 16.5,
            (401, 450): 16.0,
            (451, 500): 15.5,
            (501, 550): 15.0,
            (551, 600): 14.5,
            (601, 650): 14.0,
            (651, 700): 13.5,
            (701, 750): 13.0,
            (751, 800): 12.5,
            (801, 850): 12.0,
            (851, 900): 11.5,
            (901, 950): 11.0,
            (951, 1000): 10.5,
            (1001, 1050): 10.0,
            (1051, 1100): 9.5,
            (1101, 1150): 9.0,
            (1151, 1200): 8.5,
            (1201, 1250): 8.0,
            (1251, 1300): 7.5,
            (1301, 1350): 7.0,
            (1351, 1400): 6.5,
            (1401, 1450): 6.0,
            (1451, 1500): 5.5,
            (1501, 1550): 5.0,
            (1551, 1600): 4.5,
            (1601, 1650): 4.0,
            (1651, 1700): 3.5,
            (1701, 1750): 3.0,
            (1751, 1800): 2.5,
            (1801, 1850): 2.0,
            (1851, 1900): 1.5,
            (1901, 1950): 1.0,
            (1951, 2000): 0.5,
            (2001, float('inf')): 0.0,
        },
        1: {
            (0, 50): 25.0,
            (51, 100): 24.5,
            (101, 150): 24.0,
            (151, 200): 23.5,
            (201, 250): 23.0,
            (251, 300): 22.5,
            (301, 350): 22.0,
            (351, 400): 21.5,
            (401, 450): 21.0,
            (451, 500): 20.5,
            (501, 550): 20.0,
            (551, 600): 19.5,
            (601, 650): 19.0,
            (651, 700): 18.5,
            (701, 750): 18.0,
            (751, 800): 17.5,
            (801, 850): 17.0,
            (851, 900): 16.5,
            (901, 950): 16.0,
            (951, 1000): 15.5,
            (1001, 1050): 15.0,
            (1051, 1100): 14.5,
            (1101, 1150): 14.0,
            (1151, 1200): 13.5,
            (1201, 1250): 13.0,
            (1251, 1300): 12.5,
            (1301, 1350): 12.0,
            (1351, 1400): 11.5,
            (1401, 1450): 11.0,
            (1451, 1500): 10.5,
            (1501, 1550): 10.0,
            (1551, 1600): 9.5,
            (1601, 1650): 9.0,
            (1651, 1700): 8.5,
            (1701, 1750): 8.0,
            (1751, 1800): 7.5,
            (1801, 1850): 7.0,
            (1851, 1900): 6.5,
            (1901, 1950): 6.0,
            (1951, 2000): 5.5,
            (2001, float('inf')): 5.0,
        },
        2: {
            (0, 50): 30.0,
            (51, 100): 29.5,
            (101, 150): 29.0,
            (151, 200): 28.5,
            (201, 250): 28.0,
            (251, 300): 27.5,
            (301, 350): 27.0,
            (351, 400): 26.5,
            (401, 450): 26.0,
            (451, 500): 25.5,
            (501, 550): 25.0,
            (551, 600): 24.5,
            (601, 650): 24.0,
            (651, 700): 23.5,
            (701, 750): 23.0,
            (751, 800): 22.5,
            (801, 850): 22.0,
            (851, 900): 21.5,
            (901, 950): 21.0,
            (951, 1000): 20.5,
            (1001, 1050): 20.0,
            (1051, 1100): 19.5,
            (1101, 1150): 19.0,
            (1151, 1200): 18.5,
            (1201, 1250): 18.0,
            (1251, 1300): 17.5,
            (1301, 1350): 17.0,
            (1351, 1400): 16.5,
            (1401, 1450): 16.0,
            (1451, 1500): 15.5,
            (1501, 1550): 15.0,
            (1551, 1600): 14.5,
            (1601, 1650): 14.0,
            (1651, 1700): 13.5,
            (1701, 1750): 13.0,
            (1751, 1800): 12.5,
            (1801, 1850): 12.0,
            (1851, 1900): 11.5,
            (1901, 1950): 11.0,
            (1951, 2000): 10.5,
            (2001, float('inf')): 10.0,
        },
        3: {
            (0, 50): 35.0,
            (51, 100): 34.5,
            (101, 150): 34.0,
            (151, 200): 33.5,
            (201, 250): 33.0,
            (251, 300): 32.5,
            (301, 350): 32.0,
            (351, 400): 31.5,
            (401, 450): 31.0,
            (451, 500): 30.5,
            (501, 550): 30.0,
            (551, 600): 29.5,
            (601, 650): 29.0,
            (651, 700): 28.5,
            (701, 750): 28.0,
            (751, 800): 27.5,
            (801, 850): 27.0,
            (851, 900): 26.5,
            (901, 950): 26.0,
            (951, 1000): 25.5,
            (1001, 1050): 25.0,
            (1051, 1100): 24.5,
            (1101, 1150): 24.0,
            (1151, 1200): 23.5,
            (1201, 1250): 23.0,
            (1251, 1300): 22.5,
            (1301, 1350): 22.0,
            (1351, 1400): 21.5,
            (1401, 1450): 21.0,
            (1451, 1500): 20.5,
            (1501, 1550): 20.0,
            (1551, 1600): 19.5,
            (1601, 1650): 19.0,
            (1651, 1700): 18.5,
            (1701, 1750): 18.0,
            (1751, 1800): 17.5,
            (1801, 1850): 17.0,
            (1851, 1900): 16.5,
            (1901, 1950): 16.0,
            (1951, 2000): 15.5,
            (2001, float('inf')): 15.0,
        },
        4: {
            (0, 50): 45.0,
            (51, 100): 44.5,
            (101, 150): 44.0,
            (151, 200): 43.5,
            (201, 250): 43.0,
            (251, 300): 42.5,
            (301, 350): 42.0,
            (351, 400): 41.5,
            (401, 450): 41.0,
            (451, 500): 40.5,
            (501, 550): 40.0,
            (551, 600): 39.5,
            (601, 650): 39.0,
            (651, 700): 38.5,
            (701, 750): 38.0,
            (751, 800): 37.5,
            (801, 850): 37.0,
            (851, 900): 36.5,
            (901, 950): 36.0,
            (951, 1000): 35.5,
            (1001, 1050): 35.0,
            (1051, 1100): 34.5,
            (1101, 1150): 34.0,
            (1151, 1200): 33.5,
            (1201, 1250): 33.0,
            (1251, 1300): 32.5,
            (1301, 1350): 32.0,
            (1351, 1400): 31.5,
            (1401, 1450): 31.0,
            (1451, 1500): 30.5,
            (1501, 1550): 30.0,
            (1551, 1600): 29.5,
            (1601, 1650): 29.0,
            (1651, 1700): 28.5,
            (1701, 1750): 28.0,
            (1751, 1800): 27.5,
            (1801, 1850): 27.0,
            (1851, 1900): 26.5,
            (1901, 1950): 26.0,
            (1951, 2000): 25.5,
            (2001, float('inf')): 25.0,
        },
    }

    total_dependents = dependents + children

    if gross_salary > 2.5 * gross_min_salary:
        return 0.0

    for interval, percentage in deduction_table.get(total_dependents, {}).items():
        if interval[0] <= gross_salary <= interval[1]:
            return gross_min_salary * (percentage / 100)
    return 0.0


def calculate_gross_salary(net_salary, dependents=0, children=0, meal_tickets=0, ticket_value=0.0, tax_exempt=False, gross_min_salary=3700):
    CAS_RATE = 0.25
    CASS_RATE = 0.10
    IV_RATE = 0.10

    ticket_total = meal_tickets * ticket_value
    ticket_tax = ticket_total * IV_RATE

    # Estimare brut inițial
    if tax_exempt:
        # Net = 0.65 * Brut + (ticket_total - ticket_tax)
        gross_estimate = (net_salary - (ticket_total - ticket_tax)) / 0.65
    else:
        # Net = 0.585 * Brut + 0.1*DP + (ticket_total - ticket_tax), DP=0 inițial
        gross_estimate = (net_salary - (ticket_total - ticket_tax)) / 0.585

    personal_deduction = calculate_personal_deduction(gross_estimate, dependents, children, gross_min_salary)

    # Recalculăm brutul cu deducerea personală reală
    if tax_exempt:
        gross_salary = (net_salary - (ticket_total - ticket_tax)) / 0.65
    else:
        gross_salary = (net_salary - 0.1*personal_deduction - (ticket_total - ticket_tax)) / 0.585

    gross_salary = round(gross_salary, 2)

    cas = round(gross_salary * CAS_RATE, 2)
    cass = round(gross_salary * CASS_RATE, 2)
    if not tax_exempt:
        taxable_base = gross_salary - cas - cass - personal_deduction
        iv = round(taxable_base * IV_RATE, 2)
    else:
        iv = 0.0

    ticket_tax = round(ticket_total * IV_RATE, 2)

    return gross_salary, cas, cass, iv, ticket_tax
