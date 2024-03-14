





function increment(productId) {
	var quantityInput = document.getElementById("quantity_" + productId);
	quantityInput.value = parseInt(quantityInput.value) + 1;
}

function decrement(productId) {
	var quantityInput = document.getElementById("quantity_" + productId);
	var newValue = parseInt(quantityInput.value) - 1;
	if (newValue >= 1) {
		quantityInput.value = newValue;
	}
}

 function preventEnterSubmit(event) {
		if (event.key === "Enter") {
			event.preventDefault(); 
		}
 }