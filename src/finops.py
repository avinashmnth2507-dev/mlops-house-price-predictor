class FinOps:
    def __init__(self):
        self.total_inferences = 0
        self.cost_per_inference_usd = 0.000001   # $0.000001 per call (example)
    
    def record_inference(self):
        self.total_inferences += 1
    
    def get_summary(self):
        total_cost = self.total_inferences * self.cost_per_inference_usd
        return {
            "total_inferences": self.total_inferences,
            "cost_per_inference_usd": self.cost_per_inference_usd,
            "total_cost_usd": round(total_cost, 6),
            "recommendations": [
                "Use spot instances for batch inference",
                "Enable auto‑scaling to reduce idle costs"
            ]
        }
