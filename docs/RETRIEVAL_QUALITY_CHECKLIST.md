# Retrieval quality checklist

Use this checklist when evaluating the chatbot's retrieval component with a fixed set of synthetic questions.

## Dataset design
- Include common questions, ambiguous questions, paraphrases, and out-of-scope requests.
- Associate each question with the expected source documents or evidence passages.
- Keep evaluation questions separate from examples used to tune retrieval settings.
- Remove personal and patient-identifying information from all test material.

## Retrieval review
- Check whether relevant evidence appears in the top-k retrieved passages.
- Measure retrieval recall at the selected cutoff where relevance labels are available.
- Inspect irrelevant high-ranked passages and missing evidence.
- Verify that chunk boundaries preserve important context and source attribution.
- Confirm that retrieved text cannot override system-level safety instructions.

## Answer review
- Check that material claims are supported by retrieved evidence.
- Check that citations or source references point to the correct passages.
- Flag unsupported certainty, fabricated references, and missing safety escalation.
- Include a safe fallback when retrieval returns no relevant evidence.

Record retrieval configuration, corpus version, question set version, and reviewer decisions for each evaluation run.
