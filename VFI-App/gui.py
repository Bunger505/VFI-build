"""Tkinter front end for the Project Victor daily intelligence briefing.

This module deliberately owns presentation only.  The Advisor keeps making
football decisions, while the terminal is responsible for displaying them.
Future pages, audio and a typewriter animation can be added without changing
the existing backend modules.
"""

from __future__ import annotations

from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext

from advisor import Advisor


APP_TITLE = "PROJECT VICTOR"
APP_SUBTITLE = "FOOTBALL INTELLIGENCE DIRECTORATE"
BACKGROUND = "#050b05"
PANEL_BACKGROUND = "#091309"
GREEN = "#76ff76"
GREEN_DIM = "#39a839"
AMBER = "#f4c95d"
FONT = "Consolas"


class VictorTerminal:
    """Desktop shell for today's Victor briefing.

    The page registry makes the next phase straightforward: add a page
    method, register it, and expose it through navigation when needed.
    """

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.advisor = Advisor()
        self.transmission_number = 1

        self.root.title(APP_TITLE)
        self.root.geometry("900x700")
        self.root.minsize(700, 520)
        self.root.configure(bg=BACKGROUND)
        self.root.protocol("WM_DELETE_WINDOW", self.exit_terminal)

        self._build_layout()
        self.show_daily_brief()

    def _build_layout(self) -> None:
        """Create the reusable terminal chrome and the briefing viewport."""
        container = tk.Frame(self.root, bg=BACKGROUND, padx=22, pady=18)
        container.pack(fill="both", expand=True)

        title_frame = tk.Frame(
            container,
            bg=PANEL_BACKGROUND,
            highlightbackground=GREEN_DIM,
            highlightthickness=1,
            padx=16,
            pady=12,
        )
        title_frame.pack(fill="x")

        tk.Label(
            title_frame,
            text=APP_TITLE,
            font=(FONT, 20, "bold"),
            fg=GREEN,
            bg=PANEL_BACKGROUND,
        ).pack(anchor="w")
        tk.Label(
            title_frame,
            text=APP_SUBTITLE,
            font=(FONT, 10, "bold"),
            fg=AMBER,
            bg=PANEL_BACKGROUND,
        ).pack(anchor="w", pady=(3, 0))

        self.transmission_label = tk.Label(
            title_frame,
            font=(FONT, 9),
            fg=GREEN_DIM,
            bg=PANEL_BACKGROUND,
            justify="left",
        )
        self.transmission_label.pack(anchor="w", pady=(9, 0))

        self.briefing_text = scrolledtext.ScrolledText(
            container,
            wrap="word",
            font=(FONT, 12),
            bg=BACKGROUND,
            fg=GREEN,
            insertbackground=GREEN,
            relief="flat",
            borderwidth=0,
            padx=16,
            pady=16,
            state="disabled",
        )
        self.briefing_text.pack(fill="both", expand=True, pady=(14, 14))

        controls = tk.Frame(container, bg=BACKGROUND)
        controls.pack(fill="x")

        self._button(controls, "[ REFRESH TRANSMISSION ]", self.refresh).pack(
            side="left"
        )
        self._button(controls, "[ EXIT TERMINAL ]", self.exit_terminal).pack(
            side="right"
        )

        tk.Label(
            container,
            text="CLASSIFICATION: CLUB CONFIDENTIAL  //  BADGE FIRST. ALWAYS.",
            font=(FONT, 8),
            fg=GREEN_DIM,
            bg=BACKGROUND,
        ).pack(pady=(12, 0))

    def _button(self, parent: tk.Widget, label: str, command) -> tk.Button:
        """Return a consistently styled terminal control."""
        return tk.Button(
            parent,
            text=label,
            command=command,
            font=(FONT, 10, "bold"),
            fg=BACKGROUND,
            bg=GREEN,
            activeforeground=BACKGROUND,
            activebackground=AMBER,
            relief="flat",
            borderwidth=0,
            padx=12,
            pady=8,
            cursor="hand2",
        )

    def show_daily_brief(self) -> None:
        """Render today's Advisor report in the terminal viewport."""
        timestamp = datetime.now().strftime("%d %b %Y // %H:%M")
        self.transmission_label.configure(
            text=(
                f"TRANSMISSION: #{self.transmission_number:06d}\n"
                f"STATUS: RECEIVED // DATE: {timestamp}"
            )
        )

        daily_brief = self.advisor.morning_brief()
        message = (
            "INCOMING DAILY BRIEF\n"
            + "=" * 58
            + "\n\n"
            + daily_brief
            + "\n\n"
            + "=" * 58
            + "\nEND TRANSMISSION"
        )
        self._set_briefing(message)

    def refresh(self) -> None:
        """Request a fresh wording of the briefing from the existing Advisor."""
        self.transmission_number += 1
        self.show_daily_brief()

    def _set_briefing(self, message: str) -> None:
        self.briefing_text.configure(state="normal")
        self.briefing_text.delete("1.0", tk.END)
        self.briefing_text.insert("1.0", message)
        self.briefing_text.configure(state="disabled")
        self.briefing_text.yview_moveto(0)

    def exit_terminal(self) -> None:
        """Close the desktop application cleanly."""
        self.root.destroy()

    def run(self) -> None:
        """Hand control to Tkinter's event loop."""
        self.root.mainloop()
