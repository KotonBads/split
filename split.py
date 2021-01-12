class split:
    def __init__(self, text, pos, flag = 0):
        text_len = len(text)
        remove = text_len - pos
        if flag == 0:
            text = text[:-remove]
            print(text)
        elif flag == 1:
            if text_len == pos:
                print('YOU\'RE REMOVING THE WHOLE WORD 😠')
            else:
                text = text[:-remove]
                print(text)