"""
genpark-warrenai-value-investing-skill: Client SDK
Distills Warren Buffett value investing rules to score financial statements.
"""
from __future__ import annotations
from typing import Optional


class WarrenAIValueInvestingClient:
    """
    SDK for WarrenAI stock analysis.
    """

    def analyze_stock(
        self,
        ticker: str,
        current_price: float,
        eps: float,
        expected_growth_rate: float,
        roe: float,
        debt_to_equity: float,
        discount_rate: float = 9.0,
        terminal_multiple: float = 15.0,
    ) -> dict:
        # Calculate Intrinsic Value using Ben Graham / DCF simplification model
        # Year 10 project value EPS
        projected_eps = eps * ((1 + (expected_growth_rate / 100)) ** 10)
        terminal_value = projected_eps * terminal_multiple
        
        # Discount to present value
        intrinsic_val = terminal_value / ((1 + (discount_rate / 100)) ** 10)
        intrinsic_val = round(intrinsic_val, 2)

        # Margin of Safety calculation
        if intrinsic_val > current_price:
            safety_margin = round(((intrinsic_val - current_price) / intrinsic_val) * 100, 1)
        else:
            safety_margin = 0.0

        # Health Auditing
        passed_criteria = []
        if roe >= 15.0:
            passed_criteria.append("Strong ROE (>=15%)")
        else:
            passed_criteria.append("Weak ROE (<15%)")

        if debt_to_equity <= 1.5:
            passed_criteria.append("Safe Leverage (D/E <=1.5)")
        else:
            passed_criteria.append("High Leverage Risk (D/E >1.5)")

        health_audit = "; ".join(passed_criteria)

        # Decision Matrix
        if safety_margin >= 30.0 and roe >= 15.0 and debt_to_equity <= 1.5:
            rating = "STRONG BUY"
        elif safety_margin >= 15.0 and debt_to_equity <= 1.5:
            rating = "BUY"
        elif safety_margin > 0.0:
            rating = "HOLD"
        else:
            rating = "OVERVALUED / SELL"

        return {
            "intrinsic_value": intrinsic_val,
            "margin_of_safety_pct": safety_margin,
            "recommendation_rating": rating,
            "financial_health_audit": health_audit
        }
