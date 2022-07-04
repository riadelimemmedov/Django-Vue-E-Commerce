<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign Up</h1>
                <form @submit.prevent="signUp">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input @blur="$v.username.$touch()" v-model="username" :class="{'input is-danger':$v.username.$error}" type="text" class="input" placeholder="Username">
                            <small v-if="$v.username.required.$invalid" class="has-text-info is-block" style="font-size:15px">Please enter username</small>
                            <small v-if="$v.username.minLength.$invalid" class="has-text-info is-block" style="font-size:15px">Username minimum length is 5 characters</small>
                            <small v-if="$v.username.maxLength.$invalid" class="has-text-info is-block" style="font-size:15px">Username maximum length is 10 characters</small>
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input @input="$v.password.touch()" v-model="password" type="password" class="input" placeholder="Password">
                            <small v-if="$v.password.required.$invalid" class="has-text-info is-block" style="font-size:15px">Please enter password</small>
                            <small v-if="$v.password.minLength.$invalid" class="has-text-info is-block" style="font-size:15px">Please input minumum {{$v.password.minLength.$params.min}} length for valid password</small>
                            <small v-if="$v.password.maxLength.$invalid" class="has-text-info is-block" style="font-size:15px">Please input minumum {{$v.password.maxLength.$params.max}} length for valid password</small>                            
                        </div>
                    </div>
                    <div class="field">
                        <label>Repeat Password</label>
                        <div class="control">
                            <input @input="$v.repassword.touch()" v-model="repassword" type="password" class="input" placeholder="Password">
                            <small v-if="$v.repassword.required.$invalid" class="has-text-info is-block" style="font-size:15px">Please enter password</small>
                            <small v-if="$v.repassword.minLength.$invalid" class="has-text-info is-block" style="font-size:15px">Please input minumum {{$v.repassword.minLength.$params.min}} length for valid password</small>
                            <small v-if="$v.repassword.maxLength.$invalid" class="has-text-info is-block" style="font-size:15px">Please input minumum {{$v.repassword.maxLength.$params.max}} length for valid password</small>                            
                            <small v-if="$v.repassword.sameAs.$invalid" class="has-text-danger is-block" style="font-size:15px">Please same password</small>
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="(error,index) in errors" :key="index">{{error}}</p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button type="submit" class="button is-dark is-outlined">Sign Up</button>
                        </div>
                    </div>
                    <hr>
                    <router-link to="log-in/" class="has-text-link is-family-sans-serif">Click Here</router-link> to log in
                </form>
            </div>
        </div>
    </div>

    

</template>

<script>   
    import axios from 'axios'
    import {toast} from 'bulma-toast'
    import useVuelidate from '@vuelidate/core'
    import { required, email,minLength,maxLength,sameAs } from '@vuelidate/validators'

    export default{
        data(){
            return{
                username:'',
                password:'',
                repassword:'',
                errors:[]
            }
        },
        methods:{
            signUp(){
                if(this.username !=null && this.password !=null && this.repassword !=null){
                    const formData = {
                        username:this.username,
                        password:this.password
                    }
                    //Axios post reqeuest Back end
                    axios.post('api/v1/users/',formData)
                        .then((response)=>{
                            toast({
                                message:'Account created,please log in',
                                type:'is-success',
                                dismissible:true,
                                pauseOnHover:true,
                                duration:2000,
                                position:'bottom-right',
                            })
                            this.$router.push('/login/')
                        })
                        .catch((err)=>{
                            if(err.response){//axios error
                                for(const property in err.response.data){
                                    this.errors.push(`${property}: ${err.response.data[property]}`)//key and value format to look like
                                }
                                console.log(JSON.stringify(err.response.data))
                            }
                            else if(err.message){//return backend value message
                                this.errors.push('Something went wrong.Please try again')
                                console.log(JSON.stringify(err))
                            }
                        })
                
                }        
            }
        },
        setup(){
            return {$v:useVuelidate()}
        },
        validations(){
            return{
                username:{
                    required,
                    minLength:minLength(5),
                    maxLength:maxLength(10)
                },
                password:{
                    required,
                    minLength:minLength(6),
                    maxLength:maxLength(12)
                },
                repassword:{
                    required,
                    minLength:minLength(6),
                    maxLength:maxLength(12),
                    sameAs:sameAs(this.password)
                }
            }
        },
        mounted(){
            window.document.title = 'Sign-Up | Djackets'
        }
    }
</script>

<style>

</style>