
import os
from dotenv import load_dotenv

from openai import OpenAI


load_dotenv()


key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=key)

def analyze_text_with_llm(text):
    prompt = f"""
    Identify all clauses and obligations in the following legal document text and provide a summary of each.
    Categorize clauses as: Confidentiality Clause, Termination Clause, Indemnity Clause, Non-Compete Clause, Others.
    Categorize obligations as: Payment Obligation, Delivery Obligation, Maintenance Obligation, Confidentiality Obligation, Others.
    Provide the response in JSON format as follows:
    {{
      "clauses": {{
        "Confidentiality Clause": ["Clause Text 1", "Clause Text 2", ...],
        "Others": ["Clause Text 1", "Clause Text 2", ...]
      }},
      "obligations": {{
        "Payment Obligation": ["Obligation Text 1", "Obligation Text 2", ...],
        "Others": ["Obligation Text 1", "Obligation Text 2", ...]
      }}
    }}

    Legal Document Text:
    {text[:2000]}
    """

    messages=[ # Remove the extra outer brackets here
            {"role": "system", "content": "You are a legal expert."},
            {"role": "user", "content": prompt}
        ] # Remove the extra outer brackets here
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=5000,
        temperature=1
    )
    return response.choices[0].message.content.strip()
