def validate_game(html: str):

    errors = []

    html_lower = html.lower()

    # =========================
    # BASIC HTML VALIDATION
    # =========================

    required_tags = [
        "<html",
        "<script",
        "</html>"
    ]

    for tag in required_tags:

        if tag not in html_lower:
            errors.append(f"Missing {tag}")

    # =========================
    # GAME LOOP CHECK
    # =========================

    if (
        "requestanimationframe" not in html_lower
        and
        "setinterval" not in html_lower
    ):
        errors.append("No game loop found")

    # =========================
    # CONTROL CHECK
    # =========================

    control_patterns = [
        "keydown",
        "keyup",
        "mousemove",
        "touchstart",
        "click"
    ]

    if not any(
        pattern in html_lower
        for pattern in control_patterns
    ):
        errors.append(
            "No gameplay controls found"
        )

    # =========================
    # SCORE SYSTEM CHECK
    # =========================

    score_patterns = [
        "score",
        "points",
        "highscore"
    ]

    if not any(
        pattern in html_lower
        for pattern in score_patterns
    ):
        errors.append(
            "No scoring system found"
        )

    # =========================
    # MOVEMENT CHECK
    # =========================

    movement_patterns = [
        "+=",
        "-=",
        "velocity",
        "speed",
        "dx",
        "dy"
    ]

    if not any(
        pattern in html
        for pattern in movement_patterns
    ):
        errors.append(
            "No movement system found"
        )

    # =========================
    # POPUP CHECK
    # =========================

    if "alert(" in html_lower:
        errors.append(
            "Uses alert popup"
        )

    # =========================
    # GAME SIZE CHECK
    # =========================

    if len(html) < 2000:
        errors.append(
            "Generated game too small"
        )

    # =========================
    # CANVAS / RENDERING CHECK
    # =========================

    rendering_patterns = [
        "<canvas",
        "getcontext",
        "svg",
        "webgl"
    ]

    if not any(
        pattern in html_lower
        for pattern in rendering_patterns
    ):
        errors.append(
            "No rendering system found"
        )

    # =========================
    # GAME STATE CHECK
    # =========================

    state_patterns = [
        "let ",
        "const ",
        "var "
    ]

    if not any(
        pattern in html
        for pattern in state_patterns
    ):
        errors.append(
            "No game state variables found"
        )

    # =========================
    # RETURN RESULT
    # =========================

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }