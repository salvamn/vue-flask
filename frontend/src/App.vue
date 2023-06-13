<template>
    
    <div id ="app"> <!---Acá sera nuestra aplicación donde pondremos los componentes que mandan para mostrar-->


        <navSito/>


        <router-view /> <!---Esto se pone si osi , para tomar las rutas-->


        <footerSito/>




    </div>




</template>





<script setup>
import footerSito from './components/footerComponent.vue'
import navSito from './components/navSitoComponent.vue';



</script>





<style scoped>
@import url('@/assets/css/base.css');




</style>
