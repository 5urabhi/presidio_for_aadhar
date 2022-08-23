from presidio_analyzer import AnalyzerEngine
analyzer = AnalyzerEngine()
results = analyzer.analyze(text="My aadhar number is 9021 0123 5673; phone number is 1234554321", language="en")

print(f"Result:\n {results}")
