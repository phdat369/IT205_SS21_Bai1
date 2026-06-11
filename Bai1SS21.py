import logging
logging.basicConfig(
    filename="abc.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
current_balance = 0
def recharge_money():
    global current_balance
    while True:
        try:
            loaded = int(input("Nhập tiền cần nạp: "))
            if loaded <= 0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(f"Attempted to process {loaded} VND")
                continue
        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error("Invalid numeric input for deposit.")
        else:
            break
    print(f"Nạp tiền thành công: +{loaded:,} VND")
    current_balance += loaded
    print(f"Số dư hiện tại: {current_balance:,} VND")
    logging.info(f"Deposit successful: +{loaded} VND. Current Balance: {current_balance}")
def transfer_money():
    global current_balance
    phone_number = input("Nhập số điện thoại(định dạng 10 số): ").strip()
    while not phone_number.startswith("0") or not phone_number.isdigit() or len(phone_number) != 10:
        print("Số điện thoại không hợp lệ")
        phone_number = input("Nhập số điện thoại người nhận(định dạng 10 số): ").strip()
    while True:
        try:
            loaded = int(input("Nhập tiền cần chuyển: "))
            if loaded <= 0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(f"Attempted to process {loaded} VND")
                continue
            if loaded > current_balance:
                print("Giao dịch thất bại: Số dư của bạn không đủ.")
                print(f"Số dư hiện tại: {current_balance:,} VND")
                logging.error(f"InsufficientBalanceError: Attempted to transfer {loaded} VND with balance {current_balance} VND.")
                continue
        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error("Invalid numeric input for deposit.")
        else:
            break
    if loaded >= 5000000:
        current_balance -= loaded
        print(f"Số tiền đã chuyển: {loaded:,} VND")
        print(f"Số dư còn lại: {current_balance:,} VND")
        logging.warning(f"High value transaction detected: {loaded} VND to {phone_number}")
        logging.info(f"Transfer successful: -{loaded} VND to {phone_number}. Current Balance: {current_balance}")
    else:
        current_balance -= loaded
        print(f"Số tiền đã chuyển: {loaded:,} VND")
        print(f"Số dư còn lại: {current_balance:,} VND")
        logging.info(f"Transfer successful: -{loaded} VND to {phone_number}. Current Balance: {current_balance}")
def display_balance():
    print("--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {current_balance:,} VND")
    logging.info(f"2026-06-04 10:25:00,123 - INFO - Balance checked. Current Balance: {current_balance}")
def display_log():
    with open("abc.txt") as log:
        content = log.read()
        if not content:
            print("Không có lịch sử")
        else:
            print("--- Lịch sử log gần nhất---")
            print(content)
def main():
    while True:
        choose = input("""========== VÍ MOMO GIẢ LẬP ==========
1. Nạp tiền vào ví
2. Chuyển tiền
3. Xem lịch sử hệ thống
4. Xem số dư tài khoản
5. Thoát chương trình 
===============================================
Chọn chức năng (1-5): """)
        if choose == "1":
            recharge_money()
            print()
        elif choose == "2":
            transfer_money()
            print()
        elif choose == "3":
            display_log()
            print()
        elif choose == "4":
            display_balance()
            print()
        elif choose == "5":
            print("Chương trình kết thúc")
            break
        else:
            print("Lựa chọn không hợp lệ")
main()
    