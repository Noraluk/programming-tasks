cha_input = input()

line1 = '.'+''.join('.*..' if x %
                    3 == 2 else '.#..' for x in range(len(cha_input)))
line2 = '.'+''.join('*.*.' if x %
                    3 == 2 else '#.#.' for x in range(len(cha_input)))
line3 = '#'+''.join(f'.{cha_input[x]}.*' if x % 3 !=
                    0 else f'.{cha_input[x]}.#' for x in range(len(cha_input)))

if len(cha_input) % 3 == 2:
    line3 = line3[:-1] + '#'

print('\n'.join([line1, line2, line3, line2, line1]))
