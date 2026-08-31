from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print("Payment of Rs.", amount, "made using Credit Card.")


class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print("Payment of Rs.", amount, "made using Debit Card.")


class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print("Payment of Rs.", amount, "made using UPI.")


class PaymentProcessor:

    def __init__(self):
        self.strategy = None

    def set_payment_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):

        if self.strategy is None:
            print("Please select a payment method first.")
        else:
            self.strategy.pay(amount)


def main():

    processor = PaymentProcessor()

    while True:

        print("\n1. Credit Card")
        print("2. Debit Card")
        print("3. UPI")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            processor.set_payment_strategy(CreditCardPayment())

        elif choice == "2":
            processor.set_payment_strategy(DebitCardPayment())

        elif choice == "3":
            processor.set_payment_strategy(UpiPayment())

        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid choice")
            continue

        amount = float(input("Enter amount: "))
        processor.process_payment(amount)


if __name__ == "__main__":
    main()