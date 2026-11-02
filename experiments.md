# Experiment Log - Software Requirements Classification

| Date / Run | Prompt-version / Strategy | Accuracy | Macro F1 | Comments / Observations |
| :--- | :--- | :--- | :--- | :--- |
| Run 1 | First prompt (simple zero-shot) | 0.6594 | 0.1986 | Unbalanced classes. |
| Run 2 | Longer prompt with definitions of the categories | 0.6141 | 0.0634 | Syntax miss |
| Run 3 | Same prompt as above | 0.6214 | 0.2881 | Much better, syntax correct now and a lot better macro f1 score. |
| Run 4 | Added critical rule to the prompt | 0.3605 | 0.2105 | Tried to adjust so it does not just pick "Functional". But seems it was to big prompt for it to understand it since it lowered accuracy a lot! |
| Run 5 | Critical rule, but no definitions | 0.2029 | 0.1819 |  |
| Run 6 | Added guideline | 0.5851 | 0.2102 | Added a guidline for it to not just pick "Functional |
| Run 7 | "v4_cot" | 0.6359 | 0.2953 | Higher without category at the end of the prompt. |
| Run 8 | "v5_cot_best_prompt" | 0.6667 | 0.3325 | Changed the order of the categories in the prompt,
and resulted in higher accuracy and macro F1.  |
| Run 10 | v5_cot_best_prompt | 0.6395 | 0.3085 | Worse than before, did change in if statement and added invalid output and saw that the model is guessing at 12 completely different categories.
| Run 11 |  | 0.6630 | 0.2622 | Worse than before
| Run 12 | | 0.6630 | 0.2622 | Worse than before

