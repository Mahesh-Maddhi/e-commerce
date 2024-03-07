let spinner = document.getElementById("spinner");
let categoryCardEl = document.getElementById("categoryCard");
let searchIconEl = document.getElementById("searchIcon");
let searchBarEl = document.getElementById("searchBar");
let searchInputEl = document.getElementById("search-input");
let searchBtnEl = document.getElementById("searchBtn");
let closeBtnEl = document.getElementById("closeBtn");



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
	searchBarEl.classList.toggle("d-none");
	searchInputEl.focus();

});
closeBtnEl.onclick = ()=>{
	searchBarEl.classList.toggle("d-none");
	console.log("close clicked")
}
searchBarEl.addEventListener("keydown", (event) => {

	if (event.key === "Enter"){
		searchBarEl.classList.toggle("d-none");
		searchBtnEl.click()
		console.log("form-submitted")
	}
	
});

function closeModel(){
	document.getElementById("staticBackdrop").classList.remove("d-block","show")
	

}
