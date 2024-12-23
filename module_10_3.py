import threading
import random
import time


class Bank(threading.Thread):
    def __init__(self, balance) :
        threading.Thread.__init__(self)
        self.balance = balance
        self.lock = threading.Lock()


    def deposit(self):
        transactions = 100
        for transaction in range(transactions):
            random_number = random.randint(50, 500)
            self.balance += random_number
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {random_number}. Баланс: {self.balance}")
            time.sleep(0.001)


    def take(self) :
        transactions = 100
        for transaction in range(transactions) :
            random_number = random.randint(50, 500)
            print(f"Запрос на {random_number}")
            if random_number <= self.balance :
                self.balance -= random_number
                print(f"Снятие: {random_number}. Баланс: {self.balance}")
            else :
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank(120)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
