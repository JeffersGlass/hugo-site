
import coincident from 'https://unpkg.com/coincident/window';

console.log("Worker runnning")

const {proxy, window, isWindowProxy} = coincident(self);
const {document} = window;

function calc_pi_gl_series(digits, output_el){
    let value = 1
    let i = 1
    let term = 0;
    let highest_digit = 1

    do {
        term = ((-1) ** i)/(2*i + 1) // 1 - 1/3 + 1/5 - 1/7 + 1/9 ...
        value += term
        i += 1
        if (Math.abs(4 * term) < (1/10**highest_digit)){
            // Our error is now small enough that we can be confident in a new digit being correct
            output_el.innerText = Math.trunc((value * 4 * 10**(highest_digit-1)), highest_digit)/10**(highest_digit-1)
            highest_digit += 1
        }
    } while (Math.abs(4 * term) > (1/10**digits))
    return Math.trunc((value * 4 * 10**(digits-1)), digits)/10**(digits-1)
}

function do_calculation(){
    //Handle display changes
    document.getElementById("ellipsis").innerText = "..."
    const btn = document.getElementById("btn-calc")
    btn.setAttribute("disabled", "")
    btn.innerText = "Calculating..."

    const digits = document.getElementById("inp-digits").value
    const output_el = document.getElementById("output")
    calc_pi_gl_series(digits, output_el)

    document.getElementById("ellipsis").innerText = ""
    btn.removeAttribute("disabled")
    btn.innerText = "Calculate"
    proxy.completionAlert()
}

const btn = document.getElementById("btn-calc")
btn.addEventListener("click", do_calculation)


//proxy.greetings();

/*const output = document.getElementById("output")
output.innerText = "GOTCHA"

const arr = window.Array(1, 2, 3);
const obj = arr[Symbol.iterator]();
console.assert(
  typeof obj.next === 'function' && (
    typeof obj[Symbol.iterator] === 'function' ||
    typeof obj[Symbol.asyncIterator] !== 'function'
));

console.assert(document.body === document.body);
console.assert(typeof document.body === 'object');
console.assert(typeof document.addEventListener === 'function');

document.body.addEventListener('click', event => {
  console.log(event.type);
});

console.log(document.body.querySelectorAll('*')[0].tagName);

// to log window objects in the window/main thread
window.console.log(document.body);

document.body.appendChild(document.createElement('div')).textContent = '🥳';

const remote = new window.Object;

console.assert(isWindowProxy(remote));

console.log(JSON.stringify(
  window.Object.getOwnPropertyDescriptor(window.Int32Array, 'BYTES_PER_ELEMENT')
));

let test = 0;
Object.defineProperty(remote, 'test', {
  configurable: true,
  get: () => test++,
});

Promise.all([
  remote.test,
  remote.test,
  remote.test
]).then(results => {
  console.log(results);
  console.log(test);
});

console.assert(delete remote.key);
console.assert(Reflect.setPrototypeOf(remote, window.Array.prototype));
console.assert(window.Reflect.preventExtensions(remote));
console.log(Reflect.ownKeys(window.Promise));
console.assert(new window.Object(123) instanceof window.Number);
console.log(window.Math.max.apply(window.Math, [1, 2]));
console.log(window.Math.max.call(window.Math, 1, 2));
console.assert(window.navigator instanceof window.Object);
console.log(window.parseInt('01', 10), parseInt('01', 10));
console.log(window.navigator.userAgent);
console.assert(Object.isExtensible(window.navigator));
console.log(window.location.href);
console.assert('length' in window.localStorage);
console.log(window.localStorage.length);
console.assert(window.Symbol.iterator === Symbol.iterator);
window.document.title = 'coincident window';
console.log(window.document.title);
new window.Promise($ => $('Promise: OK')).then(console.log).then(() => {
  console.log('Answer:', window.prompt('Have you seen the console?'));
});
*/