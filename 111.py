# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

количество = int (input("введите количество чисел: "))
числа = input("введите числа: ").split()
числа = [int (число) for число in числа]
среднее = sum(числа)/количество
округление = round(среднее)
окр_в_меньш_сторону = int (среднее)
print (f"среднее : {среднее: 2f}")
print (f"округление : {округление}")
print (f"округление в меньшую сторону: {окр_в_меньш_сторону}")
