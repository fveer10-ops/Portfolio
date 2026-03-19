// alert

if(document.getElementById("Alert")){
	window.alert("Welcome to my portfolio website!");
}



//Conditional

function greetingDisplay(){
	let hour = new Date().getHours();
	let greeting = document.getElementById("greets");

	if (hour < 12){
		greeting.innerText = "Good Morning! I'm Fatehveer Chahal.";
	}
	else if (hour < 18){
		greeting.innerText = "Good Afternoon! I'm Fatehveer Chahal.";
	}
	else {
		greeting.innerText = "Good Evening! I'm Fatehveer Chahal.";
	}
}
greetingDisplay();

function timeDisplay(){
	let timeNow = new Date();
	let timeShow = timeNow.toLocaleTimeString();
	document.getElementById("clock").innerHTML = timeShow;
	
}

setInterval(timeDisplay, 1000);
timeDisplay();



// color changer


function changeColor(theme){
	document.body.style.backgroundImage = "none";
	const navAndFooter = document.querySelectorAll('nav ul, footer');
	if (theme == "dark"){
		document.body.style.backgroundColor = "black";
		document.body.style.color = "white";
		navAndFooter.forEach(element => {
			element.style.backgroundColor = "grey";
		});
	}
	else if (theme == "light"){
		document.body.style.backgroundColor = "Lavender";
		document.body.style.color = "black";
		navAndFooter.forEach(element => {
			element.style.backgroundColor = "thistle";
		});
		
	}
	else{
		document.body.style.backgroundImage = "url(backgroundImage.jpg)";
		document.body.style.backgroundSize = "cover";
		document.body.style.backgroundArrachment = "fixed";
		document.body.style.color = "black";
		navAndFooter.forEach(element => {
			element.style.backgroundColor = "steelBlue";
		});
	}
}

function mouseOver(){
	let box = document.getElementById("interactive");
	box.innerHTML = "<b> Cybersecurity Focus: </b> Penetration Testing, Java Logic, and Network Security.";
	box.style.backgroundColor = "Red";
	box.style.color = "Blue";	
	box.style.border = "2px solid black";
}

function mouseOut(){
	let box = document.getElementById("interactive");
	box.innerHTML = "Hover your mouse over here";
	box.style.backgroundColor = "transparent";
	box.style.color = "red";
	box.style.border = "2px dashed red";
}
			