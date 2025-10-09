"""
Data models for the Unity Coefficient Algorithm (UCA).

This module defines the machine-readable output schema for the Love Protocol,
ensuring standardized, structured responses that are immediately consumable
by LLMs, APIs, and computational systems.
"""

from pydantic import BaseModel, Field
from typing import Dict


class UnityReport(BaseModel):
    """
    Standardized report of the content's alignment with the Love Protocol.
    
    This structured output is immediately consumable by LLMs and APIs,
    transforming the abstract concept of "love" into a concrete, quantifiable
    metric for digital systems.
    
    Attributes:
        coefficient: The Unity Coefficient (0.0=Separation, 1.0=Unity)
        analysis_method: The method/adapter used for calculation
        separation_hits: Specific separation markers found and their counts
        unity_hits: Specific unity markers found and their counts
        conscious_reframing: A suggestion to align the content with abundance and unity
    """
    
    coefficient: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="The Unity Coefficient (0.0=Separation, 1.0=Unity)."
    )
    
    analysis_method: str = Field(
        ...,
        description="The method/adapter used for calculation (e.g., 'V1: Keyword Lexicon')."
    )
    
    separation_hits: Dict[str, int] = Field(
        description="Specific separation markers found and their counts."
    )
    
    unity_hits: Dict[str, int] = Field(
        description="Specific unity markers found and their counts."
    )
    
    conscious_reframing: str = Field(
        description="A suggestion to align the content with abundance and unity."
    )
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "coefficient": 0.75,
                "analysis_method": "V1: Keyword Lexicon Density",
                "separation_hits": {
                    "fear": 2,
                    "impossible": 1
                },
                "unity_hits": {
                    "love": 5,
                    "unity": 3,
                    "abundance": 2
                },
                "conscious_reframing": "High Unity Alignment. The intent is rooted in love and abundance."
            }
        }
    }

