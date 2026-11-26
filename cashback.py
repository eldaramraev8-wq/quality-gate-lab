<<<<<<< HEAD
def calculate_cashback(purchases: list[float], is_vip: bool = False) -> float:
=======
import os, sys
from typing import List, Dict

def calculate_cashback( purchases: List[float], is_vip: bool = False ) -> float:
    debug_var = "test"
>>>>>>> d1caf69 (Save local files)
    total = 0.0
    for amount in purchases:
        if amount <= 0:
            continue
<<<<<<< HEAD
        rate = 0.05 if is_vip else 0.02
        total += amount * rate
    return round(total, 2)
=======
        rate = 0.05 if is_vip == True else 0.02
        total += amount * rate
    return round(total, 0)
>>>>>>> d1caf69 (Save local files)
