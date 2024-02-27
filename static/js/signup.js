
let eyeOpenIcon = document.getElementById("eyeOpenIcon");
let eyeCloseIcon = document.getElementById("eyecloseIcon");
let passwordEl = document.getElementById("password");

eyeOpenIcon.onclick = ()=>{
    eyeCloseIcon.classList.remove("d-none")
    eyeOpenIcon.classList.add("d-none");
    passwordEl.type = "text";

}
eyeCloseIcon.onclick = () => {
	eyeOpenIcon.classList.remove("d-none");
	eyeCloseIcon.classList.add("d-none");
    passwordEl.type = "password";
};



