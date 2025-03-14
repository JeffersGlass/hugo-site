import argparse
import os
import pathlib
import subprocess

def start_py_file(f, dayname, part):
        f.write(f"""try:
    from pyscript import document
    from utils import get_input
except ImportError:
    def get_input(*args):
        with open("input_test.txt") as f:
            return f.read()
        
    def display(*args, **kwargs):
        if 'target' in kwargs:
            kwargs.pop('target')
        print(*args, **kwargs)
                
import sys

def main_{dayname}_{part}(*args):
    data = get_input("{dayname}_{part}")

    result = None
    display(result, target="{dayname}_{part}-output")

if not 'js' in sys.modules:
    main_{dayname}_{part}()
""")

def make_day(dayname, challenge_name = None, challenge_number = None):
    cannonical_path = pathlib.Path(dayname)
    if not os.path.isdir(cannonical_path):
        os.mkdir(cannonical_path)


    for part in ('1', '2'):
        with open(cannonical_path / f'main_{part}.py', 'w', encoding='utf-8') as f:
             start_py_file(f, dayname, part)

    for file_name in ('input.txt', 'input_test.txt'):
         with open(cannonical_path / file_name, 'w') as f:
              pass


    # Install virtual env
    prev_dir = os.getcwd()
    os.chdir(cannonical_path)
    subprocess.run(["pipenv", "install", "--python", "3.12"])
    os.chdir(prev_dir)

    DEMARKER = "<!--NEW_DAYS_ABOVE_THIS_LINE-->"

    #Add day to index.html
    with open("index.html", "r") as f:
        data = f.read().split(DEMARKER)
        assert len(data) == 2
    
    data[1] = f"""{{{{< adv2023 title="Day {challenge_number if challenge_number else "X"} (Part 1): {challenge_name if challenge_name else 'CHALLENGE NAME'}" id="{dayname}_1" file="{dayname}/main_1.py">}}}}
<p class="post-p">DESCRIPTION</p>
{{{{< /adv2023 >}}}}

{{{{< adv2023 title="Day {challenge_number if challenge_number else "X"} (Part 2): {challenge_name if challenge_name else 'CHALLENGE NAME'}" id="{dayname}_2" file="{dayname}/main_2.py">}}}}
<p class="post-p">DESCRIPTION</p>
{{{{< /adv2023 >}}}}\n\n""" + DEMARKER + data[1]
    
    with open("index.html", "w") as f:
        f.write(''.join(data))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = 'Make a Day'
    )

    parser.add_argument('dayname')
    parser.add_argument('--name', '--challenge-name')
    parser.add_argument('--number')

    args = parser.parse_args()
    make_day(args.dayname, args.name, args.number)