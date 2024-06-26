# Getting started with Presidio

## Simple flow

Using Presidio's modules as Python packages to get started

=== "Anonymize PII in text"

    1. Install Presidio
        
        ```sh
        pip install presidio-analyzer
        pip install presidio-anonymizer
        python -m spacy download en_core_web_lg
        ```
    
    2. Analyze + Anonymize
    
        ```py
        from presidio_analyzer import AnalyzerEngine
        from presidio_anonymizer import AnonymizerEngine
        
        text="My phone number is 212-555-5555"
        
        # Set up the engine, loads the NLP module (spaCy model by default) 
        # and other PII recognizers
        analyzer = AnalyzerEngine()
        
        # Call analyzer to get results
        results = analyzer.analyze(text=text,
                                   entities=["PHONE_NUMBER"],
                                   language='en')
        print(results)
        
        # Analyzer results are passed to the AnonymizerEngine for anonymization
        
        anonymizer = AnonymizerEngine()
        
        anonymized_text = anonymizer.anonymize(text=text,analyzer_results=results)
        
        print(anonymized_text)
        ```

=== "Anonymize PII in images"

    1. Install presidio-image-redactor
    
        ```sh
        pip install presidio-image-redactor
        ```
       
    2. Redact PII from image
    
        ```py
        from presidio_image_redactor import ImageRedactorEngine
        from PIL import Image
        
        image = Image.open(path_to_image_file)
        
        redactor = ImageRedactorEngine()
        redactor.redact(image=image)
        ```
---

## Read more

- [Installing Presidio](installation.md)
- [PII detection in text](analyzer/index.md)
- [PII anonymization in text](anonymizer/index.md)
- [PII redaction in images](image-redactor/index.md)
- [Discussion board](https://github.com/microsoft/presidio/discussions)
