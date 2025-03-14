from js import Chart, document, Object
from pyodide.ffi import to_js
import asyncio

def j(obj):
    return to_js(obj, dict_converter=Object.fromEntries)

def viz_day1_1():
    asyncio.ensure_future(viz_day1_1_coro())

async def viz_day1_1_coro():
    if ctx:= document.getElementById("day1_1-viz-canvas") is None:
        ctx = document.createElement("canvas")
        ctx.id = "day1_1-viz-canvas"
        parent = document.getElementById("day1_1-viz")
        parent.appendChild(ctx)
        parent.style.width="48rem"
        parent.style.height="24rem"
        parent.style.position = 'relative'

    elf_packs = (get_input('day1_1').split('\n\n'))
    elf_calories = [sum(int(line) for line in pack.split('\n')) for pack in elf_packs]
    most = max(elf_calories)
    most_index = elf_calories.index(most)

    display(f"{max(elf_calories)= }",
         target="day1_1-output",
         append=False)

    my_chart = Chart.new(ctx, j({
        "type": "bar",
        "data": j({
            "labels": [f"Elf {i}" for i in range(len(elf_packs))],
            "datasets": [j({
                "label": "data",
                "data": elf_calories,
                "stack": 1,
                "backgroundColor": ['rgba(75,192,192,0.4)' if cal != most else 'red' for cal in elf_calories ] 
            })]
        }),
        "options": j({
            "animation": False,
            "responsive": True, 
            "plugins": j({
                "legend": j({
                    "display": False
                }),
            }),
            "scales": j({
                "x": j({
                    "stacked": True
                }),
                "y": j({
                    "beginAtZero": True
                })
            })
        })
    }))