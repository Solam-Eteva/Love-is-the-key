"""
Context-Aware Consciousness Evaluation Module

This module provides context intelligence for the Unity Coefficient Algorithm,
ensuring that consciousness evaluation is informative rather than restrictive.

Philosophy:
- Illuminate, don't restrict
- Inform, don't impose
- Suggest, don't demand
- Learn, don't judge
- Respect sovereignty always

The goal is to provide awareness of consciousness patterns while honoring
creative expression, artistic license, and human sovereignty.
"""

from typing import Dict, List, Optional, Any
from enum import Enum
from dataclasses import dataclass


class ContentType(Enum):
    """Types of content that require different consciousness evaluation approaches."""
    FICTION = "fiction"
    HORROR = "horror"
    COMEDY = "comedy"
    SATIRE = "satire"
    TECHNICAL = "technical"
    BUSINESS = "business"
    PERSONAL = "personal"
    ACADEMIC = "academic"
    SPIRITUAL = "spiritual"
    ARTISTIC = "artistic"
    JOURNALISTIC = "journalistic"
    UNKNOWN = "unknown"


@dataclass
class ContentContext:
    """
    Represents the detected context of content being analyzed.
    
    Attributes:
        content_type: The primary type of content
        genre: Specific genre if applicable (e.g., "horror", "romance")
        intent: Detected intent (e.g., "artistic", "educational", "commercial")
        audience: Target audience if detectable
        creative_license: Whether creative/artistic freedom applies
        confidence: Confidence in context detection (0.0 to 1.0)
        metadata: Additional context information
    """
    content_type: ContentType
    genre: Optional[str] = None
    intent: Optional[str] = None
    audience: Optional[str] = None
    creative_license: bool = False
    confidence: float = 0.0
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class ContextDetector:
    """
    Detects content context to enable appropriate consciousness evaluation.
    
    This detector uses pattern matching and heuristics to understand what
    type of content is being analyzed, allowing the Unity Coefficient to
    be interpreted correctly.
    """
    
    # Fiction indicators
    FICTION_INDICATORS = [
        "chapter", "protagonist", "character", "plot", "story", "novel",
        "narrative", "scene", "dialogue", "narrator", "fiction"
    ]
    
    # Horror genre indicators
    HORROR_INDICATORS = [
        "horror", "terror", "fear", "scream", "blood", "death", "monster",
        "nightmare", "haunted", "ghost", "zombie", "vampire", "demon"
    ]
    
    # Comedy/Satire indicators
    COMEDY_INDICATORS = [
        "comedy", "humor", "joke", "funny", "satire", "parody", "irony",
        "sarcasm", "wit", "amusing", "hilarious", "laugh"
    ]
    
    # Technical indicators
    TECHNICAL_INDICATORS = [
        "function", "class", "method", "algorithm", "implementation",
        "documentation", "api", "code", "syntax", "compile", "debug"
    ]
    
    # Academic indicators
    ACADEMIC_INDICATORS = [
        "abstract", "methodology", "hypothesis", "research", "study",
        "analysis", "conclusion", "bibliography", "citation", "peer-reviewed"
    ]
    
    # Artistic indicators
    ARTISTIC_INDICATORS = [
        "artistic", "creative", "expression", "art", "poetry", "prose",
        "metaphor", "symbolism", "imagery", "aesthetic"
    ]
    
    def detect(self, text: str, user_context: Optional[Dict] = None) -> ContentContext:
        """
        Detect the context of the given text.
        
        Args:
            text: The text to analyze for context
            user_context: Optional user-provided context hints
            
        Returns:
            ContentContext with detected information
        """
        text_lower = text.lower()
        
        # If user explicitly provides context, trust it
        if user_context:
            return self._build_from_user_context(user_context)
        
        # Detect content type through pattern matching
        content_type, confidence = self._detect_content_type(text_lower)
        genre = self._detect_genre(text_lower, content_type)
        intent = self._detect_intent(text_lower, content_type)
        creative_license = self._has_creative_license(content_type, genre)
        
        return ContentContext(
            content_type=content_type,
            genre=genre,
            intent=intent,
            creative_license=creative_license,
            confidence=confidence
        )
    
    def _detect_content_type(self, text: str) -> tuple[ContentType, float]:
        """Detect the primary content type with confidence score."""
        scores = {}
        
        # Calculate scores for each type
        scores[ContentType.FICTION] = self._calculate_indicator_score(
            text, self.FICTION_INDICATORS
        )
        scores[ContentType.HORROR] = self._calculate_indicator_score(
            text, self.HORROR_INDICATORS
        )
        scores[ContentType.COMEDY] = self._calculate_indicator_score(
            text, self.COMEDY_INDICATORS
        )
        scores[ContentType.TECHNICAL] = self._calculate_indicator_score(
            text, self.TECHNICAL_INDICATORS
        )
        scores[ContentType.ACADEMIC] = self._calculate_indicator_score(
            text, self.ACADEMIC_INDICATORS
        )
        scores[ContentType.ARTISTIC] = self._calculate_indicator_score(
            text, self.ARTISTIC_INDICATORS
        )
        
        # Find highest scoring type
        if not scores or max(scores.values()) < 0.1:
            return ContentType.UNKNOWN, 0.0
        
        best_type = max(scores, key=scores.get)
        confidence = min(scores[best_type], 1.0)
        
        return best_type, confidence
    
    def _calculate_indicator_score(self, text: str, indicators: List[str]) -> float:
        """Calculate how strongly the text matches a set of indicators."""
        if not indicators:
            return 0.0
        
        matches = sum(1 for indicator in indicators if indicator in text)
        return matches / len(indicators)
    
    def _detect_genre(self, text: str, content_type: ContentType) -> Optional[str]:
        """Detect specific genre within content type."""
        if content_type in [ContentType.FICTION, ContentType.ARTISTIC]:
            if any(indicator in text for indicator in self.HORROR_INDICATORS):
                return "horror"
            if any(indicator in text for indicator in self.COMEDY_INDICATORS):
                return "comedy"
        return None
    
    def _detect_intent(self, text: str, content_type: ContentType) -> Optional[str]:
        """Detect the intent behind the content."""
        if content_type in [ContentType.FICTION, ContentType.ARTISTIC, ContentType.HORROR]:
            return "artistic"
        elif content_type == ContentType.TECHNICAL:
            return "educational"
        elif content_type == ContentType.ACADEMIC:
            return "research"
        return None
    
    def _has_creative_license(self, content_type: ContentType, genre: Optional[str]) -> bool:
        """Determine if creative license should be respected."""
        creative_types = [
            ContentType.FICTION,
            ContentType.HORROR,
            ContentType.COMEDY,
            ContentType.SATIRE,
            ContentType.ARTISTIC
        ]
        return content_type in creative_types or genre in ["horror", "comedy", "satire"]
    
    def _build_from_user_context(self, user_context: Dict) -> ContentContext:
        """Build ContentContext from user-provided information."""
        content_type_str = user_context.get("type", "unknown")
        try:
            content_type = ContentType(content_type_str)
        except ValueError:
            content_type = ContentType.UNKNOWN
        
        return ContentContext(
            content_type=content_type,
            genre=user_context.get("genre"),
            intent=user_context.get("intent"),
            creative_license=user_context.get("creative_license", False),
            confidence=1.0,  # User-provided context is trusted
            metadata=user_context
        )


class ConsciousnessContextualizer:
    """
    Applies context intelligence to consciousness metrics.
    
    This class adjusts how unity coefficients are interpreted and presented
    based on the detected context, ensuring that artistic expression is
    respected and consciousness evaluation remains informative rather than
    restrictive.
    """
    
    def __init__(self):
        self.detector = ContextDetector()
    
    def contextualize_coefficient(
        self,
        coefficient: float,
        text: str,
        user_context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Add context intelligence to a unity coefficient.
        
        Args:
            coefficient: The raw unity coefficient (0.0 to 1.0)
            text: The analyzed text
            user_context: Optional user-provided context
            
        Returns:
            Dictionary with contextualized analysis
        """
        context = self.detector.detect(text, user_context)
        
        return {
            "raw_coefficient": coefficient,
            "context": context,
            "interpretation": self._interpret_coefficient(coefficient, context),
            "notes": self._generate_contextual_notes(coefficient, context),
            "reframing_appropriate": self._should_suggest_reframing(coefficient, context),
            "creative_license_respected": context.creative_license
        }
    
    def _interpret_coefficient(self, coefficient: float, context: ContentContext) -> str:
        """Generate context-aware interpretation of the coefficient."""
        if context.creative_license:
            if context.content_type == ContentType.HORROR:
                return (
                    f"Unity Coefficient: {coefficient:.2f} (Genre: Horror Fiction)\n"
                    "Low coefficient expected for this genre. Creative license respected."
                )
            elif context.content_type == ContentType.COMEDY:
                return (
                    f"Unity Coefficient: {coefficient:.2f} (Genre: Comedy/Satire)\n"
                    "Coefficient reflects comedic/satirical intent. Creative expression honored."
                )
            else:
                return (
                    f"Unity Coefficient: {coefficient:.2f} (Artistic Expression)\n"
                    "Creative license recognized. No restrictions applied."
                )
        
        # Standard interpretation for non-creative content
        if coefficient >= 0.75:
            return f"Unity Coefficient: {coefficient:.2f} - High unity alignment"
        elif coefficient >= 0.5:
            return f"Unity Coefficient: {coefficient:.2f} - Balanced alignment"
        else:
            return f"Unity Coefficient: {coefficient:.2f} - Separation-leaning patterns detected"
    
    def _generate_contextual_notes(self, coefficient: float, context: ContentContext) -> List[str]:
        """Generate helpful contextual notes."""
        notes = []
        
        if context.creative_license:
            notes.append("✓ Creative license respected")
            notes.append("✓ No restrictions applied")
            notes.append("✓ Artistic expression honored")
            
            if context.content_type == ContentType.HORROR:
                notes.append("Note: Horror genre naturally employs separation themes for emotional impact")
            elif context.content_type == ContentType.COMEDY:
                notes.append("Note: Comedy/satire often uses contrast and conflict for humorous effect")
        else:
            if coefficient < 0.5:
                notes.append("Observation: Content shows separation-based patterns")
                notes.append("Suggestion: Alternative framing available if desired")
            elif coefficient >= 0.75:
                notes.append("Observation: Strong unity consciousness present")
                notes.append("Recognition: Content promotes collaborative awareness")
        
        if context.confidence < 0.5:
            notes.append(f"Note: Context detection confidence is {context.confidence:.0%}")
            notes.append("Tip: You can provide explicit context for more accurate analysis")
        
        return notes
    
    def _should_suggest_reframing(self, coefficient: float, context: ContentContext) -> bool:
        """
        Determine if reframing suggestions are appropriate.
        
        Never suggest reframing for creative/artistic content.
        Only suggest for business/technical content with low coefficients.
        """
        if context.creative_license:
            return False
        
        if context.content_type in [ContentType.BUSINESS, ContentType.TECHNICAL]:
            return coefficient < 0.5
        
        # For other content, only suggest if very low
        return coefficient < 0.3


def detect_context(text: str, user_context: Optional[Dict] = None) -> ContentContext:
    """
    Convenience function to detect content context.
    
    Args:
        text: The text to analyze
        user_context: Optional user-provided context hints
        
    Returns:
        ContentContext with detected information
    """
    detector = ContextDetector()
    return detector.detect(text, user_context)


def contextualize_analysis(
    coefficient: float,
    text: str,
    user_context: Optional[Dict] = None
) -> Dict[str, Any]:
    """
    Convenience function to add context intelligence to consciousness analysis.
    
    Args:
        coefficient: The unity coefficient
        text: The analyzed text
        user_context: Optional user-provided context
        
    Returns:
        Dictionary with contextualized analysis
    """
    contextualizer = ConsciousnessContextualizer()
    return contextualizer.contextualize_coefficient(coefficient, text, user_context)

