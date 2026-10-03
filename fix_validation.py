import re

with open('app/main.py', 'r') as f:
    content = f.read()

# Define the new function with correct logic
new_func = '''async def validate_insurance_with_nvidia(insurance_id: str, condition: str, lat: float, lon: float) -> Dict[str, Any]:
    if DEMO_MODE:
        return validate_insurance_regex(insurance_id)
    if not NVIDIA_API_KEY:
        return {valid: False, provider: Unknown, reason: Live insurance eligibility is not configured.}
    
    url = https://integrate.api.nvidia.com/v1/chat/completions
    headers = {
        Authorization: fBearer {NVIDIA_API_KEY},
        Content-Type: application/json
    }
    prompt = f
