





function increment(productId) {
	var quantityInput = document.getElementById("quantity_" + productId);
	var priceInput = document.getElementById("price_" + productId); 
	var pricePerUnitEl = document.getElementById("pricePerItem_" + productId); 
	var pricePerUnit = parseInt(pricePerUnitEl.textContent)
	let quantity =  parseInt(quantityInput.value) +1
	quantityInput.value = quantity;
	priceInput.textContent = quantity * pricePerUnit;
}

function decrement(productId) {
	var quantityInput = document.getElementById("quantity_" + productId);
	var priceInput = document.getElementById("price_" + productId);
	let quantity = parseInt(quantityInput.value);
	var pricePerUnitEl = document.getElementById("pricePerItem_" + productId);
	var pricePerUnit = parseInt(pricePerUnitEl.textContent);
	if (quantity > 1) {
		quantity -= 1;
		quantityInput.value = quantity;
		priceInput.textContent = quantity * pricePerUnit;
	}
	
	return false

}

 function preventEnterSubmit(event) {
		if (event.key === "Enter") {
			event.preventDefault(); 
		}
 }