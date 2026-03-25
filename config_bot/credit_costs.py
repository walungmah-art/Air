# config/credit_costs.py
"""
Credit cost for each command
"""

CREDIT_COSTS = {
    "/co": 1,
    "/bco": 1,
    "/st": 1,
    "/mst": 1,  # Per card - handled separately
    "/txt": 1,  # Per card - handled separately
    "/addproxy": 0,  # Free (proxy management)
    "/proxy": 0,
    "/removeproxy": 0,
    "/bininfo": 0,
}

# Commands that cost per card in bulk operations
PER_CARD_COST = 1  # Each card in multi-card commands costs 1 credit