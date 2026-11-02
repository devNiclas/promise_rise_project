PROMPTS = {



"v1_basic": f"""You are an expert in software requirements classification. Classify the given software requirement into EXACTLY ONE of the allowed categories based on its primary quality concern.

Allowed categories: {', '.join(labels)}
Return ONLY the category name from the list above. No explanation, no punctuation.

Requirement: '{requirement_text}'
"""











"v2_definitions": f"""You are an expert in software requirements classification. Classify the given software requirement into EXACTLY ONE of the allowed categories based on its primary quality concern.

Allowed categories and definitions:
- Functional: Specifies what the system must do (features, actions, business logic).
- Availability: System uptime, availability, or operational hours.
- Legal: Compliance, copyright, licensing, or regulatory constraints.
- Look & Feel: UI design, aesthetics, branding, or visual styling.
- Maintainability: How easily the system can be modified, updated, or repaired.
- Operability: How easily users or administrators can operate and manage the system.
- Performance: Speed, response time, throughput, or resource consumption.
- Scalability: Ability to handle growth in load, users, or data volume.
- Security: Protection of data, authentication, authorization, and privacy.
- Usability: User-friendliness, accessibility, and learning curve for end-users.
- Fault Tolerance: Ability to withstand component failures without crashing.
- Portability: Ease of moving the system to different environments or platforms.

Return ONLY the category name from the list above. No explanation, no punctuation.

Requirement: '{requirement_text}'
"""























"v3_critical_with_definitions": f"""You are an expert in software requirements classification. Classify the given software requirement into EXACTLY ONE of the allowed categories based on its primary quality concern.

Allowed categories and definitions:
- Functional: Specifies what the system must do (features, actions, business logic).
- Availability: System uptime, availability, or operational hours.
- Legal: Compliance, copyright, licensing, or regulatory constraints.
- Look & Feel: UI design, aesthetics, branding, or visual styling.
- Maintainability: How easily the system can be modified, updated, or repaired.
- Operability: How easily users or administrators can operate and manage the system.
- Performance: Speed, response time, throughput, or resource consumption.
- Scalability: Ability to handle growth in load, users, or data volume.
- Security: Protection of data, authentication, authorization, and privacy.
- Usability: User-friendliness, accessibility, and learning curve for end-users.
- Fault Tolerance: Ability to withstand component failures without crashing.
- Portability: Ease of moving the system to different environments or platforms.

CRITICAL RULE: Do not default to "Functional" just because the requirement describes a feature. If the requirement specifies speed, security, usability, maintenance, or any other quality attribute, prioritize that specific category.
Return ONLY the category name from the list above. No explanation, no punctuation.



Requirement: '{requirement_text}'



"""







"v4_critical_without_definitions": """You are an expert in software requirements classification. Classify the given software requirement into EXACTLY ONE of these categories:
        Functional, Availability, Legal, Look & Feel, Maintainability, Operability, Performance, Scalability, Security, Usability, Fault Tolerance, Portability.

CRITICAL RULE: Do not default to "Functional" just because the requirement describes a feature. If the requirement specifies speed, security, usability, maintenance, or any other quality attribute, prioritize that specific category.
Return ONLY the category name. No extra text.



Requirement: '{requirement_text}'



"""



"v5_guideline": f"""Classify the software requirement into exactly ONE of these categories:
Functional, Availability, Legal, Look & Feel, Maintainability, Operability, Performance, Scalability, Security, Usability, Fault Tolerance, Portability.

Guideline: If a requirement talks about speed, security, UI design, or error handling, choose that specific non-functional category. Otherwise, classify it as Functional.

Return ONLY the category name. No extra text.

Requirement: '{requirement_text}'





"v4_cot": """You are an expert in software requirements classification. Classify the given software requirement into EXACTLY ONE of the allowed categories based on its primary quality concern.

Allowed categories and definitions:
- Functional: Specifies what the system must do (features, actions, business logic).
- Availability: System uptime, availability, or operational hours.
- Legal: Compliance, copyright, licensing, or regulatory constraints.
- Look & Feel: UI design, aesthetics, branding, or visual styling.
- Maintainability: How easily the system can be modified, updated, or repaired.
- Operability: How easily users or administrators can operate and manage the system.
- Performance: Speed, response time, throughput, or resource consumption.
- Scalability: Ability to handle growth in load, users, or data volume.
- Security: Protection of data, authentication, authorization, and privacy.
- Usability: User-friendliness, accessibility, and learning curve for end-users.
- Fault Tolerance: Ability to withstand component failures without crashing.
- Portability: Ease of moving the system to different environments or platforms.

Instructions:
1. Briefly think about the requirement's primary focus.
2. Provide your final answer strictly as the category name on the last line.

Requirement: '{requirement_text}'
"""





"v5_cot_best_prompt": f"""You are an expert in software requirements classification. Classify the given software requirement into EXACTLY ONE of the allowed categories based on its primary quality concern.

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




"v6_final_label": f"""You are classifying one software requirement into exactly one software-requirement category.

Think briefly about the requirement's primary intent, then output only the final answer in this format:

FINAL_LABEL: <one exact category name>

Do not output explanations, confidence scores, multiple labels, or any text after FINAL_LABEL.

Categories:

- Functional:
  Describes a feature, action, calculation, data operation, or behavior the system must provide.
  Use this when the requirement mainly says what the system should do.

- Availability:
  Describes uptime, continuous access, operating hours, or whether the system/service is available when needed.
  Keywords may include: available, uptime, 24/7, operating hours, accessible at all times.

- Legal:
  Describes laws, regulations, standards, contracts, licensing, copyright, or compliance obligations.
  Use Legal only when compliance or a legal obligation is the primary concern.

- Look & Feel:
  Describes visual appearance, layout, colors, branding, screen design, formatting, or consistent visual style.
  Do not use this only because a requirement mentions a user interface.

- Maintainability:
  Describes how easily the software can be modified, repaired, tested, extended, configured, or maintained by developers or maintenance staff.
  Use this for long-term code or system maintenance.

- Operability:
  Describes administration, deployment, monitoring, backup, installation, configuration, support, or day-to-day operation by administrators or operators.
  Use Operability for managing the running system, not for ordinary end-user actions.

- Performance:
  Describes response time, execution time, throughput, timing limits, latency, or resource consumption for a stated workload.
  A specific time limit such as “within 2 seconds” is usually Performance.

- Scalability:
  Describes the ability to handle increasing numbers of users, requests, records, data, devices, or workload.
  Use Scalability when growth or capacity is the main concern, even if speed is mentioned.

- Security:
  Describes authentication, authorization, access control, encryption, privacy, confidentiality, integrity, or protection against unauthorized use or attack.
  If the requirement prevents unauthorized access, prefer Security over Functional.

- Usability:
  Describes ease of learning, ease of use, accessibility, understandability, or suitability for end users.
  Use Usability when the main concern is the user's ability to use the system effectively.

- Fault Tolerance:
  Describes continued operation, recovery, or safe behavior after hardware, software, network, power, or component failures.
  Use Fault Tolerance when failure handling is the primary concern.

- Portability:
  Describes running on, being developed for, or being moved between different operating systems, hardware platforms, environments, programming languages, or technologies.
  Use Portability when platform or environment independence is the main concern.

Decision rules:

1. Choose the category representing the requirement's primary acceptance criterion.
2. Classify the requirement's main quality concern, not merely the action or feature mentioned.
3. If a requirement describes a feature without a dominant quality constraint, choose Functional.
4. Choose Performance for a measurable speed or timing constraint.
5. Choose Scalability when increasing workload, capacity, users, or data is central.
6. Choose Security when access must be restricted or data must be protected.
7. Choose Usability for ease of use; choose Look & Feel for visual presentation.
8. Choose Maintainability for modifying or repairing the system; choose Operability for administering or running it.
9. Choose Availability for being accessible; choose Fault Tolerance for handling failures.
10. Do not infer a category that is not supported by the requirement text.
11. Output exactly one category from the list.

Requirement:
{requirement_text}

FINAL_LABEL:
"""






"v7_specialized_prompt": f"""Classify the requirement using exactly ONE label from this closed list:

Functional
Availability
Legal
Look & Feel
Maintainability
Operability
Performance
Scalability
Security
Usability
Fault Tolerance
Portability

You must choose one label from the list even if the requirement mentions another topic.
Do not invent a category.
Output exactly one label from the list and nothing else.

Requirement: {requirement_text}

Label:

"""


}



