from playwright.sync_api import sync_playwright
import tempfile
import os


def runtime_test(html_content):

    issues = []

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".html",
        mode="w",
        encoding="utf-8"
    ) as f:

        f.write(html_content)

        temp_path = f.name

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page(
                viewport={
                    "width": 1280,
                    "height": 900
                }
            )

            # =====================
            # JS ERROR TRACKING
            # =====================

            js_errors = []

            page.on(
                "pageerror",
                lambda e: js_errors.append(str(e))
            )

            # =====================
            # ALERT / POPUP CHECK
            # =====================

            alerts = []

            def handle_dialog(dialog):

                alerts.append(
                    dialog.message
                )

                dialog.dismiss()

            page.on(
                "dialog",
                handle_dialog
            )

            # =====================
            # LOAD GAME
            # =====================

            page.goto(
                f"file:///{temp_path}"
            )

            page.wait_for_timeout(3000)

            # =====================
            # TAKE SCREENSHOT
            # =====================

            page.screenshot(
                path="debug_game.png"
            )

            # =====================
            # BODY CHECK
            # =====================

            body_text = page.locator(
                "body"
            ).inner_text()

            if len(body_text.strip()) == 0:

                issues.append(
                    "Blank screen detected"
                )

            # =====================
            # BASIC DOM CHECK
            # =====================

            canvas_count = page.locator(
                "canvas"
            ).count()

            dom_count = page.locator(
                "div, button, canvas"
            ).count()

            if canvas_count == 0 and dom_count == 0:

                issues.append(
                    "No visible game elements"
                )

            # =====================
            # OVERSIZED LAYOUT CHECK
            # =====================

            large_elements = page.evaluate("""
() => {

    const elements = [
        ...document.querySelectorAll('*')
    ];

    return elements.filter(el => {

        const rect = el.getBoundingClientRect();

        return (
            rect.width > window.innerWidth * 2 ||
            rect.height > window.innerHeight * 2
        );

    }).length;

}
""")

            if large_elements > 0:

                issues.append(
                    "Broken oversized layout detected"
                )

            # =====================
            # INPUT TESTS
            # =====================

            keys = [
                "ArrowUp",
                "ArrowDown",
                "ArrowLeft",
                "ArrowRight",
                "Space"
            ]

            for key in keys:

                try:

                    page.keyboard.press(key)

                except:

                    pass

            try:

                page.mouse.click(
                    500,
                    400
                )

            except:

                pass

            page.wait_for_timeout(2000)

            # =====================
            # HTML LOWER
            # =====================

            html_lower = html_content.lower()

            # =====================
            # JS ERROR CHECK
            # =====================

            if len(js_errors) > 0:

                issues.append(
                    "JavaScript runtime errors"
                )

            # =====================
            # ALERT CHECK
            # =====================

            if len(alerts) > 0:

                issues.append(
                    "Game uses blocking alert popups"
                )

            # =====================
            # INPUT SYSTEM CHECK
            # =====================

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

            # =====================
            # GAMEPLAY SYSTEM CHECK
            # =====================

            has_game_loop = (
                "requestanimationframe" in html_lower
                or
                "setinterval" in html_lower
            )

            has_ui_interactions = (
                "click" in html_lower
                or
                "addeventlistener" in html_lower
            )

            if not has_game_loop and not has_ui_interactions:

                issues.append(
                    "No gameplay system detected"
                )

            # =====================
            # RESTART CHECK
            # =====================

            if (
                "restart" not in html_lower
                and
                "play again" not in html_lower
            ):

                issues.append(
                    "Restart system missing"
                )

            browser.close()

    except Exception as e:

        issues.append(str(e))

    finally:

        if os.path.exists(temp_path):

            os.remove(temp_path)

    return issues