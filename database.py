import os
import sqlite3

if os.path.isfile("game_data.db"):
    conn = sqlite3.connect("game_data.db")
    print("Database exists. Skipping initial commands.")
    cursor = conn.cursor()
else:
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()

    statements = [
        """CREATE TABLE IF NOT EXISTS easy (
        highest_score INTEGER,
        current_tier INTEGER
        );""",
        """CREATE TABLE IF NOT EXISTS medium (
        highest_score INTEGER,
        current_tier INTEGER
        );""",
        """CREATE TABLE IF NOT EXISTS hard (
        highest_score INTEGER,
        current_tier INTEGER
        );"""
    ]

    for statement in statements:
        cursor.execute(statement)

    initial_values = [
        ("easy", 200, 0),
        ("medium", 200, 0),
        ("hard", 200, 0),
    ]

    for level, score, tier in initial_values:
        cursor.execute(f"""
            INSERT INTO {level} (highest_score, current_tier)
            VALUES (?, ?)
        """, (score, tier))

    conn.commit()


def get_highest_score(level):
    """Retrieves the highest score for the specified level."""
    cursor.execute(f"SELECT highest_score FROM {level}")
    return cursor.fetchone()[0]


def update_highest_score(level, new_score):
    """Updates the highest score for the specified level."""
    cursor.execute(f"UPDATE {level} SET highest_score = ?", (new_score,))
    conn.commit()


def get_current_tier(level):
    """Retrieves the current tier for the specified level."""
    cursor.execute(f"SELECT current_tier FROM {level}")
    return cursor.fetchone()[0]


def update_current_tier(level, new_tier):
    """Updates the current tier for the specified level."""
    cursor.execute(f"UPDATE {level} SET current_tier = ?", (new_tier,))
    conn.commit()
