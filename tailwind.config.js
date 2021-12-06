module.exports = {
  purge: {
    content: ["./layouts/index.html","./layouts/**/*.html", "./content/**/*.md", "./content/**/*.html"],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      width: {
        '20-1': '19%',
        '25-1': '24%',
        '98': '24.5rem',
        '128': '32rem',
        '130': '32.5rem'
      },
      height: {
        '124': '31rem',
      }
    },
  },
  variants: {
    margin: ['first'],
    borderRadius: ['responsive', 'hover', 'focus'],
    scale: ['responsive', 'hover', 'focus'],
    transform: ['responsive', 'hover', 'focus'],
    extend: {
      backgroundColor: ['odd', 'even'],
    },
  },
  plugins: [],
}
