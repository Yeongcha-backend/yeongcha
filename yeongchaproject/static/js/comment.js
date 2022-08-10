const input = document.querySelector('.input');
const itemAdd = document.querySelector('.itemAdd');
const items = document.querySelector('.items');

const onAdd= () =>{
    const text= input.value;
    if(input.value === ''){
        input.focus();
        return;
    }
    
    const item= document.createElement('li');
    item.setAttribute('class', 'item');

    const itemText= document.createElement('span');
    itemText.setAttribute('class', 'itemText');
    itemText.innerHTML= text;
    
    const itemDel= document.createElement('button');
    itemDel.setAttribute('class', 'itemDel');
    itemDel.innerHTML= '삭제';
    itemDel.style.fontSize= '12px';
    itemDel.style.border= 'none';
    itemDel.style.color= 'rgba(136, 134, 134, 1)';
    itemDel.style.backgroundColor= 'white';
    itemDel.style.marginLeft= '700px';
    itemDel.addEventListener('click', () =>{
        items.removeChild(item);
    });

    item.appendChild(itemText);
    item.appendChild(itemDel);
    items.appendChild(item);
    input.value= '';
    input.focus();
};

itemAdd.addEventListener('click', ()=> {
    onAdd();
});

input.addEventListener('keypress', (event) =>{
    if(event.key === 'Enter'){
        onAdd();
    }
    return;
})

