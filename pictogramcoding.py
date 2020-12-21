def rle_algorithm(string_code):
    rle_string = ''
    count = 1
    for i in range(1, len(string_code)):
        if i <= len(string_code):
            if string_code[i - 1] == string_code[i]:
                count += 1
            else:
                rle_string += str(count)
                count = 1
    rle_string += str(count)
    return rle_string


def line_by_line(code):
    return ''.join([''.join(map(str, row)) for row in code])


def line_by_line_reversed(code):
    sequence = [code[i] if i % 2 == 0 else list(reversed(code[i])) for i in range(len(code))]
    return ''.join([''.join(map(str, row)) for row in sequence])


def by_stripes_2(code):
    sequence = []
    for i in range(0, len(code), 2):
        for j in range(len(code[i])):
            sequence.append(code[i][j])
            try:
                sequence.append(code[i + 1][j])
            except IndexError:
                pass
    return sequence


def by_stripes_4_reversed(code):
    sequence = []
    for i in range(0, len(code), 4):
        for j in range(len(code[i])):
            if j % 2 == 0:
                sequence.append(code[i][j])
                sequence.append(code[i + 1][j])
                sequence.append(code[i + 2][j])
                sequence.append(code[i + 3][j])
            else:
                sequence.append(code[i + 3][j])
                sequence.append(code[i + 2][j])
                sequence.append(code[i + 1][j])
                sequence.append(code[i][j])
    return sequence


def get_picture_code(picture=None):
    if picture is None:
        return [list(map(lambda el: 1 if el == '*' else 0, input()))
                for _ in range(int(input('Число строк в изображении: ')))]
    else:
        return [list(map(lambda el: 1 if el == '*' else 0, row)) for row in picture.split('\n')]


def main():
    picture = ' **  ** \n' \
              ' *** ** \n' \
              ' ** *** \n' \
              ' *** ** \n' \
              ' ** *** \n' \
              ' *** ** \n' \
              ' ** *** \n' \
              ' *** ** \n'
    print(f"line by line:\n{rle_algorithm(line_by_line(get_picture_code(picture)))}")
    print(f"line by line with reverse:\n{rle_algorithm(line_by_line_reversed(get_picture_code(picture)))}")
    print(f"by stripes-2:\n{rle_algorithm(by_stripes_2(get_picture_code(picture)))}")
    print(f"by stripes-4 with reverse:\n{rle_algorithm(by_stripes_4_reversed(get_picture_code(picture)))}")


if __name__ == "__main__":
    main()
