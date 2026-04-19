#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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


def main() -> None:
    print("=== Garden Temperature ===")
    print("")

    test_temperature()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
