import argparse
import os
import pathlib
import subprocess

def make_day(dayname, challenge_name = None, challenge_number = None):
    cannonical_path = pathlib.Path(dayname)
    if not os.path.isdir(cannonical_path):
        os.mkdir(cannonical_path)


    with open(cannonical_path / 'main.py', 'w', encoding='utf-8') as f:
        f.write(f"""from pyscript import display
from utils import get_input

def main_{dayname}(*args):
    data = get_input("{dayname}")

    result = None
    display(result, target="{dayname}-output")
""")

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
    
    data[1] = f"""{{{{< adv2023 title="Day {challenge_number if challenge_number else "X"}: {challenge_name if challenge_name else 'CHALLENGE NAME'}" id="{dayname}" file="{dayname}/main.py">}}}}
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