








function initController() {

	clockWork(document.getElementById("clock"));

	const viewer = document.getElementById("viewer");
	const controller = document.getElementById("controller");

	const viewerWS = new WebSocket(`ws://${location.host}/viewer-ws-cast`);
	viewerWS.addEventListener("message",event => {

		messageBlock = document.createElement("pre");
		messageBlock.className = "viewer-message";
		messageBlock.innerText = `${event.data}`;

		viewer.insertBefore(messageBlock, viewer.getElementsByClassName("viewer-message")[0])
	});

	const controllerWS = new WebSocket(`ws://${location.host}/controller-ws-cast`);
	controllerWS.addEventListener("message",event => {

		const words = JSON.parse(event.data);

		if(!Array.isArray(words) || words.some(word => typeof(word) !== "string")) {

			console.error("Controller socket received invalid words");
			return
		}

		words.forEach(word => {

			const controlBlock = document.createElement("div");
			const removeButton = document.createElement("button");
			const acceptButton = document.createElement("button");

			controlBlock.className = "controller-message";
			removeButton.className = "remove-button";
			acceptButton.className = "accept-button";

			removeButton.innerText = "-";
			acceptButton.innerText = "+";

			removeButton.addEventListener("click", removeWord);
			acceptButton.addEventListener("click", acceptWord);

			controlBlock.appendChild(document.createTextNode(word));
			controlBlock.appendChild(removeButton);
			controlBlock.appendChild(acceptButton);

			controller.appendChild(controlBlock)
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




function removeWord(event) {

	event.preventDefault();
	fetch(
		"/controller-word-remove",
		{
			method:		"PUT",
			headers:	{ "Content-Type": "application/json" },
			body:		JSON.stringify({ word: event.target.parentNode.innerText.slice(0,-2) })
		}
	)
	.then(response => {

		if(response.status !== 200) response.json().then(({ reason }) => alert(reason));
		else event.target.parentNode.parentNode.removeChild(event.target.parentNode)
	})
	.catch(E => alert(E))
}
function acceptWord(event) {

	event.preventDefault();
	fetch(
		"/controller-word-accept",
		{
			method:		"PUT",
			headers:	{ "Content-Type": "application/json" },
			body:		JSON.stringify({ word: event.target.parentNode.innerText.slice(0,-2) })
		}
	)
	.then(response => {

		if(response.status !== 200) response.json().then(({ reason }) => alert(reason));
		else event.target.parentNode.parentNode.removeChild(event.target.parentNode)
	})
	.catch(E => alert(E))
}







