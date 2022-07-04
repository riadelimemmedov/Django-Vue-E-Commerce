<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
          <p class="title mb-6">
              Welcome to Djacket
          </p>
          <p class="subtitle">
              The best jacket store online
          </p>
      </div>
    </section>

      <div class="columns is-multiline">
        <div class="column is-12">
            <h2 class="is-size-2 has-text-centered">Latest products</h2>
        </div>
        <!-- !ProductBox Component -->
        <app-product-box v-for="product in  latestProducts" :key="product.id" :lp="product"></app-product-box>
      </div>

  </div>
</template>

<script>
  import axios from 'axios'
  import ProductBox from '../components/ProductBox.vue'

  export default {
    name: 'HomeView',
    data(){
      return{
        latestProducts:[]
      }
    },
    components: {
      'app-product-box':ProductBox
    },
    methods:{
      async getLatestProducts(){
        this.$store.commit('setIsLoading',true)
        await axios.get('api/v1/latest-products/')
          .then((response)=>{
            console.log(response.data)
            this.latestProducts = response.data
          })
          .catch((err)=>{
            console.log('Error request home components')
            console.log(err)
          })
        this.$store.commit('setIsLoading',false)
      }
    },
    created(){
      this.getLatestProducts()
      window.document.title = 'Home | Djackets'
    }
}
</script>
