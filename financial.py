# financial.py

def calculate_gross_profit(revenue, cogs):
    return revenue - cogs

def calculate_net_profit(gross_profit, expenses):
    return gross_profit - expenses

def calculate_roi(profit, investment):
    return (profit / investment) * 100