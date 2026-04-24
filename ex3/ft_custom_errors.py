#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def garden_operations(operation_type: str) -> None:
    match operation_type:
        case "Water":
            raise WaterError("Not enough water in the tank!")
        case "Plant":
            raise PlantError("The tomato plant is wilting!")


def test_error_types() -> None:
    print("Testing PlantError...")
    try:
        garden_operations("Plant")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("")

    print("Testing WaterError...")
    try:
        garden_operations("Water")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("")

    print("Testing catching all garden errors...")
    for name in ["Plant", "Water"]:
        try:
            garden_operations(name)
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print("")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("")

    test_error_types()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
