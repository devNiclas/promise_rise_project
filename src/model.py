from openai import OpenAI
import re
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class RequirementClassifierModel:
    def __init__(self, base_url="http://localhost:8080/v1", model_name="qwen2-1.5b"):
        self.client = OpenAI(
            base_url=base_url,
            api_key="blank",
        )
        self.model_name = model_name



    def classify(self, requirement_text: str, labels: list[str]) -> str:

        prompt = f"""You are an expert in software requirements classification. Classify the given software requirement into EXACTLY ONE of the allowed categories based on its primary quality concern.

Allowed categories and definitions:
- Functional: Specifies what the system must do (features, actions, business logic).
- Availability: System uptime, availability, or operational hours.
- Security: Protection of data, authentication, authorization, and privacy.
- Maintainability: How easily the system can be modified, updated, or repaired.
- Usability: User-friendliness, accessibility, and learning curve for end-users.
- Legal: Compliance, copyright, licensing, or regulatory constraints.
- Look & Feel: UI design, aesthetics, branding, or visual styling.
- Operability: How easily users or administrators can operate and manage the system.
- Performance: Speed, response time, throughput, or resource consumption.
- Scalability: Ability to handle growth in load, users, or data volume.
- Fault Tolerance: Ability to withstand component failures without crashing.
- Portability: Ease of moving the system to different environments or platforms.

Instructions:
1. Briefly think about the requirement's primary focus.
2. Provide your final answer strictly as the category name on the last line.

Requirement: '{requirement_text}'

"""



        try: 

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are an expert in software requirements classification. Your task is to classify the given software requirement text into one of the following categories: Functional, Availability, Legal, Look & Feel, Maintainability, Operability, Performance, Scalability, Security, Usability, Fault Tolerance, Portability. Please provide only the category name as your response."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
    
            )

            predicted_label = response.choices[0].message.content.strip()


            predicted_label = predicted_label.strip("'\".,*-_ ")

            if predicted_label not in labels:
                matched = [l for l in labels if l.lower() in predicted_label.lower()]

                if matched:
                    predicted_label = matched[0]

                else: 
                        predicted_label = "Functional"

            return predicted_label


        except Exception as e:
            print(f"Error during classification: {e}")
            return "Functional"






    def classify_logits(self, requirement_text: str, labels: list[str]) -> dict:
        

    
    

            

          

