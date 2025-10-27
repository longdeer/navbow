








function initController() {

	const clock = document.getElementById("clock");
	document.getElementById("clock-size-increment")
	.addEventListener("click",event => clock.style.fontSize = Math.min(parseInt(getComputedStyle(clock)["font-size"].substring(0,3)) +1,250) + "px");
	document.getElementById("clock-size-decrement")
	.addEventListener("click",event => clock.style.fontSize = Math.max(parseInt(getComputedStyle(clock)["font-size"].substring(0,3)) -1,100) + "px");
	clockWork(clock);

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

			removeButton.innerText = "X";
			acceptButton.innerText = "V";

			// controlBlock.innerText = word;

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







