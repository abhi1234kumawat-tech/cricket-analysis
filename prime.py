def predict_win_probability():

    print("=" * 40)
    print("   CRICKET WIN PROBABILITY PREDICTOR")
    print("=" * 40)

    try:
        target        = int(input("Enter target runs      : "))
        current_score = int(input("Enter current score    : "))
        balls_left    = int(input("Enter balls remaining  : "))
        wickets_left  = int(input("Enter wickets remaining: "))
    except ValueError:
        print("Invalid input: please enter numeric values")
        return

    # ── Edge Cases ───────────────────────────────────────────
    if balls_left == 0:
        print("\n  Status : Match Finished")
        return

    if wickets_left == 0:
        print("\n  Status : Well played guys")
        return

    if current_score >= target:
        print("\n  Status : Chill guys we are Win 🏆")
        return

    runs_needed = target - current_score
    overs_left  = round(balls_left / 6, 2)

    if current_score == 0 or (40 - balls_left) == 0:
        current_rr = 0.0
    else:
        balls_bowled = 120 - balls_left
        current_rr   = round((current_score / balls_bowled) * 6, 2)

    required_rr = round((runs_needed / balls_left) * 6, 2)

    # ── Pressure Score ───────────────────────────────────────
    wicket_pressure = round((10 - wickets_left) / 10 * 100, 2)
    rr_pressure     = round((required_rr / current_rr) * 10, 2) if current_rr != 0 else 100.0

    # ── Win Probability Logic ────────────────────────────────
    base_prob = 100.0

    # RR factor
    if required_rr <= 6:
        base_prob -= 10
    elif required_rr <= 8:
        base_prob -= 25
    elif required_rr <= 10:
        base_prob -= 40
    elif required_rr <= 12:
        base_prob -= 60
    else:
        base_prob -= 80

    # Wicket factor
    if wickets_left >= 7:
        base_prob += 15
    elif wickets_left >= 5:
        base_prob += 5
    elif wickets_left >= 3:
        base_prob -= 15
    else:
        base_prob -= 30

    # Balls factor
    if balls_left >= 60:
        base_prob += 10
    elif balls_left >= 30:
        base_prob += 0
    else:
        base_prob -= 15

    win_prob  = max(0, min(100, round(base_prob, 2)))
    lose_prob = round(100 - win_prob, 2)

    # ── Final Prediction ─────────────────────────────────────
    if win_prob >= 60:
        prediction = "Strong Win Chance 💪🏏"
    elif win_prob >= 40:
        prediction = "Match is Wide Open ⚖️"
    elif win_prob >= 20:
        prediction = "Tough Chase Ahead 😬"
    else:
        prediction = "Try Best Next Time 😔"

    # ── Output ───────────────────────────────────────────────
    print("=" * 40)
    print("         MATCH ANALYSIS REPORT")
    print("=" * 40)
    print(f"  Target Score     : {target}")
    print(f"  Current Score    : {current_score}")
    print(f"  Runs Needed      : {runs_needed}")
    print(f"  Balls Remaining  : {balls_left}")
    print(f"  Overs Remaining  : {overs_left}")
    print(f"  Wickets Left     : {wickets_left}")
    print("-" * 40)
    print("         RUN RATE ANALYSIS")
    print("-" * 40)
    print(f"  Current Run Rate : {current_rr}")
    print(f"  Required Run Rate: {required_rr}")
    print("-" * 40)
    print("         PRESSURE ANALYSIS")
    print("-" * 40)
    print(f"  Wicket Pressure  : {wicket_pressure}%")
    print(f"  RR Pressure      : {rr_pressure}")
    print("-" * 40)
    print("         FINAL PREDICTION")
    print("-" * 40)
    print(f"  Win Probability  : {win_prob}%")
    print(f"  Lose Probability : {lose_prob}%")
    print(f"  Prediction       : {prediction}")
    print("=" * 40)


predict_win_probability()