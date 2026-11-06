from openai import OpenAI
import re
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer


class RequirementClassifierModel:
    def __init__(self, base_url="http://localhost:8080/v1", model_name="Qwen/Qwen2-1.5B"):
        self.client = OpenAI(
            base_url=base_url,
            api_key="blank",
        )
        self.model_name = model_name

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print("Loading local model for logits...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()



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






    def classify_logits(self, requirement_text: str, labels: list[str]) -> str:
        if not labels:
            raise ValueError("At least one classification label is required.")

        prompt = f"""Classify the software requirement below.
Requirement: "{requirement_text}"
Type:"""

        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        prompt_length = input_ids.shape[1]

        self.model.eval()
        with torch.inference_mode():
            label_scores = []

            for label in labels:
                # Score the complete label, including labels that tokenize into
                # multiple pieces, and normalize so label length is not favored.
                label_ids = self.tokenizer.encode(
                    " " + label, add_special_tokens=False
                )
                if not label_ids:
                    raise ValueError(f"Label cannot be tokenized: {label!r}")

                label_tensor = torch.tensor([label_ids], device=self.device)
                full_input_ids = torch.cat([input_ids, label_tensor], dim=1)
                logits = self.model(full_input_ids).logits

                total_log_prob = 0.0
                for index, token_id in enumerate(label_ids):
                    token_logits = logits[0, prompt_length + index - 1, :]
                    total_log_prob += F.log_softmax(token_logits, dim=0)[
                        token_id
                    ].item()

                label_scores.append(total_log_prob / len(label_ids))

            scores_tensor = torch.tensor(label_scores, device=self.device)
            probabilities = F.softmax(scores_tensor, dim=0)
            max_prob, best_index = torch.max(probabilities, dim=0)

            best_label = labels[best_index.item()]
            msp_confidence = max_prob.item()

            prob_list = probabilities.tolist()
            all_probabilities = {label: prob for label, prob in zip(labels, prob_list)}
            return best_label, msp_confidence, all_probabilities


                    

                        

        




        

    
    

            

          
