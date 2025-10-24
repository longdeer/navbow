








function initController() {

	console.log("initiated!");

	const header = document.getElementsByTagName("header")[0];
	clock(header);

	const viewer = document.getElementById("viewer");
	const controller = document.getElementById("controller");

	const viewerWS = new WebSocket(`ws://${location.host}/viewer-ws-cast`);
	viewerWS.addEventListener("open",event => console.log("opened"));
	viewerWS.addEventListener("message",event => {

		messageBlock = document.createElement("pre");
		messageBlock.className = "viewer-message";
		messageBlock.innerText = event.data;

		viewer.appendChild(messageBlock);
		viewer.scrollTo(0, viewer.scrollHeight)
	});

	const controllerWS = new WebSocket(`ws://${location.host}/controller-ws-cast`);
	controllerWS.addEventListener("open",event => console.log("opened"));
	controllerWS.addEventListener("message",event => {

		messageBlock = document.createElement("pre");
		messageBlock.className = "controller-message";
		messageBlock.innerText = event.data;

		controller.appendChild(messageBlock);
		controller.scrollTo(0, controller.scrollHeight)
	});
}
function clock(element) {

	const current = new Date();
	const H = String(current.getHours()).padStart(2,"0");
	const M = String(current.getMinutes()).padStart(2,"0");
	const S = String(current.getSeconds()).padStart(2,"0");
	element.innerText = `${H}:${M}:${S}`;
	setTimeout(clock, 1000, element)
}







