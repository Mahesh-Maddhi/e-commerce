let productImageEl = document.getElementById("product-image");
let ImageGalleryEl = document.getElementById("image-gallery");

ImageGalleryEl.addEventListener("click",(event)=>{
    let imageUrl = event.target.src;
    productImageEl.src = imageUrl;
    console.log(imageUrl);
})