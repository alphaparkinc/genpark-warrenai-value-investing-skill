# genpark-warrenai-value-investing-skill

> **GenPark AI Agent Skill** -- WarrenAI value investing and stock intrinsic value evaluator.

## Quick Start

```python
from client import WarrenAIValueInvestingClient
client = WarrenAIValueInvestingClient()
res = client.analyze_stock("AAPL", 170.0, 6.0, 10.0, 25.0, 0.8)
print(res["recommendation_rating"])
```
