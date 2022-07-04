<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>
                <form @submit.prevent="logIn">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username" placeholder="Username">
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password" placeholder="Password" >
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="(error,index) in errors" :key="index">{{error}}</p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Log In</button>
                        </div>
                    </div>
                    <hr>
                    Or <router-link to="/sign-up/"></router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'


    export default{
        name:'Login',
        data(){
            return{
                username:'',
                password:'',
                errors:[]
            }
        },
        methods:{
            async logIn(){
                axios.defaults.headers.common['Authorization']=''
                window.localStorage.removeItem('token')
                
                const formData = {
                    username:this.username,
                    password:this.password
                }

                await axios.post('api/v1/token/login',formData)
                    .then((response)=>{
                        const token = response.data.auth_token

                        this.$store.commit('setToken',token)
                        axios.defaults.headers.common['Authorization']="Token " + token
                        window.localStorage.setItem('token',token)

                        //const toPath = this.$router.query.to || '/cart'

                        this.$router.replace('/cart')
                    })
                    .catch((err)=>{
                        if(err.response){
                            for(const property in err.response.data){
                                this.errors.push(`${property}: ${err.response.data[property]}`)
                            }
                        }
                        else{
                            this.errors.push('Something went wrong.Please try again')
                            console.log(JSON.stringify(err))
                        }
                    })
            }
        },
        mounted(){
            window.document.title = 'Logo In | Djackets'
        }
    }
</script>

<style>

</style>