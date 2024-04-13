


let links = document.querySelectorAll('#account-sections a');

links.forEach((link)=> {
    link.addEventListener('click',  () =>{
        links.forEach( (otherLink)=> {
            otherLink.classList.remove('active');
        });
        link.classList.add('active');
    });
});

