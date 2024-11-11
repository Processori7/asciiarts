import sys
from itertools import islice
from PIL import Image
from tkinter import filedialog


# Функция для преобразования изображения в ASCII
def image_to_ascii(image_path, width):
	try:
		# Открываем изображение
		img = Image.open(image_path)

		# Изменяем размер изображения
		aspect_ratio = img.height / img.width
		new_height = int(aspect_ratio * width * 0.55)  # 0.55 для учета соотношения сторон символов
		img = img.resize((width, new_height))

		# Преобразуем изображение в градации серого
		img = img.convert("L")

		# Определяем символы ASCII
		ascii_chars = "@%#*+=-:. "
		pixels = img.getdata()

		# Преобразуем пиксели в символы
		ascii_str = ''.join(ascii_chars[pixel * (len(ascii_chars) - 1) // 255] for pixel in pixels)

		# Разбиваем строку на строки для вывода
		img_width = img.width
		ascii_str_len = len(ascii_str)
		ascii_img = "\n".join(ascii_str[i:i + img_width] for i in range(0, ascii_str_len, img_width))

		return ascii_img
	except Exception as e:
		print(e+"\n")
		main()


def load_alphabet(filename):
	try:
		alphabet = []
		with open(filename) as f:
			while True:
				ascii_char = list(islice(f, 8))  # 8 - высота символа
				if ascii_char:
					alphabet.append(ascii_char)
				else:
					break
		return alphabet
	except Exception as e:
		print(e+"\n")

def get_char_index(char):
	try:
		ORDER_OFFSET = 1072  # Смещение для кириллицы
		if char =="ё":
			index = ord(char) -1 - ORDER_OFFSET
		else:
			index = ord(char) - ORDER_OFFSET
		return index
	except Exception as e:
		print(e+"\n")
		main()

def write_text(alphabet):
	try:
		inpt = input("Введите текст:").lower()

		for phrase in inpt.split(' '):
			for counter in range(8):  # Высота символа
				for char in phrase:
					index = get_char_index(char)
					if 0 <= index < len(alphabet):  # Проверка на допустимый индекс
						print(f"{alphabet[index][counter][:-1]:<8}", end=' ')  # 8 - ширина
					else:
						print(" " * 8, end=' ')  # Пустое место для недопустимого символа
				print()
			print()
	except Exception as e:
		print(e+"\n")
		main()

def main():
	try:
		alphabet = load_alphabet('alphabet.txt')
		while True:
			ans = input("Выберите действие:\n1-Ввести текст\n2-Картинка в ASCII >>>")
			if ans.isdigit():
				ans = int(ans)
				if ans == 1:
					write_text(alphabet)
				elif ans == 2:
					image_path = filedialog.askopenfilename()  # Укажите путь к вашему изображению
					width =input("Укажите ширину:")
					if width.isdigit():
						width = int(width)
					else:
						width = 100
					ascii_art = image_to_ascii(image_path, width)
					print(ascii_art)
				else:
					print("Ошибка! Введите 1 или 2.")
			else:
				print("Ошибка! Введите число!")
	except Exception as e:
		print(e+"\n")
		main()

if __name__ == "__main__":
    main()
