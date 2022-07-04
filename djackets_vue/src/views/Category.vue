<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">
                    {{category.name}}
                </h2>
            </div>
            <!-- !ProductBox Component -->
            <app-product-box v-for="product in category.products" :key="product.id" :lp="product"></app-product-box>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'
    import ProductBoxVue from '../components/ProductBox.vue'

    export default{
        name:'Category',
        data(){
            return{
                category:{
                    products:[]
                }
            }
        },
        components:{
            'app-product-box':ProductBoxVue
        },
        watch:{
            $route(to,from,next){
                if(to.name=='Category'){
                    this.getCategory()
                }
            }
        },
        methods:{
            async getCategory(){
                const categorySlug = this.$route.params.category_slug
                console.log('Category Slug', categorySlug)
                
                this.$store.commit('setIsLoading',true)
                await axios.get(`api/v1/products/${categorySlug}/`)
                    .then((response)=>{
                        this.category = response.data
                        console.log('Category Value',this.category);
                        window.document.title = this.category.name + '| Djackets'
                    })
                    .catch((err)=>{
                        console.log(err)
                        toast({
                            message:'Someting went wrong.Pleasse try again',
                            type:'is-danger',
                            dismissible:true,
                            pauseOnHover:true,
                            duration:2000,
                            position:'bottom-right',
                        })
                    })
                this.$store.commit('setIsLoading',false)
            }
        },
        mounted(){
            this.getCategory()
        }
    }
</script>

<style>

</style>