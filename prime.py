def ipl_points_table():

    print("=" * 50)
    print("        IPL CRICKET POINTS TABLE")
    print("=" * 50)

    try:
        num_teams = int(input("Enter number of teams: "))
    except ValueError:
        print("Invalid input: please enter a numeric value")
        return

    teams = []

    for i in range(num_teams):
        print(f"\n--- Enter details for Team {i + 1} ---")

        team_name = input("  Team name          : ").strip()

        try:
            matches_played = int(input("  Matches played     : "))
            wins           = int(input("  Wins               : "))
            losses         = int(input("  Losses             : "))
            rain_points    = int(input("  Rain affected games: "))
        except ValueError:
            print("  Invalid input: please enter numeric values")
            return

        # ── Edge Cases ───────────────────────────────────────
        if matches_played == 0:
            print(f"\n  Status : {team_name} — No points (no matches played)")
            teams.append({
                "name"   : team_name,
                "played" : 0,
                "wins"   : 0,
                "losses" : 0,
                "rain"   : 0,
                "points" : 0,
                "nrr"    : 0.000
            })
            continue

        if wins > matches_played:
            print(f"\n  Status : {team_name} — Not possible (wins > matches played)")
            return

        if losses > matches_played:
            print(f"\n  Status : {team_name} — Not possible (losses > matches played)")
            return

        if wins + losses > matches_played:
            print(f"\n  Status : {team_name} — Not possible (wins + losses > matches played)")
            return

        # ── Points Calculation ───────────────────────────────
        points = (wins * 2) + (rain_points * 1)

        teams.append({
            "name"   : team_name,
            "played" : matches_played,
            "wins"   : wins,
            "losses" : losses,
            "rain"   : rain_points,
            "points" : points,
            "nrr"    : round((wins - losses) / matches_played, 3)
        })

    # ── Sort by Points then NRR ──────────────────────────────
    teams = sorted(teams, key=lambda x: (x["points"], x["nrr"]), reverse=True)

    # ── Display Table ────────────────────────────────────────
    print("\n")
    print("=" * 70)
    print("               IPL 2024 — POINTS TABLE")
    print("=" * 70)
    print(f"  {'#':<4} {'Team':<15} {'P':<6} {'W':<6} {'L':<6} {'Rain':<6} {'Pts':<6} {'NRR'}")
    print("-" * 70)

    for rank, team in enumerate(teams, start=1):
        print(f"  {rank:<4} {team['name']:<15} {team['played']:<6} {team['wins']:<6} "
              f"{team['losses']:<6} {team['rain']:<6} {team['points']:<6} {team['nrr']}")

    print("=" * 70)
    print(f"  🏆 Table Leader : {teams[0]['name']} with {teams[0]['points']} points")
    print("=" * 70)


ipl_points_table()
