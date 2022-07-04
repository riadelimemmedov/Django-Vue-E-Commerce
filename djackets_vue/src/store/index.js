import { createStore } from 'vuex'

export default createStore({
  state: {
      cart:{
        items:[]
      },
      isAuthenticated:false,
      token:'',
      isLoading:false
  },
  getters: {
  },
  mutations: {
    initializeStorage(state){//when startted project work this initializeStorage functio work
      //create cart localstorage object
      if(window.localStorage.getItem('cart')){//if cart already exists localstorage get cart data
        state.cart = JSON.parse(window.localStorage.getItem('cart'))
      }
      else{//if not exists
        window.localStorage.setItem('cart',JSON.stringify(state.cart))
      }

      //!For login authentication token
      if(window.localStorage.getItem('token')){
        state.token = window.localStorage.getItem('token')
        state.isAuthenticated=true
      }
      else{//if not token
        state.token=''
        state.isAuthenticated=false
      }
    },
    addToCart(state,item){
      const exists = state.cart.items.filter((i=>i.product.id===item.product.id))//if already exists product in advanced cart
      if(exists.length>0){//if before have this product in cart
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }
      else{
        state.cart.items.push(item)
      }
      //updated localstorage
      window.localStorage.setItem('cart',JSON.stringify(state.cart))
    },
    setIsLoading(state,status){
      state.isLoading = status
    },
    setToken(state,token){//when user logged in token value state.token value equal token loggen in token value
      state.token=token
      state.isAuthenticated=true
    },
    removeToken(state){
      state.token=''
      state.isAuthenticated=false
    },
    clearCart(state){
      state.cart = {items:[]}
      window.localStorage.setItem('cart',JSON.stringify(state.cart))
    }
  },
  actions: {
  },
  modules: {
  }
})
