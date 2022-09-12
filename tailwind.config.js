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
        '76': '19rem',
      },
      maxHeight: {
        '124': '31rem',
      },
      backgroundColor: {
        'pygray': '#2C2E34',
      }
    }
  },
  variants: {
    margin: ['first', 'responsive'],
    borderRadius: ['responsive', 'hover', 'focus'],
    transform: ['responsive', 'hover', 'focus'],
    extend: {
      backgroundColor: ['odd', 'even'],
      fontWeight: ['responsive', 'hover'],
      scale: ['responsive', 'hover', 'focus'],
      borderWidth: ['responsive', 'hover'],
      borderColor: ['responsive', 'hover']
    },
  },
  plugins: [],
}
