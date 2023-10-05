def caesar(offset, input_str):
    result = ""
    for char in input_str:
        if char == ' ':
            result += ' '
        else:
            shifted_char_code = ord(char) + (offset % 26)  # Gunakan modulo 26 untuk memastikan pergeseran tidak melebihi 26 karakter
            if char.islower():
                if shifted_char_code > ord('z'):
                    shifted_char_code -= 26  # Kembali ke awal alfabet jika melebihi 'z'
                result += chr(shifted_char_code)
            else:
                result += char  # Abaikan karakter selain huruf kecil
    return result

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl