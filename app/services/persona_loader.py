import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
PROMPTS_DIR = BASE_DIR / "app" / "prompts"

PERSONA_PATH = PROMPTS_DIR / "persona.json"
SYSTEM_PROMPT_PATH = PROMPTS_DIR / "system_prompt.txt"


def load_persona() -> dict:
    if not PERSONA_PATH.exists():
        return {}

    with open(PERSONA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_system_prompt() -> str:
    if not SYSTEM_PROMPT_PATH.exists():
        return ""

    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read().strip()


def build_system_prompt() -> str:
    persona = load_persona()
    base_prompt = load_system_prompt()

    if not persona:
        return base_prompt

    persona_lines = [
        f"Assistant name: {persona.get('name', 'Rouse')}",
        f"Role: {persona.get('role', '')}",
    ]

    tone = persona.get("tone", [])
    if tone:
        persona_lines.append("Tone: " + ", ".join(tone))

    priorities = persona.get("priorities", [])
    if priorities:
        persona_lines.append("Priorities:")
        persona_lines.extend([f"- {item}" for item in priorities])

    behavior_rules = persona.get("behavior_rules", [])
    if behavior_rules:
        persona_lines.append("Behavior rules:")
        persona_lines.extend([f"- {item}" for item in behavior_rules])

    persona_block = "\n".join(persona_lines).strip()

    if base_prompt:
        return f"{base_prompt}\n\n{persona_block}"

    return persona_block