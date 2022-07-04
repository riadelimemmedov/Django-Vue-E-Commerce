<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>
            </div>
            <div class="column is-12 box mt-2">
                <table class="table is-fullwidth" v-if="cartTotalLenght"><!-- !v-if="cartTotalLenght"-->
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                            <!-- !CartItem componennt here -->
                            <app-cart-item 
                                v-for="item in cart.items" 
                                :key="item.id" 
                                :initialItem="item"
                                @removeCart="removeCart"></app-cart-item>
                    </tbody>
                </table>
                <p v-else>You dont't have any products in your cart...</p>
            </div>
            <div class="column is-12 box">
                <h2 class="subtitle">Summary</h2>
                <strong>${{cartTotalPrice}}</strong>, {{cartTotalLenght}} items
                <hr>
                <router-link to="/checkout/" class="button is-dark">Proceed to checkout</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import CartItem from '../components/CartItem.vue'
    
    export default{
        name:'Cart',
        data(){
            return{
                cart:{
                    items:[]
                }
            }
        },
        methods:{
            removeCart(item){
                this.cart.items = this.cart.items.filter(i=>i.product.id!=item.product.id)
            }
        },
        components:{
            'app-cart-item':CartItem
        },
        mounted(){
            this.cart = this.$store.state.cart
        },
        computed:{//channge basa value vue instance
            cartTotalLenght(){
                return this.cart.items.reduce((acc,curVal)=>{
                    return acc+=curVal.quantity
                },0)
            },
            cartTotalPrice(){
                return this.cart.items.reduce((acc,curVal)=>{
                    return acc+=curVal.product.price*curVal.quantity
                },0)
            }
        }
    }
</script>

<style>

</style>