







function initController() {

	clockWork(document.getElementById("clock"));

	const controllerState = new Set();
	const viewer = document.getElementById("viewer");
	const controller = document.getElementById("controller");
	const ws = new WebSocket(`ws://${location.host}/controller-ws-cast`);


	Array.prototype.forEach.call(

		controller.getElementsByClassName("controller-message"),
		div => {

			// slicing out -+ buttons from current "word"
			const word = div.innerText.slice(0,-2);
			controllerState.add(word);

			div
				.getElementsByClassName("remove-button")[0]
				.addEventListener("click",event => removeWord(event, controllerState, word));
			div
				.getElementsByClassName("accept-button")[0]
				.addEventListener("click",event => acceptWord(event, controllerState, word))
		}
	);


	ws.addEventListener("message",event => {

		const { view,control } = JSON.parse(event.data);

		if(typeof(view) !== "string") {

			console.error("Controller socket received invalid \"view\"");
			return
		}


		const messageBlock = document.createElement("pre");
		messageBlock.className = "viewer-message";
		messageBlock.innerText = view;

		viewer.insertBefore(messageBlock, viewer.getElementsByClassName("viewer-message")[0]);


		if(Array.isArray(control) && control.every(word => typeof(word) === "string")) {

			control.forEach(word => {
				if(!controllerState.has(word)) {

					const controlBlock = document.createElement("div");
					const removeButton = document.createElement("button");
					const acceptButton = document.createElement("button");

					controlBlock.className = "controller-message";
					removeButton.className = "remove-button";
					acceptButton.className = "accept-button";

					removeButton.innerText = "-";
					acceptButton.innerText = "+";

					removeButton.addEventListener("click",event => removeWord(event, controllerState, word));
					acceptButton.addEventListener("click",event => acceptWord(event, controllerState, word));

					controlBlock.appendChild(document.createTextNode(word));
					controlBlock.appendChild(removeButton);
					controlBlock.appendChild(acceptButton);

					controller.appendChild(controlBlock);
					controllerState.add(word)
				}
			})
		}	else console.error("Controller socket received invalid \"words\"")
	})
}




function initManager() {

	clockWork(document.getElementById("clock"));

	const table = document.getElementById("words-table");

	Array.prototype.forEach.call(

		document.getElementsByClassName("del-button"),
		button => button.addEventListener("click",event => {

			const word = event.target.parentNode.cells[1].innerText;
			if(confirm(`Delete "${word}"?`)) removeWord(event, word)
		})
	)
}




function clockWork(element) {

	const current = new Date();
	const H = String(current.getHours()).padStart(2,"0");
	const M = String(current.getMinutes()).padStart(2,"0");
	const S = String(current.getSeconds()).padStart(2,"0");
	const U = current.getMilliseconds();

	element.innerText = `${H}:${M}:${S}`;

	setTimeout(clockWork, 1000 -U, element)
}




function removeWord(event /* Event */, word /* String */) {

	event.preventDefault();
	fetch(

		"/controller-word-remove",
		{
			method:		"DELETE",
			headers:	{ "Content-Type": "application/json" },
			body:		JSON.stringify({ word })
		}
	)
	.then(response => {
		if(response.status !== 200)

			response.json()
			.then(({ reason }) => alert(reason))
			.catch(() => alert(`Uncaught response status: ${response.status}`))

		// only remove "word" from "state" in case of success query
		else event.target.parentNode.parentNode.removeChild(event.target.parentNode);
	})
	.catch(E => alert(E))
}




function acceptWord(event, state /* Set */, word /* String */) {

	event.preventDefault();
	fetch(

		"/controller-word-accept",
		{
			method:		"PUT",
			headers:	{ "Content-Type": "application/json" },
			body:		JSON.stringify({ word })
		}
	)
	.then(response => {
		if(response.status !== 200)

			response.json()
			.then(({ reason }) => alert(reason))
			.catch(() => alert(`Uncaught response status: ${response.status}`))

		else {

			event.target.parentNode.parentNode.removeChild(event.target.parentNode);
			state.delete(word) // only remove "word" from "state" in case of success query
		}
	})
	.catch(E => alert(E))
}







