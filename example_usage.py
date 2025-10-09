"""
Example usage of the Unity Coefficient Algorithm (UCA).

This script demonstrates how to use the love-is-the-key package to analyze
digital content and interactions for alignment with unity consciousness.
"""

from love_is_the_key import get_unity_report
import json


def print_report(title: str, text: str):
    """Helper function to print a formatted report."""
    print(f"\n{'='*70}")
    print(f"ANALYSIS: {title}")
    print(f"{'='*70}")
    print(f"\nInput Text:\n\"{text}\"")
    
    report = get_unity_report(text)
    
    print(f"\n--- Unity Coefficient Report ---")
    print(f"Coefficient: {report.coefficient}")
    print(f"Analysis Method: {report.analysis_method}")
    print(f"\nSeparation Markers Found: {len(report.separation_hits)}")
    for marker, count in report.separation_hits.items():
        print(f"  - {marker}: {count}")
    
    print(f"\nUnity Markers Found: {len(report.unity_hits)}")
    for marker, count in report.unity_hits.items():
        print(f"  - {marker}: {count}")
    
    print(f"\nConscious Reframing:")
    print(f"  {report.conscious_reframing}")
    
    print(f"\n--- JSON Output (for LLM/API integration) ---")
    print(json.dumps(report.model_dump(), indent=2))


if __name__ == "__main__":
    print("Unity Coefficient Algorithm - Example Usage")
    print("=" * 70)
    
    # Example 1: High Unity Content
    print_report(
        "High Unity Content",
        "We can co-create a world of love, abundance, and possibility through "
        "collaboration and shared understanding. Together, we manifest harmony."
    )
    
    # Example 2: Separation-Based Content
    print_report(
        "Separation-Based Content",
        "Fear and crisis dominate our world. The lack and scarcity we face "
        "create conflict and division among us."
    )
    
    # Example 3: Balanced Content
    print_report(
        "Balanced Content",
        "While we face challenges and fear, we can transform them through "
        "love, unity, and conscious co-creation."
    )
    
    # Example 4: Code Comment Analysis
    print_report(
        "Code Comment Analysis",
        "# This function enables collaborative problem-solving through shared "
        "resources and collective intelligence."
    )
    
    # Example 5: Policy Statement Analysis
    print_report(
        "Policy Statement Analysis",
        "Our organization values inclusive decision-making, open communication, "
        "and the empowerment of all team members to contribute their unique gifts."
    )
    
    print(f"\n{'='*70}")
    print("Analysis Complete")
    print(f"{'='*70}\n")
