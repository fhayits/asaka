import sys


def main():
    if len(sys.argv) < 2:
        print("Foydalanish: asaka-cli <ismingiz>")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Salom, {name}! Asaka dasturiga xush kelibsiz.")


if __name__ == "__main__":
    main()
