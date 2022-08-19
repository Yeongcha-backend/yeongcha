var btn = document.getElementsByClassName("btn");
var btn1 = document.getElementsByClassName("btn1");
var btn2 = document.getElementsByClassName("btn2");
var btn3 = document.getElementsByClassName("btn3");

function handleClick(event){
    console.log(event.target);

    console.log(event.target.classList);

    if(event.target.classList[1] === 'clicked'){
        event.target.classList.remove('clicked');
    } 
    else{
        event.target.classList.add('clicked');
    }
}

function init(){
    for (var i = 0; i < btn.length; i++) {
        btn[i].addEventListener("click", handleClick);
      }
}

function init1(){
    for (var i = 0; i < btn1.length; i++) {
        btn1[i].addEventListener("click", handleClick);
      }
}

function init2(){
    for (var i = 0; i < btn2.length; i++) {
        btn2[i].addEventListener("click", handleClick);
      }
}

function init3(){
    for (var i = 0; i < btn3.length; i++) {
        btn3[i].addEventListener("click", handleClick);
      }
}



init();
init1();
init2();
init3();