







function initController() {

	clockWork(document.getElementById("clock"));

	const controllerState = new Set();
	const viewer = document.getElementById("viewer");
	const controller = document.getElementById("controller");
	const viewerWS = new WebSocket(`ws://${location.host}/viewer-ws-cast`);
	const controllerWS = new WebSocket(`ws://${location.host}/controller-ws-cast`);

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

	viewerWS.addEventListener("message",event => {

		messageBlock = document.createElement("pre");
		messageBlock.className = "viewer-message";
		messageBlock.innerText = `${event.data}`;

		viewer.insertBefore(messageBlock, viewer.getElementsByClassName("viewer-message")[0])
	});

	controllerWS.addEventListener("message",event => {

		const words = JSON.parse(event.data);

		if(!Array.isArray(words) || words.some(word => typeof(word) !== "string")) {

			console.error("Controller socket received invalid words");
			return
		}

		words.forEach(word => {

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
	})
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




function removeWord(event, state /* Set */, word /* String */) {

	event.preventDefault();
	fetch(

		"/controller-word-remove",
		{
			method:		"PUT",
			headers:	{ "Content-Type": "application/json" },
			body:		JSON.stringify({ word })
		}
	)
	.then(response => {

		if(response.status !== 200) response.json().then(({ reason }) => alert(reason));
		else {

			event.target.parentNode.parentNode.removeChild(event.target.parentNode);
			state.delete(word) // only remove "word" from "state" in case of success query
		}
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

		if(response.status !== 200) response.json().then(({ reason }) => alert(reason));
		else {

			event.target.parentNode.parentNode.removeChild(event.target.parentNode);
			state.delete(word) // only remove "word" from "state" in case of success query
		}
	})
	.catch(E => alert(E))
}







