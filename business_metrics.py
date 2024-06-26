# business_metrics.py

def profit_margin(revenue, cost):
    if revenue == 0:
        raise ValueError("Revenue cannot be zero.")
    return (revenue - cost) / revenue

def roi(gain_from_investment, cost_of_investment):
    if cost_of_investment == 0:
        raise ValueError("Cost of investment cannot be zero.")
    return (gain_from_investment - cost_of_investment) / cost_of_investment

def clv(avg_purchase_value, purchase_frequency, customer_lifespan):
    return avg_purchase_value * purchase_frequency * customer_lifespan