





function increment(productId) {
	var quantityInput = document.getElementById("quantity_" + productId);
	let quantity =  parseInt(quantityInput.value) +1
	quantityInput.value = quantity;
}

function decrement(productId) {
	var quantityInput = document.getElementById("quantity_" + productId);
	let quantity = parseInt(quantityInput.value);

	if (quantity > 1) {
		quantity -= 1;
		quantityInput.value = quantity;
	}
	
}

 function preventEnterSubmit(event) {
		if (event.key === "Enter") {
			event.preventDefault(); 
		}
 }