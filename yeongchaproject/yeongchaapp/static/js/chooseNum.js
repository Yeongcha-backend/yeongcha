var gak = document.getElementsByClassName('gak');

function handleClick(event){
    console.log(event.target);

    console.log(event.target.classList);

    if(event.target.classList[1] === 'clicked'){
        event.target.classList.remove('clicked');
    } else{
        for(var i= 0; i<gak.length; i++){
            gak[i].classList.remove('clicked');
        }

        event.target.classList.add('clicked');
    }
}

function init(){
    for (var i = 0; i < gak.length; i++) {
        gak[i].addEventListener("click", handleClick);
      }
}

init();