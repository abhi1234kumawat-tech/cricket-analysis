import json
from datetime import date


def validate_player(name, matches, runs, wickets):

    # ── Step 1: Edge Case Checks ─────────────────────────
    print(f"\n  🔍 Step 1 — Validating data for {name}...")

    if wickets < 0:
        print(f"  ❌ Invalid data: negative wickets not allowed")
        return "invalid", {
            "player" : name,
            "reason" : "Negative wickets not allowed"
        }

    if runs == 0 or matches == 0:
        print(f"  ⚠️  No runs scored — no match contribution recorded")
        return "no_match", {
            "player"  : name,
            "matches" : matches,
            "status"  : "No runs scored — no match played"
        }

    return "valid", None


def calculate_stats(name, matches, runs, wickets):

    # ── Step 2: Batting Average ──────────────────────────
    print(f"  🔍 Step 2 — Calculating batting average...")
    batting_avg = round(runs / matches, 2)
    print(f"  ✅ Batting Average  : {batting_avg}")

    # ── Step 3: Runs Per Match ───────────────────────────
    print(f"  🔍 Step 3 — Calculating runs per match...")
    runs_per_match = round(runs / matches, 2)
    print(f"  ✅ Runs per Match   : {runs_per_match}")

    # ── Step 4: Role Detection ───────────────────────────
    print(f"  🔍 Step 4 — Detecting player role...")
    if wickets == 0:
        role = "Pure Batsman 🏏"
    elif runs > 500 and wickets > 20:
        role = "All Rounder 🌟"
    elif wickets > 20:
        role = "Pure Bowler 🎯"
    else:
        role = "Batting All Rounder 🏏🎯"
    print(f"  ✅ Role Detected    : {role}")

    # ── Step 5: Performance Rating ───────────────────────
    print(f"  🔍 Step 5 — Calculating performance rating...")
    score = 0

    if batting_avg >= 50:
        score += 40
    elif batting_avg >= 35:
        score += 25
    elif batting_avg >= 20:
        score += 15
    else:
        score += 5

    if wickets >= 50:
        score += 40
    elif wickets >= 20:
        score += 25
    elif wickets >= 10:
        score += 15
    else:
        score += 5

    if matches >= 50:
        score += 20
    elif matches >= 20:
        score += 10
    else:
        score += 5

    if score >= 80:
        rating = "World Class ⭐⭐⭐⭐⭐"
    elif score >= 60:
        rating = "Excellent ⭐⭐⭐⭐"
    elif score >= 40:
        rating = "Good ⭐⭐⭐"
    elif score >= 20:
        rating = "Average ⭐⭐"
    else:
        rating = "Needs Improvement ⭐"

    print(f"  ✅ Performance      : {rating}")

    return {
        "name"              : name,
        "matches"           : matches,
        "runs"              : runs,
        "wickets"           : wickets,
        "batting_avg"       : batting_avg,
        "runs_per_match"    : runs_per_match,
        "role"              : role,
        "rating"            : rating,
        "performance_score" : score
    }
def collect_input():

    print("=" * 45)
    print("     CRICKET PLAYER STATS ANALYSER")
    print("=" * 45)

    try:
        num_players = int(input("Enter number of players: "))
    except ValueError:
        print("Invalid input: please enter numeric value")
        return

    players    = []
    invalid    = []
    no_matches = []

    for i in range(num_players):
        print(f"\n--- Player {i + 1} Details ---")

        name = input("  Player name     : ").strip()

        try:
            matches = int(input("  Matches played  : "))
            runs    = int(input("  Runs scored     : "))
            wickets = int(input("  Wickets taken   : "))
        except ValueError:
            print("  Invalid input: please enter numeric values")
            return

        status, result = validate_player(name, matches, runs, wickets)

        if status == "invalid":
            invalid.append(result)
            continue
        elif status == "no_match":
            no_matches.append(result)
            continue

        player_data = calculate_stats(name, matches, runs, wickets)
        players.append(player_data)

    display_and_save(players, invalid, no_matches)


def display_and_save(players, invalid, no_matches):

    # ── Sort by Performance Score ────────────────────────
    players = sorted(players, key=lambda x: x["performance_score"], reverse=True)

    for rank, p in enumerate(players, start=1):
        p["rank"] = rank

    # ── Terminal Breakdown ───────────────────────────────
    print("\n")
    print("=" * 55)
    print("           FINAL PLAYER STATS REPORT")
    print("=" * 55)

    for p in players:
        print(f"\n  Rank             : {p['rank']}")
        print(f"  Player           : {p['name']}")
        print(f"  Matches          : {p['matches']}")
        print(f"  Runs             : {p['runs']}")
        print(f"  Wickets          : {p['wickets']}")
        print(f"  Batting Average  : {p['batting_avg']}")
        print(f"  Runs per Match   : {p['runs_per_match']}")
        print(f"  Role             : {p['role']}")
        print(f"  Rating           : {p['rating']}")
        print("-" * 55)

    if no_matches:
        print("\n  ⚠️  No Match Players:")
        for n in no_matches:
            print(f"  → {n['player']} : {n['status']}")

    if invalid:
        print("\n  ❌ Invalid Entries:")
        for inv in invalid:
            print(f"  → {inv['player']} : {inv['reason']}")

    print("=" * 55)

    # ── Save to JSON ─────────────────────────────────────
    data = {
        "cricket_player_stats": {
            "generated_on"     : str(date.today()),
            "total_players"    : len(players),
            "standings"        : players,
            "no_match_players" : no_matches,
            "invalid_entries"  : invalid
        }
    }

    with open("player_stats.json", "w") as f:
        json.dump(data, f, indent=2)

    print(f"\n  ✅ Data saved to player_stats.json successfully!")
    print("=" * 55)


# ── Run Program ──────────────────────────────────────────
collect_input()