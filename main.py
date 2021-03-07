def is_reverse(a: str, b: str) -> bool:
	if len(a) == 0 or len(b) == 0:
		return len(a) == len(b)
	if a[0].lower() != b[-1].lower():
		return False
	return is_reverse(a[1:], b[:-1])


from typing import List, Dict


def counts(numbers: List[int], find: List[int]) -> Dict[int, int]:
	count = {k: 0 for k in find}
	for n in numbers:
		if n in count:
			count[n] += 1
	return count


def switch_pairs(s: str) -> str:
	characters = list(s)
	for i in range(0, len(characters) - len(characters) % 2, 2):
		characters[i], characters[i + 1] = characters[i + 1], characters[i]
	return "".join(characters)


if __name__ == '__main__':
	assert is_reverse("CS320", "023sC") is True
	assert is_reverse("Madam", "MaDAm") is True
	assert is_reverse("Q", "Q") is True
	assert is_reverse("", "") is True
	assert is_reverse("e via n", "N aIv E") is True
	assert is_reverse("Go! Go", "OG !OG") is True
	assert is_reverse("Obama", "McCain") is False
	assert is_reverse("banana", "nanaba") is False
	assert is_reverse("hello!!", "olleh") is False
	assert is_reverse("", "x") is False
	assert is_reverse("madam I", "i m adam") is False
	assert is_reverse("ok", "oko") is False

	assert counts([], []) == {}
	assert counts([1], []) == {}
	assert counts([], [1]) == {1: 0}
	assert counts([1], [1]) == {1: 1}
	assert counts([4, -2, 3, 9, 4, 17, 5, 29, 14, 87, 4, -2, 100], [-2, 4, 29]) == {4: 3, -2: 2, 29: 1}

	assert switch_pairs("") == ""
	assert switch_pairs("a") == "a"
	assert switch_pairs("example") == "xemalpe"
	assert switch_pairs("hello there") == "ehll ohtree"
	assert switch_pairs("homework") == "ohemowkr"
	assert switch_pairs("😄😞") == "😞😄"
