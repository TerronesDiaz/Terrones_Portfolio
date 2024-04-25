/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	darkMode: 'media', 
	theme: {
	  extend: {
		colors: {
		  transparentGray: 'rgba(0, 0, 0, 0.6)',
		  transparentWhite: 'rgba(255, 255, 255, 0.8)',
		  transparentBlack: 'rgba(0, 0, 0, 0.6)', 
		},
	  },
	},
	plugins: [],
  }
  