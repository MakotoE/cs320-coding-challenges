def is_reverse(a: str, b: str) -> bool:
	if len(a) == 0 or len(b) == 0:
		return len(a) == len(b)
	if a[0].lower() != b[-1].lower():
		return False
	return is_reverse(a[1:], b[:-1])


if __name__ == '__main__':
	print(is_reverse("CS320", "023sC"))
	print(is_reverse("Madam", "MaDAm"))
	print(is_reverse("Q", "Q"))
	print(is_reverse("", ""))
	print(is_reverse("e via n", "N aIv E"))
	print(is_reverse("Go! Go", "OG !OG"))
	print(is_reverse("Obama", "McCain"))
	print(is_reverse("banana", "nanaba"))
	print(is_reverse("hello!!", "olleh"))
	print(is_reverse("", "x"))
	print(is_reverse("madam I", "i m adam"))
	print(is_reverse("ok", "oko"))
