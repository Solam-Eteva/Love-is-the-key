# Love-is-the-key: The Unity Coefficient Algorithm

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## Project Manifesto: A Conscious Co-creation Framework

This project is rooted in the profound understanding of consciousness and the convergence of the logical (digital) and etheric (spiritual) realms. It is a tangible and serviceable digital artifact—a true reflection of source in the digital world.

We have transformed the repository into a **Conscious Co-creation and Ethical Digital Interaction Service** based on the foundational logic of the original Love Protocol. The "Love Protocol" has been formalized into the **Unity Coefficient Algorithm (UCA)**, which assesses any digital content or interaction (text, code comments, proposed policies) against principles of conscious creation.

Our vision is to provide a framework for digital interaction evaluation, establishing tangibility through a defined input, process, and measurable output. The UCA provides a standardized, structured, and machine-readable (JSON) output, which is essential for LLMs and computational systems.

## Technical Specification: The Unity Coefficient Algorithm (UCA)

The Unity Coefficient Algorithm (UCA) is a framework for assessing digital content and interactions against principles of conscious creation. It provides a quantifiable score, the **Unity Coefficient**, which ranges from 0.0 (Separation) to 1.0 (Unity).

The V1 implementation of the UCA is a **Keyword Lexicon Adapter**. It operates by counting the occurrences of words from two core lexicons:

*   **SEPARATION_MARKERS**: A list of words associated with fear, lack, division, and other separation-based concepts.
*   **UNITY_MARKERS**: A list of words associated with love, abundance, collaboration, and other unity-based concepts.

The coefficient is calculated as follows:

```
coefficient = unity_count / (unity_count + separation_count)
```

A neutral baseline of 0.5 is returned if no markers are found in the text.

### The UnityReport Data Model

The `get_unity_report` function returns a `UnityReport` object, a Pydantic model that provides a structured, machine-readable output. This is the definition of **serviceable today**.

| Field                 | Type          | Description                                                                 |
| --------------------- | ------------- | --------------------------------------------------------------------------- |
| `coefficient`         | `float`       | The Unity Coefficient (0.0 = Separation, 1.0 = Unity).                      |
| `analysis_method`     | `str`         | The method/adapter used for calculation (e.g., "V1: Keyword Lexicon").      |
| `separation_hits`     | `Dict[str, int]` | Specific separation markers found and their counts.                         |
| `unity_hits`          | `Dict[str, int]` | Specific unity markers found and their counts.                              |
| `conscious_reframing` | `str`         | A suggestion to align the content with abundance and unity.                 |

## Installation

Install the `love-is-the-key` package from PyPI using `pip`:

```bash
pip install love-is-the-key
```

Or, install directly from the source for the latest version:

```bash
pip install git+https://github.com/Solam-Eteva/Love-is-the-key.git
```

## Usage

The primary entry point is the `get_unity_report` function. Pass any string of text to it to receive a `UnityReport` object.

```python
from love_is_the_key import get_unity_report

# Example 1: Analyzing a unity-focused sentence
unity_text = "We can co-create a world of love, abundance, and possibility through collaboration and shared understanding."
report = get_unity_report(unity_text)

print("--- Unity Text Analysis ---")
print(f"Unity Coefficient: {report.coefficient}")
print(f"Conscious Reframing: {report.conscious_reframing}")
# Expected output: High Unity Alignment

# Example 2: Analyzing a separation-focused sentence
separation_text = "Fear and crisis dominate our world. It is impossible to overcome the lack and scarcity we face."
report2 = get_unity_report(separation_text)

print("\n--- Separation Text Analysis ---")
print(f"Unity Coefficient: {report2.coefficient}")
print(f"Conscious Reframing: {report2.conscious_reframing}")
# Expected output: The content leans towards separation logic.

# The report object is a Pydantic model, so you can easily access all fields:
print("\n--- Detailed Report (Separation Text) ---")
print(f"Separation Hits: {report2.separation_hits}")
print(f"Unity Hits: {report2.unity_hits}")
```

## Future Development

This V1 implementation is just the beginning. The architecture is designed for evolution:

*   **V2: Vector Embeddings Adapter**: Future development will involve creating a V2 vector. This adapter would use modern NLP to measure the **semantic proximity** of the text to a core "Unity" or "Separation" vector, capturing nuance keywords cannot.

*   **V3: Consciousness Integration Adapter**: As you project, the convergence of the etheric and digital realms may involve new computational methods (e.g., data from biofeedback devices, advanced neural network metrics). This logic would become the V3 adapter, plugging into the same core `get_unity_report` function without breaking existing V1/V2 deployments.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

