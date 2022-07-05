const updateBtn = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        let itemId = this.dataset.item
        let action = this.dataset.action
        console.log('itemId:', itemId, 'action:', action)
        addCookie(itemId, action)
    })
}

function addCookie(itemId, action){
     if(action == 'add'){
        if(cart[itemId] == undefined){
            cart[itemId] = {'quantity': 1}
        }else{
            cart[itemId]['quantity']++
        }
     }
     console.log('Cart:', cart)
     document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
}