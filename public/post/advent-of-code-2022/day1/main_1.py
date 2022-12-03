def main_day1_1():
    elf_packs = (get_input('day1_1').split('\n\n'))
    elf_calories = (sum(int(line) for line in pack.split('\n')) for pack in elf_packs)
    display(f"{max(elf_calories)= }",
         target="day1_1-output",
         append=False)