#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            42 / 0
        case 2:
            open("/non/existent/file")
        case 3:
            "abc" + 42


def test_error_types() -> None:
    for i in [0, 1, 2, 3, 4]:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError,
        ) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        else:
            print("Operation completed successfully")


def main() -> None:
    print("=== Garden Error Types Demo ===")

    test_error_types()
    print("")

    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
