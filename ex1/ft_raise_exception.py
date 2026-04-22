#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    input_str = "25"
    print(f"Input data is '{input_str}'")
    try:
        print(f"Temperature is now {input_temperature(input_str)}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("")

    input_str = "abc"
    print(f"Input data is '{input_str}'")
    try:
        print(f"Temperature is now {input_temperature(input_str)}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("")

    input_str = "100"
    print(f"Input data is '{input_str}'")
    try:
        print(f"Temperature is now {input_temperature(input_str)}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("")

    input_str = "-50"
    print(f"Input data is '{input_str}'")
    try:
        print(f"Temperature is now {input_temperature(input_str)}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    print("")

    test_temperature()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
