def main_day1_2():
    elf_packs = (get_input('day1_2').split('\n\n'))
    elf_calories = sorted(sum(int(line) for line in pack.split('\n')) for pack in elf_packs)
    display(f"{sum(elf_calories[-3:])= }",
         target="day1_2-output",
         append=False)