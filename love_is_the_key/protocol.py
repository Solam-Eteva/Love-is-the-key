"""
Core logic and lexicon for the Unity Coefficient Algorithm (UCA).

This module contains the intellectual foundation of the Love Protocol:
the carefully curated lexicons that distinguish separation-based consciousness
from unity-based consciousness, and the protocol adapters that calculate
the Unity Coefficient.
"""

from .models import UnityReport
from .context import detect_context, contextualize_analysis, ContentContext
from typing import List, Optional, Dict, Any

# --- The Core Lexicon (P3) ---
# This is the most vital step: the philosophical foundation that gives
# the V1 algorithm immediate, measurable value.

# **PLACEHOLDER 1: LEXICON EXPANSION** - This is the most vital step.
# These lists should be meticulously expanded to capture the full spectrum
# of separation and unity consciousness in language.

SEPARATION_MARKERS: List[str] = [
    # Core separation concepts
    "fear", "lack", "impossible", "us versus them", "judgement",
    "crisis", "scarcity", "division", "conflict", "enemy",
    
    # Expanded separation terms
    "zero-sum", "my way", "compete", "dominate", "control",
    "threat", "danger", "attack", "defend", "protect",
    "limited", "finite", "not enough", "mine", "yours",
    "separate", "isolated", "alone", "abandoned", "rejected",
    "failure", "loss", "defeat", "victim", "powerless",
    "hate", "anger", "resentment", "revenge", "punishment",
    "wrong", "bad", "evil", "sin", "guilt",
    "shame", "blame", "fault", "mistake", "error",
    "weak", "inferior", "less than", "unworthy", "inadequate",
    "impossible", "can't", "won't", "never", "hopeless",
    "desperate", "anxious", "worried", "stressed", "overwhelmed",
    "chaos", "disorder", "destruction", "collapse", "end",
    "death", "dying", "terminal", "fatal", "doomed",
    "exclusive", "elite", "superior", "better than", "privilege",
    "hierarchy", "rank", "status", "class", "caste",
    "border", "boundary", "wall", "barrier", "fence",
    "restriction", "limitation", "constraint", "prohibition", "ban",
    "competition", "rivalry", "opponent", "adversary", "foe",
]

UNITY_MARKERS: List[str] = [
    # Core unity concepts
    "love", "unity", "co-create", "abundance", "possibility",
    "solution", "harmony", "peace", "together", "collaboration",
    
    # Expanded unity terms
    "shared source", "potential", "oneness", "wholeness", "integration",
    "connection", "relationship", "bond", "link", "bridge",
    "infinite", "unlimited", "boundless", "endless", "eternal",
    "collective", "community", "all beings", "everyone", "humanity",
    "together", "united", "joined", "merged", "combined",
    "success", "victory", "triumph", "achievement", "accomplishment",
    "empowerment", "strength", "capability", "capacity", "ability",
    "compassion", "kindness", "care", "support", "help",
    "forgiveness", "acceptance", "understanding", "empathy", "sympathy",
    "right", "good", "virtue", "merit", "worth",
    "honor", "respect", "dignity", "value", "appreciation",
    "strong", "capable", "worthy", "deserving", "adequate",
    "possible", "can", "will", "always", "hopeful",
    "calm", "peaceful", "serene", "tranquil", "relaxed",
    "order", "harmony", "balance", "equilibrium", "stability",
    "life", "living", "vital", "vibrant", "thriving",
    "inclusive", "open", "welcoming", "accepting", "embracing",
    "equality", "fairness", "justice", "equity", "balance",
    "opening", "gateway", "portal", "passage", "access",
    "freedom", "liberty", "autonomy", "independence", "sovereignty",
    "cooperation", "partnership", "alliance", "synergy", "symbiosis",
    "trust", "faith", "belief", "confidence", "assurance",
    "joy", "happiness", "delight", "pleasure", "bliss",
    "gratitude", "thankfulness", "appreciation", "acknowledgment", "recognition",
    "growth", "development", "evolution", "progress", "advancement",
    "creation", "generation", "manifestation", "emergence", "birth",
    "light", "illumination", "clarity", "insight", "wisdom",
    "truth", "authenticity", "genuineness", "sincerity", "honesty",
    "beauty", "grace", "elegance", "refinement", "excellence",
]


# --- V1 Implementation: Keyword Lexicon Adapter (P4) ---

def v1_keyword_calculate(text: str) -> UnityReport:
    """
    V1 Protocol: Calculates Unity Coefficient based on simple keyword density.
    
    This is the immediate utility for LLMs via fast, quantifiable metrics.
    The algorithm counts occurrences of separation and unity markers in the text,
    then calculates a coefficient representing the balance between them.
    
    Args:
        text: The input text to analyze (can be content, code comments, policies, etc.)
        
    Returns:
        UnityReport: A structured report containing the coefficient and detailed analysis
        
    Algorithm:
        1. Convert text to lowercase for case-insensitive matching
        2. Count occurrences of each marker in both lexicons
        3. Calculate coefficient: unity_count / (unity_count + separation_count)
        4. Generate conscious reframing based on coefficient thresholds
    """
    text_lower = text.lower()
    separation_hits = {}
    unity_hits = {}
    
    # 1. Count Markers
    for marker in SEPARATION_MARKERS:
        count = text_lower.count(marker)
        if count > 0:
            separation_hits[marker] = count
    
    for marker in UNITY_MARKERS:
        count = text_lower.count(marker)
        if count > 0:
            unity_hits[marker] = count
    
    separation_count = sum(separation_hits.values())
    unity_count = sum(unity_hits.values())
    total_markers = separation_count + unity_count
    
    # 2. Calculate Coefficient
    if total_markers == 0:
        coefficient = 0.5  # Neutral baseline
    else:
        coefficient = unity_count / total_markers
    
    # 3. Conscious Reframing Logic
    if coefficient >= 0.75:
        reframing = "High Unity Alignment. The intent is rooted in love and abundance."
    elif coefficient >= 0.5:
        reframing = "Balanced Alignment. The potential for conscious co-creation is strong, requiring only slight reframing."
    else:
        # **PLACEHOLDER 2: REFRAMING ALGORITHM** - Future development point
        reframing = "The content leans towards separation logic. Re-evaluate the core premise from the perspective of our shared source and inherent abundance."
    
    return UnityReport(
        coefficient=round(coefficient, 4),
        analysis_method="V1: Keyword Lexicon Density",
        separation_hits=separation_hits,
        unity_hits=unity_hits,
        conscious_reframing=reframing
    )


# --- Main Entry Point ---

def get_unity_report(
    text: str,
    user_context: Optional[Dict] = None,
    include_context: bool = True
) -> UnityReport:
    """
    Primary function for external systems (LLMs, APIs) to call.
    
    This function provides context-aware consciousness evaluation that respects
    creative expression and human sovereignty. The analysis is informative
    rather than restrictive, illuminating consciousness patterns without
    imposing judgments or limitations.
    
    Args:
        text: The input text to analyze
        user_context: Optional context hints (type, genre, intent, etc.)
        include_context: Whether to include contextual analysis (default: True)
        
    Returns:
        UnityReport: A structured report with context-aware consciousness analysis
        
    Philosophy:
        - Illuminate, don't restrict
        - Inform, don't impose
        - Suggest, don't demand
        - Learn, don't judge
        - Respect sovereignty always
        
    Future Development:
        **PLACEHOLDER 3: ADAPTER SELECTION LOGIC** - When V2 (e.g., NLP or Vector
        Embeddings) is built, the logic here will dynamically switch to the more
        advanced adapter based on configuration.
    """
    # Get base unity coefficient using V1 algorithm
    base_report = v1_keyword_calculate(text)
    
    # If context awareness is disabled, return base report
    if not include_context:
        return base_report
    
    # Add context intelligence
    context_data = contextualize_analysis(
        coefficient=base_report.coefficient,
        text=text,
        user_context=user_context
    )
    
    # Enhance the report with contextual information
    enhanced_report = UnityReport(
        coefficient=base_report.coefficient,
        analysis_method=base_report.analysis_method,
        separation_hits=base_report.separation_hits,
        unity_hits=base_report.unity_hits,
        conscious_reframing=_generate_context_aware_reframing(
            base_report.conscious_reframing,
            context_data
        ),
        context_info=context_data
    )
    
    return enhanced_report


def _generate_context_aware_reframing(
    base_reframing: str,
    context_data: Dict[str, Any]
) -> str:
    """
    Generate context-aware reframing that respects creative license.
    
    Args:
        base_reframing: The original reframing suggestion
        context_data: Contextual analysis data
        
    Returns:
        Context-aware reframing message
    """
    context: ContentContext = context_data["context"]
    
    # For creative content, acknowledge and respect artistic expression
    if context.creative_license:
        return (
            f"{context_data['interpretation']}\n\n"
            f"Creative Expression Recognized:\n"
            f"Your artistic vision is respected. No reframing suggested.\n"
            f"The consciousness patterns detected are appropriate for {context.content_type.value} content."
        )
    
    # For non-creative content, provide helpful suggestions if appropriate
    if context_data["reframing_appropriate"]:
        return (
            f"{context_data['interpretation']}\n\n"
            f"Observation: {base_reframing}\n\n"
            f"Note: This is informational only. You have complete sovereignty "
            f"over your expression. Alternative framings are available if desired."
        )
    
    # For balanced or high-unity content
    return (
        f"{context_data['interpretation']}\n\n"
        f"{base_reframing}"
    )

