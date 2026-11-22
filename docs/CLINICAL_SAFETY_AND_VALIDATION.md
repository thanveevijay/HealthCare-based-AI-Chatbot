# Clinical Safety and Validation Boundaries

This project is an educational healthcare-assistant prototype. It is not a medical device and must not be used as the sole basis for diagnosis, triage, or treatment decisions.

## User-facing boundaries

- Clearly state that generated content is informational and does not replace a qualified healthcare professional.
- Do not claim that a chatbot response confirms or rules out a disease.
- Do not present a rule-based symptom score as a clinically validated triage score.
- If a user describes potentially life-threatening symptoms, prioritize clear emergency-care guidance rather than routine self-care suggestions.
- Avoid delaying urgent care with long questionnaires or repeated chatbot interactions.

## Evidence and retrieval

- Preserve the source identifier and relevant excerpt for every retrieved clinical passage.
- Distinguish retrieved evidence from model-generated explanation.
- Do not invent citations or imply that a source supports a claim it does not contain.
- Keep source version and retrieval configuration available for audit and reproducibility.
- Review the knowledge base for outdated, contradictory, or geographically inapplicable guidance.

## Validation before any real-world use

A research evaluation should include:

1. A documented intended-use statement and explicit exclusions.
2. Expert review of symptom categories, severity rules, and emergency escalation language.
3. Testing on representative, appropriately governed data with patient-level separation.
4. Subgroup analysis to identify uneven performance and failure modes.
5. Calibration and uncertainty evaluation, not only accuracy.
6. Human-factors testing to check whether users misunderstand risk labels or over-trust generated advice.
7. Privacy, security, and incident-response review.

Do not describe the system as clinically validated, production-ready for patient care, or safe for autonomous triage without appropriate independent evidence and regulatory review.

## Data protection

Do not commit API keys, patient information, conversation exports, or other secrets. Use environment variables or a managed secret store for credentials. Minimize retained personal data and define access, retention, and deletion policies before handling real patient information.
