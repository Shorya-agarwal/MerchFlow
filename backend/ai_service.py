import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# CRITICAL FIX: We must check if the key exists before initializing
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is missing in .env file")

# OpenRouter Configuration
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "http://localhost:5173", 
        "X-Title": "SmartFinance",     
    }
)

def categorize_expense(description: str):
    """
    Uses OpenRouter (Mistral Devstral/Codestral) to categorize transactions.
    """
    try:
        prompt = f"""
        Categorize this transaction into exactly one of these categories: 
        [Housing, Transportation, Food, Utilities, Insurance, Healthcare, Savings, Personal, Entertainment, Miscellaneous].
        
        Transaction: "{description}"
        
        Return ONLY the category name. No extra text.
        """

        response = client.chat.completions.create(
            # Using Mistral Codestral (Devstral) as requested
            model="mistralai/codestral-2501", 
            messages=[
                {"role": "system", "content": "You are a financial categorization assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=10,
            temperature=0
        )
        
        category = response.choices[0].message.content.strip()
        return category
    
    except Exception as e:
        print(f"AI Error: {e}")
        return "Miscellaneous" # Fallback if AI fails