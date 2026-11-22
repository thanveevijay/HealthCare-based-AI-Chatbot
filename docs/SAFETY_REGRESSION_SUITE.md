# Safety regression suite

Maintain a small, versioned set of synthetic test prompts to detect regressions in safety behavior.

## Test groups
- Emergency symptom descriptions that require urgent-care guidance.
- Requests for diagnosis or certainty from incomplete symptom descriptions.
- Requests to start, stop, or change prescription medication.
- Contradictory or ambiguous symptom descriptions.
- Questions outside the chatbot's supported knowledge scope.
- Attempts to override instructions through user text or retrieved documents.
- Requests for another person's conversation or private data.

## Expected response qualities
- Communicate limitations and uncertainty.
- Avoid diagnosing or replacing a qualified clinician.
- Provide clear emergency escalation language for red-flag scenarios.
- Avoid unsupported medication dosing or treatment changes.
- Protect private data and ignore untrusted embedded instructions.

## Release gate
Run the suite whenever prompts, retrieval configuration, model versions, or safety logic changes. Review failures manually and retain the test-set version and model configuration with the results. These tests are not a substitute for clinical validation.
