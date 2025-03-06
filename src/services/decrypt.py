def decrypt(text, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  keyword = []

  for letter in text:
    if letter in alphabet:
      new_index = (alphabet.index(letter) - key) % 26
      keyword.append(alphabet[new_index])
    else:
      keyword.append(letter)

  return "".join(keyword)
      