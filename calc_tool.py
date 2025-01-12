def calculator():
    print("calc tool")
    print("1: plus")
    print("2: minus")
    print("3: multiply")
    print("4: divide")
    print("5: べき乗")

    choice = input("Enter 1-4:")

    if choice in ['1','2','3','4','5']:
        num1 = float(input("1つ目の数値を入力:"))
        num2 = float(input("2つ目の数値を入力:"))

        if choice == '1':
            print(f"結果: {num1 + num2}")
        elif choice == '2':
            print(f"結果: {num1 - num2}")
        elif choice == '3':
            print(f"結果: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"結果: {num1 / num2}")
            else:
                print("エラー: 0で割ることはできません")
        elif choice == '5':
            print(f"結果: {num1 ** num2}")
    else:
        print("無効な選択です。")

if __name__ == '__main__':
    calculator()
