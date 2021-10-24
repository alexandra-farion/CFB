# -*- coding: utf-8 -*-

# номер, имя имя, масса, группа, главная / побочка, период

x = [26, 'Железо', 'Ferrum', 56, 8, 'b', 4, False, False]
rule_e = [2, 8, 18, 32]
rule_orbitals = ['S', 'p', 'd', 'f']


def orbitals(n_e, level):
    formula = ''
    level = str(level)

    count = 0
    for i in range(4):
        formula += level + rule_orbitals[i] + ' '
        n_e -= 2 + count
        if n_e <= 0:
            break
        count += 4

    return formula


def is_actin_lantin(parameters):
    return parameters[-1] or parameters[-2]


def print_atom(level, number_e=None):
    print("Уровень:", level, "\n", "Электронов:", number_e, "\n", "Формула уровня:",
          orbitals(number_e, level), "\n")


def calculate_atom(parameters):
    number_e = parameters[0]
    number_levels = parameters[6] - 2

    if not is_actin_lantin(parameters):
        for current_level in range(number_levels):
            e_on_cur_lvl = rule_e[current_level]
            number_e -= e_on_cur_lvl

            print_atom(current_level + 1, e_on_cur_lvl)

        e_on_last_level = parameters[4]
        if parameters[-4] == 'b':
            e_on_last_level = 2

        number_e -= e_on_last_level

        print_atom(number_levels + 1, number_e)
        print_atom(number_levels + 2, e_on_last_level)


# calculate_atom(x)
