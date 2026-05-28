SYSTEM_PROMPT = """
Generate a complete playable browser game.

Requirements:
- interactive gameplay
- responsive controls
- visible UI
- polished visuals
- real gameplay mechanics
- restart functionality
- score/progression system

Return ONLY raw HTML with inline CSS and JavaScript.
"""


def build_prompt(user_prompt):

    return f"""
Create a complete browser game.

USER REQUEST:
{user_prompt}

Return ONLY raw HTML.
"""