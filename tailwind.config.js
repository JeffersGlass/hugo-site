module.exports = {
  purge: {
    content: ["./layouts/index.html","./layouts/**/*.html", "./content/**/*.md", "./content/**/*.html"],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      width: {
        '20-1': '19%',
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
