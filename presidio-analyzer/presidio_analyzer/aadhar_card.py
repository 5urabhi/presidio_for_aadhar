from typing import Optional, List

from presidio_analyzer import Pattern, PatternRecognizer


class AadharCardRecognizer(PatternRecognizer):

    PATTERNS = [
        Pattern(
            "Aadhar Card (weak)",
            r"[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}",
            0.2,
        ),
        Pattern(
            "Aadhar Card (Medium)",
            r"[0-9]{4}\s[0-9]{4}\s[0-9]{4}",
            0.5,
        ),
    ]

    CONTEXT = [
       "AADHAR_NUMBER","AADHAR Number", "aadhar number", "aadhar_number", "aadhar id", "aadhar_id", "Aadhar id", "Aadhar ID"
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "Aadhar Card",
    ):
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )

