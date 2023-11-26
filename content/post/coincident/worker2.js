import coincident from 'https://unpkg.com/coincident/window';
const {proxy, window} = coincident(self);

function calc_pi_gl_series(digits){
    let value = 1
    let i = 1
    let term = 0;

    do {
        term = ((-1) ** i)/(2*i + 1) // 1 - 1/3 + 1/5 - 1/7 + ...
        value += term
        i += 1
    } while (Math.abs(4 * term) > (1/10**digits))
    return value * 4
}

function do_calculation(){
    const result = calc_pi_gl_series(5); // hardcoded number of digits for now
    console.log(result)
}

const btn = window.document.getElementById("btn-calc2")
btn.addEventListener("click", do_calculation)