"""
Unit tests for the Unity Coefficient Algorithm (UCA).

These tests verify the UCA logic works as intended for clear-cut examples,
ensuring code reliability (≥95% certainty).
"""

import pytest
from love_is_the_key import get_unity_report, UnityReport


class TestUnityReport:
    """Test the UnityReport data model."""
    
    def test_unity_report_structure(self):
        """Test that UnityReport has all required fields."""
        report = UnityReport(
            coefficient=0.75,
            analysis_method="V1: Keyword Lexicon Density",
            separation_hits={"fear": 1},
            unity_hits={"love": 3},
            conscious_reframing="Test reframing"
        )
        
        assert report.coefficient == 0.75
        assert report.analysis_method == "V1: Keyword Lexicon Density"
        assert report.separation_hits == {"fear": 1}
        assert report.unity_hits == {"love": 3}
        assert report.conscious_reframing == "Test reframing"
    
    def test_unity_report_coefficient_bounds(self):
        """Test that coefficient is bounded between 0.0 and 1.0."""
        with pytest.raises(ValueError):
            UnityReport(
                coefficient=1.5,  # Invalid: > 1.0
                analysis_method="Test",
                separation_hits={},
                unity_hits={},
                conscious_reframing="Test"
            )
        
        with pytest.raises(ValueError):
            UnityReport(
                coefficient=-0.1,  # Invalid: < 0.0
                analysis_method="Test",
                separation_hits={},
                unity_hits={},
                conscious_reframing="Test"
            )


class TestV1KeywordCalculate:
    """Test the V1 Keyword Lexicon Adapter."""
    
    def test_pure_unity_text(self):
        """Test text with only unity markers."""
        text = "We can co-create a world of love, abundance, and possibility through collaboration."
        report = get_unity_report(text)
        
        assert report.coefficient == 1.0
        assert report.analysis_method == "V1: Keyword Lexicon Density"
        assert len(report.unity_hits) > 0
        assert len(report.separation_hits) == 0
        assert "High Unity Alignment" in report.conscious_reframing
    
    def test_pure_separation_text(self):
        """Test text with only separation markers."""
        # Note: "impossible" contains "possible" which is a unity marker
        text = "Fear and crisis dominate our world through lack and scarcity and conflict."
        report = get_unity_report(text)
        
        assert report.coefficient < 0.3  # Should be low, but may not be exactly 0.0
        assert report.analysis_method == "V1: Keyword Lexicon Density"
        assert len(report.separation_hits) > 0
        assert "separation logic" in report.conscious_reframing
    
    def test_balanced_text(self):
        """Test text with equal unity and separation markers."""
        text = "There is fear and crisis but also love and hope."
        report = get_unity_report(text)
        
        assert 0.3 <= report.coefficient <= 0.7  # Should be approximately balanced
        assert report.analysis_method == "V1: Keyword Lexicon Density"
        assert len(report.separation_hits) > 0
        assert len(report.unity_hits) > 0
    
    def test_neutral_text(self):
        """Test text with no markers."""
        text = "The quick brown fox jumps over the lazy dog."
        report = get_unity_report(text)
        
        assert report.coefficient == 0.5  # Neutral baseline
        assert report.analysis_method == "V1: Keyword Lexicon Density"
        assert len(report.separation_hits) == 0
        assert len(report.unity_hits) == 0
    
    def test_case_insensitivity(self):
        """Test that the algorithm is case-insensitive."""
        text_lower = "love and unity"
        text_upper = "LOVE AND UNITY"
        text_mixed = "LoVe AnD uNiTy"
        
        report_lower = get_unity_report(text_lower)
        report_upper = get_unity_report(text_upper)
        report_mixed = get_unity_report(text_mixed)
        
        assert report_lower.coefficient == report_upper.coefficient == report_mixed.coefficient
        assert report_lower.unity_hits == report_upper.unity_hits == report_mixed.unity_hits
    
    def test_marker_counting(self):
        """Test that markers are counted correctly."""
        text = "love love love fear"
        report = get_unity_report(text)
        
        assert report.unity_hits["love"] == 3
        assert report.separation_hits["fear"] == 1
        assert report.coefficient == 0.75  # 3 / (3 + 1)
    
    def test_high_unity_threshold(self):
        """Test the high unity threshold (>= 0.75)."""
        text = "love unity abundance"  # 3 unity markers, 0 separation
        report = get_unity_report(text)
        
        assert report.coefficient >= 0.75
        assert "High Unity Alignment" in report.conscious_reframing
    
    def test_balanced_threshold(self):
        """Test the balanced threshold (>= 0.5)."""
        text = "love fear"  # 1 unity, 1 separation
        report = get_unity_report(text)
        
        assert 0.5 <= report.coefficient < 0.75
        assert "Balanced Alignment" in report.conscious_reframing
    
    def test_separation_threshold(self):
        """Test the separation threshold (< 0.5)."""
        text = "fear crisis lack"  # 0 unity, 3 separation
        report = get_unity_report(text)
        
        assert report.coefficient < 0.5
        assert "separation logic" in report.conscious_reframing


class TestGetUnityReport:
    """Test the main entry point function."""
    
    def test_returns_unity_report(self):
        """Test that get_unity_report returns a UnityReport object."""
        text = "Test text with love and unity"
        report = get_unity_report(text)
        
        assert isinstance(report, UnityReport)
    
    def test_empty_string(self):
        """Test handling of empty string."""
        text = ""
        report = get_unity_report(text)
        
        assert report.coefficient == 0.5  # Neutral baseline
        assert len(report.separation_hits) == 0
        assert len(report.unity_hits) == 0
    
    def test_json_serialization(self):
        """Test that the report can be serialized to JSON."""
        text = "love and unity"
        report = get_unity_report(text)
        
        json_str = report.model_dump_json()
        assert isinstance(json_str, str)
        assert "coefficient" in json_str
        assert "analysis_method" in json_str

