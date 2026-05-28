import re


def clean_html(html):

    # =========================
    # REMOVE MARKDOWN
    # =========================

    html = re.sub(
        r"```html",
        "",
        html,
        flags=re.IGNORECASE
    )

    html = re.sub(
        r"```",
        "",
        html
    )

    # =========================
    # REMOVE ALERT POPUPS
    # =========================

    html = re.sub(
        r"alert\s*\(.*?\)\s*;",
        "",
        html,
        flags=re.DOTALL
    )

    # =========================
    # FIX FULLSCREEN CANVAS
    # =========================

    html = html.replace(
        "window.innerWidth",
        "800"
    )

    html = html.replace(
        "window.innerHeight",
        "600"
    )

    # =========================
    # FORCE IFRAME SAFE BODY
    # =========================

    if "<body" in html.lower():

        html = re.sub(
            r"<body.*?>",
            """
<body style="
margin:0;
padding:0;
overflow:hidden;
display:flex;
justify-content:center;
align-items:center;
background:#111;
font-family:Arial;
">
""",
            html,
            flags=re.IGNORECASE | re.DOTALL
        )

    # =========================
    # AUTO ADD KEYBOARD SUPPORT
    # =========================

    if (
        "keydown" not in html.lower()
    ):

        keyboard_script = """

<script>

document.addEventListener(
    "keydown",
    function(e){

        console.log(
            "Key pressed:",
            e.key
        );

    }
);

</script>

"""

        html = html.replace(
            "</body>",
            keyboard_script + "</body>"
        )

    # =========================
    # AUTO ADD GAME LOOP
    # =========================

    if (
        "requestanimationframe" not in html.lower()
        and
        "setinterval" not in html.lower()
    ):

        animation_script = """

<script>

function autoLoop(){

    requestAnimationFrame(
        autoLoop
    );

}

autoLoop();

</script>

"""

        html = html.replace(
            "</body>",
            animation_script + "</body>"
        )

    # =========================
    # FIX MULTIPLE GAME LOOPS
    # =========================

    html = re.sub(
        r"requestAnimationFrame\s*\(\s*draw\s*\)",
        """
if(!window.__gameLoopRunning){

    window.__gameLoopRunning = true;

    requestAnimationFrame(draw);

}
""",
        html
    )

    # =========================
    # REMOVE BLOCKING GAME OVER
    # =========================

    html = html.replace(
        "gameOver = true;",
        """
gameOver = true;

console.log("Game Over");
"""
    )

    # =========================
    # PREVENT BODY OVERFLOW
    # =========================

    html = html.replace(
        "overflow: visible",
        "overflow: hidden"
    )

    # =========================
    # ENSURE CANVAS FITS SCREEN
    # =========================

    html += """

<style>

canvas{

    max-width:100vw !important;
    max-height:100vh !important;
    display:block;
    margin:auto;

}

</style>

"""

    return html.strip()