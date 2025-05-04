import os

PDF_DIR = "literature/pdf"
NOTES_DIR = "literature/notes"
TEMPLATE = """# {title}

**Problem / Goal:**  
_What challenge or question is this paper tackling?_

**Key Idea:**  
_What’s the central technique, algorithm, or insight?_

**Resource Counts:**  
_E.g., # qubits, circuit depth, classical compute time._

**Results / Speed-Up Claim:**  
_What performance improvement or result is claimed?_

**Limits / Open Questions:**  
_What assumptions, tradeoffs, or gaps remain?_

**Relevance to My RQ:**  
_How does this connect to your own research question?_
"""

def generate_notes():
    os.makedirs(NOTES_DIR, exist_ok=True)
    for filename in os.listdir(PDF_DIR):
        if filename.lower().endswith(".pdf"):
            base_name = os.path.splitext(filename)[0]
            note_path = os.path.join(NOTES_DIR, f"{base_name}.md")
            if not os.path.exists(note_path):
                with open(note_path, "w") as f:
                    f.write(TEMPLATE.format(title=base_name.replace('_', ' ')))
                print(f"Created: {note_path}")
            else:
                print(f"Skipped (already exists): {note_path}")

if __name__ == "__main__":
    generate_notes()