<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>
                <h2 class="is-size-5 has-text-grey">Search term : {{query}}</h2>
            </div>
            <!-- !ProductBox Component -->
            <app-product-box v-for="product in products" :key="product.id" :lp="product"></app-product-box>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import ProductBox from '../components/ProductBox.vue'

    export default{
        name:'Search',
        data(){
            return{
                products:[],
                query:''
            }
        },
        components:{
            'app-product-box':ProductBox,
        },
        mounted(){//after request
            window.document.title = 'Search | Djackets'

            let url = window.location.search.substring(1)
            let params = new URLSearchParams(url)
            console.log('Url value', url)
            console.log('Params', params)
            
            if(params.get('product_name')){//return value according given key
                this.query = params.get('product_name')
                this.performSearch()
            }
        },
        methods:{
            async performSearch(){
                this.$store.commit('setIsLoading',true)
                console.log('Query value', this.query)
                await axios.post('api/v1/products_djackets/search/',{'product_name':this.query})
                    .then((response)=>{
                        this.products = response.data
                    })
                    .catch((err)=>{
                        console.log(err)
                    })
                this.$store.commit('setIsLoading',false)
            }
        }
    }
</script>

<style>

</style>