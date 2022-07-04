<template>
        <tr>
            <td><router-link :to="item.product.get_absolute_url">{{item.product.name}}</router-link></td>
            <td>${{item.product.price}}</td>
            <td>
                {{item.quantity}}
                <a @click="decrementQuantity(item)">-</a>
                <a @click="incrementQuantity(item)">+</a>
            </td>
            <td>${{getItemTotal(item).toFixed(2)}}</td>
            <td><button class="delete" @click="removeFromCart(item)"></button></td>
        </tr>
</template> 

<script>
    export default{
        name:'CartItem',
        props:{
            initialItem:Object
        },
        data(){
            return{
                item:this.initialItem
            }
        },
        methods:{
            getItemTotal(item){
                return item.quantity * item.product.price
            },
            decrementQuantity(){
                this.item.quantity--
                if(item.quantity==0){
                    this.$emit('removeCart',item)
                }
                this.updateCart()
            },
            incrementQuantity(){
                this.item.quantity++
                this.updateCart() 
            },
            updateCart(){
                window.localStorage.setItem('cart',JSON.stringify(this.$store.state.cart))
            },
            removeFromCart(item){
                this.$emit('removeCart',item)
                this.updateCart()
            }
        }
    }
</script>

<style>

</style>