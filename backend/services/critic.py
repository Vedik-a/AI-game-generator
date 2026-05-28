def critique_game(html):

    issues = []

    html_lower = html.lower()

    # =========================
    # EMPTY UI CHECK
    # =========================

    if (
        'class="tile"' in html_lower
        and
        '>x<' not in html_lower
        and
        '>o<' not in html_lower
        and
        'textcontent' not in html_lower
        and
        'innertext' not in html_lower
    ):

        issues.append(
            "UI elements appear visually empty"
        )

    # =========================
    # GAME ENDING CHECK
    # =========================

    ending_patterns = [

        "game over",
        "winner",
        "win",
        "lose",
        "restart",
        "collision"

    ]

    has_ending = any(
        pattern in html_lower
        for pattern in ending_patterns
    )

    if not has_ending:

        issues.append(
            "No visible game ending logic"
        )

    # =========================
    # OBJECTIVE CHECK
    # =========================

    if (
        "score" not in html_lower
        and
        "goal" not in html_lower
        and
        "level" not in html_lower
    ):

        issues.append(
            "No clear gameplay objective"
        )

    # =========================
    # INTERACTION CHECK
    # =========================

    interaction_patterns = [

        "addeventlistener",
        "onclick",
        "click",
        "keydown",
        "keyup",
        "mousedown",
        "mousemove",
        "touchstart",
        "touchmove",
        "requestanimationframe",
        "setinterval"

    ]

    has_interaction = any(
        pattern in html_lower
        for pattern in interaction_patterns
    )

    if not has_interaction:

        issues.append(
            "No meaningful interactions detected"
        )

    # =========================
    # MOVEMENT / ACTIVITY CHECK
    # =========================

    movement_patterns = [

        "requestanimationframe",
        "setinterval",
        "velocity",
        "speed",
        "dx",
        "dy",
        "+=",
        "-="

    ]

    has_movement = any(
        pattern in html_lower
        for pattern in movement_patterns
    )

    gameplay_input_patterns = [

        "click",
        "keydown",
        "keyup",
        "mousedown",
        "touchstart"

    ]

    has_gameplay_input = any(
        pattern in html_lower
        for pattern in gameplay_input_patterns
    )

    if (
        not has_movement
        and
        not has_gameplay_input
    ):

        issues.append(
            "No gameplay activity detected"
        )

    # =========================
    # EMPTY CANVAS CHECK
    # =========================

    if (
        "<canvas" in html_lower
        and
        "fillrect" not in html_lower
        and
        "drawimage" not in html_lower
        and
        "arc(" not in html_lower
    ):

        issues.append(
            "Canvas appears visually empty"
        )

    # =========================
    # RESTART CHECK
    # =========================

    if (
        "restart" not in html_lower
        and
        "play again" not in html_lower
    ):

        issues.append(
            "No restart system detected"
        )

    # =========================
    # PLAYER INPUT CHECK
    # =========================

    has_keyboard = (
        "keydown" in html_lower
        or
        "keyup" in html_lower
    )

    has_mouse = (
        "click" in html_lower
        or
        "mousedown" in html_lower
        or
        "touchstart" in html_lower
    )

    if not has_keyboard and not has_mouse:

        issues.append(
            "No player input system detected"
        )

    # =========================
    # BAD CANVAS SCALING
    # =========================

    if (
        "canvas.width = window.innerwidth" in html_lower
        or
        "canvas.height = window.innerheight" in html_lower
    ):

        issues.append(
            "Canvas uses fullscreen scaling which breaks iframe layouts"
        )

    # =========================
    # OFFSCREEN RENDERING CHECK
    # =========================

    if (
        "translate(" in html_lower
        and
        "-9999" in html_lower
    ):

        issues.append(
            "Possible offscreen rendering detected"
        )

    # =========================
    # SCORE UPDATE CHECK
    # =========================

    score_update_patterns = [

        "score++",
        "score +=",
        "score -=",
        "score =",
        "textcontent",
        "innerhtml"

    ]

    has_score_update = any(
        pattern in html_lower
        for pattern in score_update_patterns
    )

    if (
        "score" in html_lower
        and
        not has_score_update
    ):

        issues.append(
            "Score exists but never updates"
        )

    # =========================
    # GAMEPLAY INTERACTION CHECK
    # =========================

    collision_patterns = [

        "collision",
        "intersects",
        "distance",
        "overlap",
        "hit",
        "touch"

    ]

    has_collision = any(
        pattern in html_lower
        for pattern in collision_patterns
    )

    has_game_loop = (
        "requestanimationframe" in html_lower
        or
        "setinterval" in html_lower
    )

    has_click_gameplay = (
        "click" in html_lower
        or
        "onclick" in html_lower
    )

    if (
        has_game_loop
        and
        not has_collision
        and
        not has_click_gameplay
    ):

        issues.append(
            "No gameplay interaction logic detected"
        )

    return issues