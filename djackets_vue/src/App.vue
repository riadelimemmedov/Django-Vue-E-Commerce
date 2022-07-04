<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
        <!-- !Navbar Brand -->
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item"><strong>Djackets</strong></router-link>
          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <!-- !Navbar Menu -->
        <div class="navbar-menu" id="navbar-menu" :class="{'is-active':showMobileMenu}">
          <div class="navbar-start">
            <div class="navbar-item">
              <form method="GET" action="/search">
                <div class="field has-addons">
                  <div class="control">
                    <input type="text" name="product_name" class="input" placeholder="What are you looking for?">
                  </div>
                  <div class="control">
                    <button type="submit" class="button is-success">
                      <span class="icon"></span>
                      <i class="fas fa-search"></i>
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
          
          <div class="navbar-end">
            <router-link :to="{name:'Category',params:{category_slug:'summer'}}" class="navbar-item">Summer</router-link>
            <router-link to="/winter" class="navbar-item">Winter</router-link>
            <div class="navbar-item">
              <div class="buttons">

                <template v-if="$store.state.isAuthenticated">
                  <router-link to="/myaccount/" class="button is-light">Logut</router-link>
                </template>
                <template v-else>
                  <router-link to="/sign-up/" class="button is-light">Sign Up</router-link>
                  <router-link to="/login/" class="button is-light">Login</router-link>
                </template>

                
                <router-link to="/cart" class="button is-success">
                  <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                  <span>Cart ({{cartTotalLength}})</span>
                </router-link>
              </div>
            </div>
          </div>
        </div>
    </nav>

    <!-- !Loading Bar -->
    <div class="is-loading-bar has-text-centered" :class="{'is-loading':$store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <!-- !Router-View -->
    <div class="section">
      <router-view/>
    </div>
    <!-- !Footer -->
    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>
  </div>
</template>

<script>
  import axios from 'axios'

  export default{
    data(){
      return{
        showMobileMenu:false,
        cart:{
          items:[]
        }
      }
    },
    beforeCreate(){//when opened app.vue page beforeCreate immediatily working
      this.$store.commit('initializeStorage')//called when open thi page  

      const token = this.$store.state.token
      
      if(token){
        axios.defaults.headers.common['Authorization']="Token " + token
      }
      else{
        axios.defaults.headers.common['Authorization']=""
      }
    },
    mounted(){
      this.cart = this.$store.state.cart
    },
    computed:{
      cartTotalLength(){
        let totalLength = 0
        for(let i=0;i<this.cart.items.length;i++){
          totalLength += this.cart.items[i].quantity
        }
        return totalLength
      }
    },
    methos:{
      
    }

  }
</script>

<style lang="scss">
  @import '../node_modules/bulma';
    .lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
  }
  .lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color: #ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite;
  }
  @keyframes lds-dual-ring {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  .is-loading-bar {
    height: 0;
    overflow: hidden;
    -webkit-transition: all 0.3s;
    transition: all 0.3s;
    &.is-loading {
      height: 80px;
    }
  }
</style>
