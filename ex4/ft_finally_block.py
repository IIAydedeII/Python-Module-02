#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for name in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for name in ["Tomato", "lettuce", "Carrots"]:
            water_plant(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("")


def main() -> None:
    print("=== Garden Watering System ===")
    print("")

    test_watering_system()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
