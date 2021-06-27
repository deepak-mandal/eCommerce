console.log("Hello world in the console")

//adding event listener
var updateBtns = document.getElementsByClassName("update-cart")

for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener("click", function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log("productId: ", productId, "action: ", action)

    console.log('USER: ', user)
    if(user === 'AnonymousUser'){
        console.log('Not logged in')
    }
    else{
        updateUserOrder(productId, action)
    }

    })
}



function updateUserOrder(productId, action){
    console.log('User id logged in, sending data..')


    //featch API
    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        //passing the data
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({'productId':productId, 'action':action})
    })
    //getting response
    .then((response) =>{
        return response.json()
    })
    //getting output at console
    .then((data) =>{
        console.log('data: ', data)
    })
}