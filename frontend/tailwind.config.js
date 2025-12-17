/** @type {import('tailwindcss').Config} */
export default {
    // This array tells Tailwind exactly where to look for classes
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}", 
      "./src/*.{js,ts,jsx,tsx}"
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  }