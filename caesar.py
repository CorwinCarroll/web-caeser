def morethan(n):
	alphadic_lower = list("abcdefghijklmnopqrstuvwxyz")
	if n > 25:
		n = n % len(alphadic_lower)
		return n
	else:
		return n

def alphabet_position(letter):
	combo_d = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	return combo_d.get(letter)

def rotate_character(l, rotation):
	alphadic_lower = list("abcdefghijklmnopqrstuvwxyz")
	alphadic_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	rotation = morethan(rotation)
	if l in alphadic_lower:
		rotated_lower = []
		rotated_lower = alphadic_lower
		char = rotated_lower.index(l)
		rotated_lower = rotated_lower[rotation:] + rotated_lower[:rotation]
		return rotated_lower[char]
	elif l in alphadic_upper:
		rotated_upper = []
		rotated_upper = alphadic_upper
		char = rotated_upper.index(l)
		rotated_upper = rotated_upper[rotation:] + rotated_upper[:rotation]
		return rotated_upper[char]
	else:
		return l

def encrypt(text, rot):
	encrypting = []
	for l in text:
		encrypting.append(rotate_character(l, rot))
	encrypted = ''.join(encrypting)
	return encrypted