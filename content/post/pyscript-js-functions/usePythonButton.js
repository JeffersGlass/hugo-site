    document.getElementById("use-python-objects").addEventListener("click", () => {
        console.log("Displaying contents of Python list 'names', calling Python function 'multiplier'")
        el = document.getElementById("output")
        el.innerHTML = '' //Clear contents of output
        for (const name of names_js){
            el.innerHTML += "Name: " + name + "<br\>";
        };
        number = Math.floor(Math.random() * 10) + 1 //random between 1 and 10
        el.innerHTML += number + " times two is " + multiplier_js(number) + "<br\>";
    });