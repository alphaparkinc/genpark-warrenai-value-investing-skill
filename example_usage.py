"""
example_usage.py -- Demonstrates WarrenAIValueInvestingClient
"""
from client import WarrenAIValueInvestingClient

def main():
    client = WarrenAIValueInvestingClient()
    result = client.analyze_stock(
        ticker="AAPL",
        current_price=175.00,
        eps=6.50,
        expected_growth_rate=11.5,
        roe=35.0,
        debt_to_equity=1.1
    )
    print(f"[WarrenAI Stock Valuation: {result['recommendation_rating']}]")
    print(f"Intrinsic Value: ${result['intrinsic_value']} (Margin of Safety: {result['margin_of_safety_pct']}%)")
    print(f"Financial Health Audit: {result['financial_health_audit']}")

if __name__ == "__main__":
    main()
