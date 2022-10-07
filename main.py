def encode(message):
    encoded_msg = ""
    i = 0
    while i <= len(message) - 1:
        count = 1
        char = message[i]
        j = i
        while j < len(message) - 1:
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_msg = encoded_msg + str(count) + char
        i = j + 1
    return encoded_msg


encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
