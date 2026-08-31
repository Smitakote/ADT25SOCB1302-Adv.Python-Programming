# Dynamic Report Generator

def format_report(func):
    def wrapper(self, *args):
        print("\n------------------------------")
        print(self.title)
        print("------------------------------")
        func(self, *args)
        print("------------------------------")
    return wrapper


class Report:

    def __init__(self, title, data):
        self.title = title
        self.data = data

    # Magic method
    def __str__(self):
        return "Report Name: " + self.title

    # Class method
    @classmethod
    def create_report(cls, title, data):
        return cls(title, data)

    # Decorator
    @format_report
    def generate_report(self, style="normal"):

        if style == "normal":
            for key, value in self.data.items():
                print(key, ":", value)

        elif style == "upper":
            for key, value in self.data.items():
                print(key.upper(), ":", str(value).upper())

        elif style == "simple":
            for key, value in self.data.items():
                print(key, "=", value)

        else:
            print("Invalid format!")


def main():

    data = {
        "Name": "Anjali",
        "Branch": "CSE",
        "Marks": 85,
        "Grade": "A"
    }

    report = Report.create_report("Student Report", data)

    print(report)

    while True:

        print("\n1. Normal Format")
        print("2. Uppercase Format")
        print("3. Simple Format")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            report.generate_report("normal")

        elif choice == "2":
            report.generate_report("upper")

        elif choice == "3":
            report.generate_report("simple")

        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()