# Knowledge Base Update Procedure

## Before an update
- Identify the source and owner of the proposed content.
- Check that the material is appropriate for the chatbot's informational scope.
- Review accuracy, publication date, and whether the source has been superseded.
- Remove unnecessary personal or sensitive information from ingestion inputs.

## Processing
1. Preserve source metadata such as title, publisher, and revision date.
2. Apply the documented text-cleaning and chunking process.
3. Rebuild embeddings or search indexes using the approved pipeline.
4. Run retrieval tests for representative questions.
5. Compare the updated index against the previous version.

## Release checks
- Verify that retrieved passages match the intended source.
- Test outdated, conflicting, and out-of-scope questions.
- Confirm that citations or source references are preserved where supported.
- Keep a rollback path to the last known-good knowledge base.

## Governance
Record the update date, source versions, processing configuration, reviewer, and release identifier. Clinical or safety-sensitive content should receive qualified review before publication.

A knowledge base update should improve traceability and retrieval quality without implying that the chatbot provides medical diagnosis or treatment.
