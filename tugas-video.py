def expenses_menu():
    expenses = []

    def add_expense():
        date = input("Tanggal (YYYY-MM-DD): ")
        category = input("Kategori: ")
        amount = float(input("Jumlah (Rp): ").replace('.', ''))
        description = input("Deskripsi: ")

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        expenses.append(expense)
        expenses.sort(key=lambda x: x['amount'])
        print("Pengeluaran berhasil ditambahkan!\n")

    def view_expenses():
        if not expenses:
            print("Belum ada pengeluaran yang tercatat.\n")
            return

        print("Pengeluaran yang tercatat:")
        print("-" * 40)
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. {expense['date']} | {expense['category']} | Rp{expense['amount']:,} | {expense['description']}")
        print("-" * 40)
        print()

    def total_expenses():
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total pengeluaran: Rp{total:,}\n")

    def binary_search_expense():
        if not expenses:
            print("Belum ada pengeluaran yang tercatat.\n")
            return

        try:
            target = float(input("Masukkan jumlah pengeluaran yang ingin dicari (Rp): ").replace('.', ''))
        except ValueError:
            print("Harap masukkan angka yang valid.\n")
            return

        low, high = 0, len(expenses) - 1
        while low <= high:
            mid = (low + high) // 2
            if expenses[mid]['amount'] == target:
                expense = expenses[mid]
                print(f"Pengeluaran ditemukan: {expense['date']} | {expense['category']} | Rp{expense['amount']:,} | {expense['description']}\n")
                return
            elif expenses[mid]['amount'] < target:
                low = mid + 1
            else:
                high = mid - 1

        print("Pengeluaran tidak ditemukan.\n")

    while True:
        print("Aplikasi Catatan Pengeluaran")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. Total Pengeluaran")
        print("4. Cari Pengeluaran (Binary Search)")
        print("5. Keluar")

        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            binary_search_expense()
        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    expenses_menu()
