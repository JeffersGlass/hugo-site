This all brings me back to [Issue #519 - Add Loading of Structured Packages to Py-Config](https://github.com/pyscript/pyscript/issues/519), where the idea of loading things in a deliberate way was first discussed, and which eventually lead to `[[fetch]]` as we know it. Gosh we were all so young back then! It's worth re-reading that thread, a lot of ideas floated here are explored there with good commentary. Not that we have to agree with our past selves.

If having a real-life example is helpful, here is the py-config from the [WASM Wabbit](https://jeff.glass/post/whats-new-pyscript-2023-03-1/#pyxel), the Pyxel-in-PyScript game I built in the Spring:

```toml
<py-config>
    packages = ['pyxel']

    [[fetch]]
    from = 'https://dev.jeff.glass/wasm-wabbit-game/src'
    files = ['animated.py', 'collision.py', 'frame.py', 'images.pyxres', 'level.py', 'main.py', 'protocols.py', 'sounds.pyxres', 'wabbit-wesources.pyxres', 'wabbit.py', 'objects/coin.py']
    

    [[fetch]]
    from = 'https://dev.jeff.glass/wasm-wabbit-game/src/levels'
    files = ['level_1.pyxres', 'level_2.pyxres', 'level_3.pyxres']
    to_folder = 'levels'
</py-config>
```

It's pulling some objects out of the `/src` path and sticking them in root (plus sticking `coin.py` in the `/objects` path), and sticking some levels out of the `/levels` path and sticking them in the levels folder.

Re-written with just a 1-to-1 mappiing, this would become:
```toml
<py-config>
packages = ['pyxel']

[[fetch]]
[files]
    "https://dev.jeff.glass/wasm-wabbit-game/src/animated.py" = "animated.py" 
    "https://dev.jeff.glass/wasm-wabbit-game/src/collision.py" = "collision.py" 
    "https://dev.jeff.glass/wasm-wabbit-game/src/frame.py" = "frame.py" 
    "https://dev.jeff.glass/wasm-wabbit-game/src/images.pyres" = "images.pyres" 
    "https://dev.jeff.glass/wasm-wabbit-game/src/level.py" = "level.py" 
    "https://dev.jeff.glass/wasm-wabbit-game/src/main.py" = "main.py" 
    "https://dev.jeff.glass/wasm-wabbit-game/src/protocols.py" = "protocols.py"
    "https://dev.jeff.glass/wasm-wabbit-game/src/sounds.pyxres" = "sounds.pyxres"
    "https://dev.jeff.glass/wasm-wabbit-game/src/wabbit-wesources" = "wabbit-wesources.pyxres" 
    "https://dev.jeff.glass/wasm-wabbit-game/src/wabbit.py" = "wabbit.py"
    "https://dev.jeff.glass/wasm-wabbit-game/src/objects/coin.py" = "objects/coin.py"
    "https://dev.jeff.glass/wasm-wabbit-game/src/levels/level_1.pyxres" = "levels/level_1.pyxres"
    "https://dev.jeff.glass/wasm-wabbit-game/src/levels/level_2.pyxres" = "levels/level_2.pyxres"
    "https://dev.jeff.glass/wasm-wabbit-game/src/levels/level_3.pyxres" = "levels/level_3.pyxres"
<py-config>
```

It is wholey unambigous what this does... but the amout of copy-paste makes it easy to see how errors can be introduced when addition additional files. It's also hard to see at a glance what files come from which source URLs and reason about what might be missing.

I have a suggestion to make, but I'll actually put it in a separate comment to keep it apart from this example.