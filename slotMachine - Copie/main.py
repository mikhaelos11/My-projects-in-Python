import random

MAX_LINES = 3
MAX_BET = 500
MIN_BET = 1

ROWS = 4
COLS = 4 #se pot adauga si valorile 3, 4, respectiv 5, dar rata de castig scade,
#metoda de validae a casigurilor necesita aceeasi valoare pe intreaga linie pentru a valida

symbol_count = {
    "sevens": 4,
    "watermelon": 14,
    "cherries": 14,
    "orange": 10,
    "lemon": 11,
}
symbol_values = {
    "sevens": 20,
    "watermelon": 10,
    "cherries": 5,
    "orange": 4,
    "lemon": 2,
}
class Slot:

    def __init__(self):
        pass

    def check_winnings(self, columns, lines, bet, values):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines


    def get_slot_machine_spin(self, rows, cols, symbols):
        all_symbols = []
        for symbol, symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)

        columns = []
        for _ in range(cols):
            column = []
            current_symbols = all_symbols
            for _ in range(rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)

            columns.append(column)
        return columns

    def print_slot_machine(self, columns):
         for row in range(len(columns[0])):
             for i, column in enumerate(columns):
                 if i != len(columns) - 1:
                    print(column[row], end=" | ")
                 else:
                    print(column[row], end="")

             print()


    def deposit(self):
        while True:
            amount = input("What would you like to deposit? $")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than 0. ")
            else:
                print("Please enter a number.")
        return amount

    def get_number_of_lines(self):
        while True:
            lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter a valid number of lines. ")
            else:
                print("Please enter a number.")
        return lines

    def get_bet(self):
        while True:
            amount = input("What would you like to bet on each line?")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
            else:
                print("Please enter a number.")

        return amount
    def spin(self, balance):
        lines = self.get_number_of_lines()
        while True:
            bet = self.get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You do not have enough to bet that amount, your current balance is ${balance}")
            else:
                break
        print(f"You are betting ${bet} on {lines} lines. Equal bet is equal to ${total_bet}")

        slots = self.get_slot_machine_spin(ROWS, COLS, symbol_count)
        self.print_slot_machine(slots)
        winnings, winning_lines = self.check_winnings(slots, lines, bet, symbol_values)
        print(f"You won ${winnings}.")
        print(f"You won on lines", *winning_lines)
        return winnings - total_bet

    def main(self):
        balance = self.deposit()
        while True:
            print(f"Current balance is ${balance}")
            answer  = input("Pres enter to play (q to quit).")
            if answer == "q":
                break
            balance += self.spin(balance)
        print(f"You left wwith ${balance}.")

play=Slot()
play.main()