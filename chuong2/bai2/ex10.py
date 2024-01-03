import json
import datetime
transactions = []

while True:
    transaction = {}
    transaction['type'] = input("Loại giao dịch (tiền/vàng): ")
    transaction['amount'] = float(input("Số tiền/vàng: "))
    transactions.append(transaction)
    continue_transaction = input("Tiếp tục giao dịch? (y/n): ").strip().lower()
    if continue_transaction != 'y':
        break
save_to_file = input("Lưu giao dịch vào tập tin JSON? (1: Có, 0: Không): ").strip()
if save_to_file == '1':
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"{current_time}.json"
    with open(filename, 'w') as json_file:
        json.dump(transactions, json_file, indent=4)
    print(f'Giao dịch đã được lưu vào tệp {filename}')
else:
    print('Không lưu giao dịch vào tệp JSON.')
