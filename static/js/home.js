document.getElementById("spinner");

async function requestServer(url, payload = { method: "GET" }) {
	try {
		let response = await fetch(url, payload);
		let data = await response.json();
		// console.log(data);
		return data;
	} catch (error) {
		console.error("error fetching data:", error);
	}
}

document.addEventListener("DOMContentLoaded",()=>{
	spinner.classList.add("d-none")
})

