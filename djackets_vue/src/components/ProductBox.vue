<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img :src="lp.get_thumbnail" alt="">
            </figure>
            <h3 class="is-size-4">{{lp.name}}</h3>
            <p class="is-size-6 has-text-grey">${{lp.price}}</p>
            <strong>{{lp.get_absolute_url}}</strong>
            <router-link :to="lp.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
        </div>
    </div>
</template>

<script>
    export default{
        name:'ProductBox',
        props:{//ProductBox componenti harada istifade olunursa burdaki propsda icinde gelecek ele
            lp:Object//cunki yuxarirdada lp dir,hemcinin diger componentlere bind ededed  :lp seklinde yazmlisan ProductBox componenti icinde tanimlayanda
        }
    }
</script>

<style scoped>
    .image{
        margin-top: -1.25rem;
        margin-left: -1.25rem;
        margin-right: -1.25rem;
    }
</style>