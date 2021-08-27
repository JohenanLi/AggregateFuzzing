<template>
    <router-view v-if="isRouterAlive"></router-view>
</template>

<script>
export default {
    name:'app',
    provide(){
        return{
            reload:this.reload
        }
    },
    data(){
        return{
            isRouterAlive:true
        }
    },
    methods:{
        reload(){
            this.isRouterAlive = false
            this.$nextTick(function(){
                this.isRouterAlive = true
            })
        }
    }
};
</script>

<style>
@import "./assets/css/main.css";
@import "./assets/css/color-dark.css";
</style>
