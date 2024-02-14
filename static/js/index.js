const $slideNumButton = document.querySelector('.number-slide')
const $settingsButton = document.querySelector('.settings')

// OPÇÕES
const options = {
	vibrate: !(localStorage.getItem('slide.options.vibrate') === 'false'),
	dblClick: localStorage.getItem('slide.options.dblClick') === 'true'
}

// ENVIA O COMANDO PARA O BACK-END
function sendCommand(command) {
	if (options.vibrate) navigator.vibrate(150)
	fetch(`/control/${command}`).then((r) => {
		if (r.status !== 204) throw new Error(r)
	}).catch((err) => {
		if (options.vibrate) navigator.vibrate([200, 100, 200])
	})
}

// FUNÇÃO DOS BOTÕES
document.querySelectorAll('[data-command]').forEach((el) => {
	// Ação do botão
	el.addEventListener(options.dblClick ? 'dblclick' : 'click', function (e) {
		e.preventDefault()
		sendCommand(this.dataset.command)
	})
})

// BOTÃO PULAR PARA SLIDE
$slideNumButton.addEventListener(options.dblClick ? 'dblclick' : 'click', (e) => {
	e.preventDefault()
	Swal.fire({
		title: 'Pular para slide',
		input: 'number',
		inputAttributes: {
			min: '1',
			step: '1',
			placeholder: 'Nº do slide'
		},
		showCancelButton: true,
		confirmButtonText: 'Ir',
		cancelButtonText: 'Cancelar'
	}).then((result) => {
		if (!result.value) return
		if (!isNaN(result.value) && parseInt(result.value) > 0) {
			sendCommand(`goto/${result.value}`)
		}
	})
})

// BOTÃO CONFIGURAÇÕES
$settingsButton.addEventListener(options.dblClick ? 'dblclick' : 'click', (e) => {
	e.preventDefault()
	Swal.fire({
		title: 'Configurações',
		showCancelButton: true,
		confirmButtonText: 'Salvar',
		cancelButtonText: 'Cancelar',
		html: `
			<div class="settings-popup">
				<label>
					<input type="checkbox" id="vibrate" ${options.vibrate ? 'checked' : ''}>
					<span>Vibração</span>
				</label>
				<label>
					<input type="checkbox" id="dblClick" ${options.dblClick ? 'checked' : ''}>
					<span>Duplo clique para acionar</span>
				</label>
			</div>`,
		preConfirm: () => {
			return {
				vibrate: document.getElementById('vibrate').checked,
				dblClick: document.getElementById('dblClick').checked
			}
		}
	}).then((result) => {
		if (!result.value) return
		localStorage.setItem('slide.options.vibrate', result.value.vibrate)
		localStorage.setItem('slide.options.dblClick', result.value.dblClick)
		location.reload()
	})
})
