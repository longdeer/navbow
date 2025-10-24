








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

		messageBlock = document.createElement("pre");
		messageBlock.className = "controller-message";
		messageBlock.innerText = event.data;

		controller.appendChild(messageBlock);
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







