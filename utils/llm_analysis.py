
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

    # messages=[ # Remove the extra outer brackets here
    #         {"role": "system", "content": "You are a legal expert."},
    #         {"role": "user", "content": prompt}
    #     ] # Remove the extra outer brackets here
    
    # response = client.chat.completions.create(
    #     model="gpt-4o",
    #     messages=messages,
    #     max_tokens=5000,
    #     temperature=1
    # )
    json_data ="""
    ```json
    {
    "clauses": {
      "Others": [
        "CONSULTANT agrees to exercise special skill to accomplish the following results in a manner reasonably satisfactory to COMMISSION: , as specified in Exhibit A: Scope of Services, which by this reference is incorporated herein.",
        "No person named in paragraph B of this Section, or his or her successor, shall be removed or replaced by CONSULTANT, nor shall his or her agreed-upon function hereunder be changed, without the prior written consent of COMMISSION. Such consent shall not be unreasonably withheld."
      ]
    },
    "obligations": {
      "Others": [
        "CONSULTANT agrees to exercise special skill to accomplish the following results in a manner reasonably satisfactory to COMMISSION.",
        "The CONSULTANT shall submit written progress reports with each invoice. The report should be sufficiently detailed for the Contract Manager to determine if the CONSULTANT is performing to expectations or is on schedule; to provide communication of interim findings; and to sufficiently address any difficulties or special problems encountered, so remedies can be developed.",
        "The CONSULTANT’s Project Manager shall meet with the COMMISSION’s Contract Manager, as needed, to discuss progress on the contract."
      ],
      "Payment Obligation": [
        "In consideration for CONSULTANT accomplishing said result, COMMISSION agrees to pay oN as follows: Total payment is not to exceed $ for time and materials at the rates and conditions set forth in Exhibit B: Fee Schedule, which by this reference is incorporated herein."
      ]
    }
    }
    ```
    """
    # return response.choices[0].message.content.strip()
    return json_data
