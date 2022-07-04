<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="title">My Account</div>
            </div>
            <div class="column is-12">
                <button class="button is-danger" @click="logOut()">Log Out</button>
            </div>
            
            <hr>

            <div class="column is-12">
                <h2 class="subtitle">My Orders</h2>
                <app-order-summary v-for="order in orders" :key="order.id" :order="order"></app-order-summary>
            </div>


        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import OrderSummary from '../components/OrderSummary.vue'

    export default{
        name:'MyAccount',
        data(){
            return{
                orders:[]
            }
        },
        methods:{
            logOut(){
                axios.defaults.headers.common["Authorization"] = ""
                window.localStorage.removeItem('token')
                window.localStorage.removeItem('username')
                window.localStorage.removeItem('userid')

                this.$store.commit('removeToken')
                this.$router.push('/')
            },
            async getMyOrders(){
                this.$store.commit('setIsLoading',true)
                await axios.get('api/v1/orders/')
                    .then((response)=>{
                        this.orders=response.data
                    })
                    .catch((err)=>{
                        console.log(err)
                    })
                this.$store.commit('setIsLoading',false)
            }
        },
        components:{
            'app-order-summary':OrderSummary
        },
        mounted(){
            window.document.title = 'My Account | Djackets'
            this.getMyOrders()
        }
    }
</script>


<style>

</style>