from pydantic import BaseModel
from typing import Dict, Any

class TestCase(BaseModel):
    id: int
    input: Dict[str, Any]  # Dynamic input structure
    expected: Any          # Flexible output type
    description: str

class ProblemAnalysis(BaseModel):
    variables: list[str]
    constraints: list[str]
    input_format: str
    output_format: str