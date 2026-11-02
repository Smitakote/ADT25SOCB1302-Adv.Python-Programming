import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    logging.debug("Division function started")

    try:
        result = a / b
        logging.info("Division performed successfully")
        logging.debug("Result is %s", result)
        return result

    except ZeroDivisionError:
        logging.exception("Error occurred: Division by zero")
        return None

def main():
    logging.info("Program execution started")

    try:
        a = 10
        b = 2

        logging.debug("Input values: a=%s, b=%s", a, b)

        result = divide(a, b)
        print("Result:", result)

        # Exception example
        divide(10, 0)

    except Exception:
        logging.exception("Unexpected error occurred")

    finally:
        logging.info("Program execution completed")

if __name__ == "__main__":
    main()