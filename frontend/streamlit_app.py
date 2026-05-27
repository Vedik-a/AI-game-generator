import streamlit as st
import streamlit.components.v1 as components

from api_client import generate_game

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Game Generator",
    layout="wide"
)

st.title("🎮 AI Game Generator")

# =========================
# USER INPUT
# =========================

prompt = st.text_area(
    "Describe your game idea",
    height=150,
    placeholder="""
Examples:
- Snake game
- Flappy bird
- Space shooter
- Racing game
"""
)

# =========================
# GENERATE BUTTON
# =========================

if st.button("Generate Game"):

    if not prompt.strip():

        st.warning(
            "Please enter a prompt."
        )

        st.stop()

    with st.spinner(
        "Generating your game..."
    ):

        try:

            result = generate_game(
                prompt
            )

            html_content = result[
                "html_content"
            ]

            st.success(
                "Game Generated!"
            )

            # =========================
            # SAVE GAME
            # =========================

            with open(
                "../generated_games/generated_game.html",
                "w",
                encoding="utf-8"
            ) as f:

                f.write(html_content)

            # =========================
            # TABS
            # =========================

            tab1, tab2 = st.tabs(
                [
                    "🎮 Play Game",
                    "🧠 View Code"
                ]
            )

            # =========================
            # PLAY GAME TAB
            # =========================

            with tab1:

                st.subheader(
                    "🎮 Play Game"
                )

                fixed_html = f"""
                <div
                    id="game-wrapper"
                    tabindex="0"
                    style="
                        width:100%;
                        height:100%;
                        outline:none;
                        overflow:hidden;
                    "
                >
                    {html_content}
                </div>

                <script>

                    const wrapper =
                        document.getElementById(
                            "game-wrapper"
                        );

                    // =====================
                    // FORCE FOCUS
                    // =====================

                    function forceFocus() {{

                        wrapper.focus();

                        window.focus();

                        document.body.focus();
                    }}

                    setTimeout(
                        forceFocus,
                        500
                    );

                    window.onload = forceFocus;

                    document.onclick = forceFocus;

                    // =====================
                    // GLOBAL KEYBOARD FIX
                    // =====================

                    const keys = [
                        "ArrowUp",
                        "ArrowDown",
                        "ArrowLeft",
                        "ArrowRight",
                        " ",
                        "w",
                        "a",
                        "s",
                        "d",
                        "W",
                        "A",
                        "S",
                        "D"
                    ];

                    document.addEventListener(
                        "keydown",
                        function(e) {{

                            if (
                                keys.includes(e.key)
                            ) {{

                                e.preventDefault();

                                const event =
                                    new KeyboardEvent(
                                        "keydown",
                                        {{
                                            key: e.key
                                        }}
                                    );

                                window.dispatchEvent(
                                    event
                                );

                                document.dispatchEvent(
                                    event
                                );
                            }}
                        }}
                    );

                </script>
                """

                components.html(
                    fixed_html,
                    height=900,
                    scrolling=False
                )

                # =========================
                # DOWNLOAD BUTTON
                # =========================

                st.download_button(
                    "⬇ Download Game HTML",
                    data=html_content,
                    file_name="generated_game.html",
                    mime="text/html"
                )

            # =========================
            # VIEW CODE TAB
            # =========================

            with tab2:

                st.subheader(
                    "🧠 Generated Source Code"
                )

                st.code(
                    html_content,
                    language="html"
                )

        except Exception as e:

            st.error(str(e))