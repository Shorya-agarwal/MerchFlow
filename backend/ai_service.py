import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("CRITICAL ERROR: GEMINI_API_KEY is missing!")
else:
    genai.configure(api_key=api_key)

def categorize_expense(description: str):
    """
    Tries AI first. If AI fails (quota/network), falls back to keyword matching.
    """
    try:
        # PLAN A: Use the Stable AI Model
        # 'gemini-flash-latest' is usually the standard 1.5 Flash (most reliable free tier)
        model = genai.GenerativeModel("models/gemini-flash-latest")
        
        prompt = f"""
        Categorize this transaction: "{description}"
        Choose strictly from: [Housing, Transportation, Food, Utilities, Insurance, Healthcare, Savings, Personal, Entertainment, Miscellaneous]
        Return ONLY the category name.
        """

        print(f"--> AI Attempt: {description}")
        response = model.generate_content(prompt)
        category = response.text.strip().replace("\n", "").replace(".", "")
        print(f"<-- AI Success: {category}")
        return category

    except Exception as e:
        # PLAN B: Graceful Fallback (The "Intuit" way to handle errors)
        print(f"!! AI Failed ({e}). Switching to Local Fallback.")
        return local_categorizer(description)

def local_categorizer(description: str):
    """
    A dumb but reliable backup system.
    """
    desc = description.lower()
    if any(x in desc for x in ["uber", "gas", "shell", "flight", "train", "bus"]):
        return "Transportation"
    if any(x in desc for x in ["food", "burger", "steak", "walmart", "coffee", "starbucks", "pizza"]):
        return "Food"
    if any(x in desc for x in ["netflix", "cinema", "movie", "spotify", "game"]):
        return "Entertainment"
    if any(x in desc for x in ["rent", "lease", "mortgage", "hotel"]):
        return "Housing"
    
    return "Miscellaneous"