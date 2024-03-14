
let categoryCardEl = document.getElementById("categoryCard");
let searchIconEl = document.getElementById("searchIcon");
let searchBarEl = document.getElementById("searchBar");
let searchInputEl = document.getElementById("search-input");
let searchBtnEl = document.getElementById("searchBtn");
let closeBtnEl = document.getElementById("closeBtn");


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
