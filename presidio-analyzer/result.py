from presidio_analyzer import AnalyzerEngine
analyzer = AnalyzerEngine()
results = analyzer.analyze(text="My AADHAR Number is 543221351123", language="en")
print("Result:")
print(results)
