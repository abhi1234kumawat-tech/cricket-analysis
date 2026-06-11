import json
from datetime import date

def ipl_json_generator():

    print("=" * 45)
    print("       IPL DATA — JSON GENERATOR")
    print("=" * 45)

    standings  = []
    invalid    = []
    no_matches = []

    for i in range(5):
        print(f"\n--- Enter details for Team {i + 1} ---")

        team_name = input("  Team name       : ").strip()

        try:
            matches = int(input("  Matches played  : "))
            wins    = int(input("  Wins            : "))
            losses  = int(input("  Losses          : "))
        except ValueError:
            print("  Invalid input: please enter numeric values")
            return

        # ── Edge Cases ───────────────────────────────────────
        if matches == 0:
            no_matches.append({
                "team"   : team_name,
                "status" : "No match played yet"
            })
            continue

        if wins > matches:
            invalid.append({
                "team"   : team_name,
                "reason" : f"Wins ({wins}) cannot exceed matches played ({matches})"
            })
            continue

        if losses > matches:
            invalid.append({
                "team"   : team_name,
                "reason" : f"Losses ({losses}) cannot exceed matches played ({matches})"
            })
            continue

        if wins + losses > matches:
            invalid.append({
                "team"   : team_name,
                "reason" : f"Wins + Losses ({wins + losses}) cannot exceed matches played ({matches})"
            })
            continue

        points = wins * 2
        nrr    = round((wins - losses) / matches, 3)

        standings.append({
            "team"           : team_name,
            "matches_played" : matches,
            "wins"           : wins,
            "losses"         : losses,
            "points"         : points,
            "nrr"            : nrr
        })

    # ── Sort by Points then NRR ──────────────────────────────
    standings = sorted(standings, key=lambda x: (x["points"], x["nrr"]), reverse=True)

    for rank, team in enumerate(standings, start=1):
        team["rank"] = rank

    # ── Build JSON ───────────────────────────────────────────
    ipl_data = {
        "ipl_points_table": {
            "season"          : "2026",
            "last_updated"    : str(date.today()),
            "standings"       : standings,
            "no_match_played" : no_matches,
            "invalid_entries" : invalid
        }
    }

    # ── Save to File ─────────────────────────────────────────
    with open("ipl_data.json", "w") as f:
        json.dump(ipl_data, f, indent=2)

    print("\n")
    print("=" * 45)
    print("       JSON DATA SAVED SUCCESSFULLY")
    print("=" * 45)
    print(f"  File          : ipl_data.json")
    print(f"  Teams saved   : {len(standings)}")
    print(f"  Invalid teams : {len(invalid)}")
    print(f"  No matches    : {len(no_matches)}")
    print("=" * 45)
    print("\n  Preview:")
    print(json.dumps(ipl_data, indent=2))


ipl_json_generator()