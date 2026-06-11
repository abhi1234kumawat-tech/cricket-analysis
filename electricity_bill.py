def calculate_electricity_bill():
    try:
        units = float(input("Enter the total electricity units consumed: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return

    if units < 0:
        print("its not possible")
        return
    elif units == 0:
        print("no electricity used")
        return

    bill_breakdown = []
    total_amount = 0
    remaining_units = units

    # First 100 units
    if remaining_units > 0:
        slab1_units = min(remaining_units, 100)
        slab1_cost = slab1_units * 3
        total_amount += slab1_cost
        bill_breakdown.append(f"0 - 100 units: {slab1_units:.2f} units * 3 Rs = {slab1_cost:.2f} Rs")
        remaining_units -= slab1_units

    # Next 200 units (101 to 300)
    if remaining_units > 0:
        slab2_units = min(remaining_units, 200)
        slab2_cost = slab2_units * 5
        total_amount += slab2_cost
        bill_breakdown.append(f"101 - 300 units: {slab2_units:.2f} units * 5 Rs = {slab2_cost:.2f} Rs")
        remaining_units -= slab2_units

    # Above 300 units
    if remaining_units > 0:
        slab3_cost = remaining_units * 7
        total_amount += slab3_cost
        bill_breakdown.append(f"Above 300 units: {remaining_units:.2f} units * 7 Rs = {slab3_cost:.2f} Rs")

    print("\n--- ELECTRICITY BILL BREAKDOWN ---")
    print(f"Total Units Consumed: {units:.2f}")
    print("-" * 34)
    for line in bill_breakdown:
        print(line)
    print("-" * 34)
    print(f"Total Amount Payable: {total_amount:.2f} Rs")

calculate_electricity_bill()
