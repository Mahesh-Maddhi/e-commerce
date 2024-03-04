let spinner = document.getElementById("spinner");
let categoryCardEl = document.getElementById("categoryCard");
let searchIconEl = document.getElementById("searchIcon");
let searchBarEl = document.getElementById("searchBar");



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

document.addEventListener("DOMContentLoaded", () => {spinner.classList.add("d-none");});

searchIconEl.addEventListener("click", () => {
	searchBarEl.classList.toggle("d-block");
	console.log("hello");
});

function closeModel(){
	document.getElementById("staticBackdrop").classList.remove("d-block","show")
	

}
