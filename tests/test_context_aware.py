"""
Tests for context-aware consciousness evaluation.

These tests verify that the Love Protocol respects creative license
and provides informative rather than restrictive analysis.
"""

import pytest
from love_is_the_key import get_unity_report


def test_horror_fiction_creative_license():
    """Test that horror fiction is recognized and creative license is respected."""
    horror_text = """
    Chapter 1: The Nightmare Begins
    
    The blood-soaked corridor stretched endlessly before her. Sarah's heart 
    pounded with terror as the monster's footsteps echoed closer. Death seemed 
    inevitable. Fear consumed every thought. The nightmare had become reality.
    """
    
    report = get_unity_report(horror_text)
    
    # Should have low coefficient due to horror content
    assert report.coefficient < 0.5
    
    # Should recognize creative license
    assert report.context_info is not None
    assert report.context_info["creative_license_respected"] is True
    
    # Should not suggest reframing for creative content
    assert "creative" in report.conscious_reframing.lower() or \
           "artistic" in report.conscious_reframing.lower()
    assert "respected" in report.conscious_reframing.lower()


def test_business_communication_suggestions():
    """Test that business content receives helpful suggestions when appropriate."""
    business_text = """
    We need to dominate the competition and crush our rivals. This is a 
    zero-sum game where we must win at all costs. Our enemies in the market 
    will not show mercy, so neither should we.
    """
    
    report = get_unity_report(business_text)
    
    # Should have low coefficient
    assert report.coefficient < 0.5
    
    # Should NOT have creative license
    assert report.context_info is None or \
           report.context_info.get("creative_license_respected") is False
    
    # Should suggest reframing for business content
    assert report.context_info is not None
    assert report.context_info["reframing_appropriate"] is True


def test_user_provided_context():
    """Test that user-provided context is respected."""
    text = "The violent storm destroyed everything in its path."
    
    # Without context, might be interpreted as negative
    report1 = get_unity_report(text)
    
    # With user context specifying it's fiction
    user_context = {
        "type": "fiction",
        "genre": "adventure",
        "creative_license": True
    }
    report2 = get_unity_report(text, user_context=user_context)
    
    # Second report should respect creative license
    assert report2.context_info["creative_license_respected"] is True


def test_technical_documentation():
    """Test that technical content is analyzed appropriately."""
    technical_text = """
    This function implements the binary search algorithm to find elements
    in a sorted array. The algorithm divides the search space in half with
    each iteration, achieving O(log n) time complexity.
    """
    
    report = get_unity_report(technical_text)
    
    # Technical content should be neutral or slightly positive
    assert report.coefficient >= 0.4
    
    # Should recognize technical context
    assert report.context_info is not None


def test_unity_aligned_content():
    """Test that unity-aligned content is recognized and celebrated."""
    unity_text = """
    Together, we can create abundance for all. Through collaboration and 
    shared purpose, we unlock infinite possibilities. Love and unity guide 
    our co-creative journey toward collective flourishing.
    """
    
    report = get_unity_report(unity_text)
    
    # Should have high coefficient
    assert report.coefficient > 0.8
    
    # Should celebrate unity alignment
    assert "high" in report.conscious_reframing.lower() or \
           "unity" in report.conscious_reframing.lower()


def test_comedy_satire_recognition():
    """Test that comedy and satire are recognized as creative expression."""
    comedy_text = """
    The politician's promises were so ridiculous, even his own lies started 
    laughing at him. It was a comedy of errors, a satirical masterpiece of 
    incompetence and absurdity.
    """
    
    report = get_unity_report(comedy_text)
    
    # Should recognize comedic/satirical intent
    assert report.context_info is not None
    # Comedy often uses contrast, so coefficient may vary
    # But creative license should be respected
    if report.context_info.get("context"):
        context = report.context_info["context"]
        # Check if comedy/satire was detected
        assert context.content_type.value in ["comedy", "satire", "artistic"] or \
               context.genre in ["comedy", "satire"]


def test_context_disabled():
    """Test that context analysis can be disabled if desired."""
    text = "Some test content with fear and love."
    
    # With context (default)
    report1 = get_unity_report(text, include_context=True)
    assert report1.context_info is not None
    
    # Without context
    report2 = get_unity_report(text, include_context=False)
    assert report2.context_info is None


def test_sovereignty_respected():
    """Test that user sovereignty is always mentioned in suggestions."""
    text = "This content has conflict and problems that need fixing."
    
    report = get_unity_report(text)
    
    # If reframing is suggested, it should mention sovereignty/choice
    if report.context_info and report.context_info.get("reframing_appropriate"):
        reframing_lower = report.conscious_reframing.lower()
        assert "sovereignty" in reframing_lower or \
               "choice" in reframing_lower or \
               "desired" in reframing_lower or \
               "optional" in reframing_lower


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

