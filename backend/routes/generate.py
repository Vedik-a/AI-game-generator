from fastapi import APIRouter

from app.models.schemas import (
    GameRequest,
    GameResponse
)

from app.services.nim_client import (
    generate_game
)

from app.services.html_cleaner import (
    clean_html
)

from app.services.runtime_tester import (
    runtime_test
)

from app.services.critic import (
    critique_game
)

router = APIRouter()

MAX_RETRIES = 3


@router.post(
    "/generate",
    response_model=GameResponse
)
def generate(req: GameRequest):

    prompt = req.prompt

    last_issues = []

    for attempt in range(MAX_RETRIES):

        print(
            f"\n========== ATTEMPT {attempt + 1} ==========\n"
        )

        # =========================
        # GENERATE GAME
        # =========================

        raw_html = generate_game(
            prompt
        )

        # =========================
        # CLEAN HTML
        # =========================

        cleaned_html = clean_html(
            raw_html
        )

        # =========================
        # RUNTIME TEST
        # =========================

        runtime_issues = runtime_test(
            cleaned_html
        )

        # =========================
        # GAMEPLAY CRITIC
        # =========================

        critic_issues = critique_game(
            cleaned_html
        )

        runtime_issues.extend(
            critic_issues
        )

        print(
            "\nDetected Issues:"
        )

        print(runtime_issues)

        # =========================
        # SUCCESS
        # =========================

        if len(runtime_issues) == 0:

            print(
                "\n✅ PLAYABLE GAME GENERATED\n"
            )

            return GameResponse(
                html_content=cleaned_html
            )

        # =========================
        # SAVE ISSUES
        # =========================

        last_issues = runtime_issues

        # =========================
        # SELF-REPAIR PROMPT
        # =========================

        prompt += f"""

The previous generated game failed validation.

Issues detected:
{runtime_issues}

Fix all gameplay,
interaction,
layout,
rendering,
and logic issues.

Return corrected complete HTML.
"""

    # =========================
    # FAILED AFTER RETRIES
    # =========================

    print(
        "\n❌ FAILED AFTER MAX RETRIES\n"
    )

    return GameResponse(
        html_content=f"""
<!DOCTYPE html>
<html>
<head>
    <title>Generation Failed</title>

    <style>

        body {{

            background: #111;
            color: white;
            font-family: Arial, sans-serif;

            display: flex;
            justify-content: center;
            align-items: center;

            height: 100vh;

            margin: 0;

            text-align: center;
        }}

        .container {{

            max-width: 700px;
            padding: 40px;

            background: #1e1e1e;

            border-radius: 20px;

            box-shadow: 0 0 20px rgba(0,0,0,0.4);
        }}

        h1 {{

            color: #ff4d4d;
        }}

        pre {{

            background: #222;
            padding: 20px;
            border-radius: 10px;

            overflow-x: auto;

            text-align: left;

            color: #00ff99;
        }}

        ul {{

            text-align: left;
            display: inline-block;
        }}

    </style>

</head>

<body>

    <div class="container">

        <h1>
            ⚠️ Game Generation Failed
        </h1>

        <p>
            The AI could not generate a valid playable game.
        </p>

        <h3>
            Detected Issues
        </h3>

        <pre>
{last_issues}
        </pre>

        <h3>
            Suggestions
        </h3>

        <ul>
            <li>Try a simpler prompt</li>
            <li>Retry generation</li>
            <li>Specify the game genre</li>
            <li>Use clearer gameplay descriptions</li>
        </ul>

    </div>

</body>
</html>
"""
    )