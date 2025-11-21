







function initController() {

	clockWork(document.getElementById("clock"),document.getElementById("calendar"));

	const controllerState = {};
	const viewer = document.getElementById("viewer");
	const controller = document.getElementById("controller");
	const ws = new WebSocket(`ws://${location.host}/controller-ws-cast`);


	Array.prototype.forEach.call(

		controller.getElementsByClassName("controller-message"),
		div => {

			// slicing out -+ buttons from current "word"
			const word = div.innerText.slice(0,-2);
			controllerState[word] = div;

			div
				.getElementsByClassName("remove-button")[0]
				.addEventListener("click",event => forgetWord(event, word, ws));
			div
				.getElementsByClassName("accept-button")[0]
				.addEventListener("click",event => acceptWord(event, word, ws))
		}
	);


	ws.addEventListener("message",event => {

		const { view, control, released } = JSON.parse(event.data);

		if(released) {
			if(released in controllerState) {

				controller.removeChild(controllerState[released]);
				delete controllerState[released];
				return
			}	console.error(`Received ${released} which is not in controller state`)
		}

		if(typeof(view) !== "string") {

			console.error("Controller socket received invalid \"view\"");
			return
		}


		const messageBlock = document.createElement("pre");
		messageBlock.className = "viewer-message";
		messageBlock.innerText = view;

		viewer.insertBefore(messageBlock, viewer.getElementsByClassName("viewer-message")[0]);


		if(control) {
			if(Array.isArray(control) && control.every(word => typeof(word) === "string")) {

				control.forEach(word => {
					if(!(word in controllerState)) {

						const controlBlock = document.createElement("div");
						const removeButton = document.createElement("button");
						const acceptButton = document.createElement("button");

						controlBlock.className = "controller-message";
						removeButton.className = "remove-button";
						acceptButton.className = "accept-button";

						removeButton.innerText = "-";
						acceptButton.innerText = "+";

						removeButton.addEventListener("click",event => forgetWord(event, word, ws));
						acceptButton.addEventListener("click",event => acceptWord(event, word, ws));

						controlBlock.appendChild(document.createTextNode(word));
						controlBlock.appendChild(removeButton);
						controlBlock.appendChild(acceptButton);

						controller.appendChild(controlBlock);
						controllerState[word] = controlBlock
					}
				})
			}	else console.error("Controller socket received invalid \"words\"")
		}
	})
}




function initManager() {

	clockWork(document.getElementById("clock"),document.getElementById("calendar"));

	const table = document.getElementById("words-table").getElementsByTagName("tbody")[0];
	const wmap = new Map();
	const ws = new WebSocket(`ws://${location.host}/words-ws-cast`);

	Array.prototype.forEach.call(

		document.getElementsByClassName("del-button"),
		button => {

			const word = button.parentNode.cells[1].innerText;
			wmap.set(word, button.parentNode);
			button.addEventListener("click",event => {

				if(confirm(`Delete "${word}"?`)) removeWord(event, word, ws)
			})
		}
	)
	ws.addEventListener("message",event => {

		const { removed } = JSON.parse(event.data);

		if(removed) {
			if(wmap.has(removed)) {

				table.removeChild(wmap.get(removed));
				wmap.delete(removed)
			}	else console.warn(`Received remove signal for "${removed}" which is not in table`)
		}
	})
}




function clockWork(clock, calendar) {

	const current = new Date();
	const H = String(current.getHours()).padStart(2,"0");
	const M = String(current.getMinutes()).padStart(2,"0");
	const S = String(current.getSeconds()).padStart(2,"0");
	const U = current.getMilliseconds();

	clock.innerText = `${H}:${M}:${S}`;
	calendar.innerText = current.toDateString();

	setTimeout(clockWork, 1000 -U, clock, calendar)
}




function forgetWord(event /* Event */, word /* String */, ws /* WebSocket */) {

	event.preventDefault();

	try { ws.send(`forget:${word}`) }
	catch(E) { console.error(`Failed to forget ${word} due to ${E}`) }
}




function acceptWord(event /* Event */, word /* String */, ws /* WebSocket */) {

	event.preventDefault();

	try { ws.send(`accept:${word}`) }
	catch(E) { console.error(`Failed to accept ${word} due to ${E}`) }
}




function removeWord(event /* Event */, word /* String */, ws /* WebSocket */) {

	event.preventDefault();

	try { ws.send(`remove:${word}`) }
	catch(E) { console.error(`Failed to remove ${word} due to ${E}`) }
}







