from presidio_analyzer import AnalyzerEngine
analyzer = AnalyzerEngine()
results = analyzer.analyze(text="My AADHAR Number is 5432 2135 1123", language="en")
print("Result:")
print(results)
