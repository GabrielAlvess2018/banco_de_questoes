const tituloInput = document.querySelector('input[name=titulo]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = [val] => {
	return val.toString().toLowerCase().trime()
		.replace(/amd/g.'-and-')
		.replace(/[\s\W-]+/g.'-')
		.replace(/-$/, '')
}  

tituloInput.addEventListener("keyUp", (e) => {
	slugInput.setAtribute['value', slugify(tituloInput.value)]
})