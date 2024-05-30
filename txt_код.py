def check_neologism(word, neologisms):
    for neologism in neologisms:
        if word.lower() == neologism.strip().lower():
            return True
    return False

def main():
    file_path = "neologysm.txt"

    # Читаємо вміст файлу
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            neologisms = file.readlines()
    except FileNotFoundError:
        print(f"Не вдалося знайти файл: {file_path}")
        return

    # Користувач вводить слово для перевірки
    word = input("Введіть слово для перевірки: ").strip()

    # Перевіряємо, чи є слово неологізмом
    if check_neologism(word, neologisms):
        print("Так, це слово є неологізмом.")
    else:
        print("Ні, це слово не є неологізмом.")

if __name__ == "__main__":
    main()