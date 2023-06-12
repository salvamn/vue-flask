<template>
    
    <div id ="app"> <!---Acá sera nuestra aplicación donde pondremos los componentes que mandan para mostrar-->


        <navSito/>



        <router-view /> <!---Esto se pone si osi , para tomar las rutas-->


    </div>




</template>





<script setup>

import navSito from './components/navSitoComponent.vue';



</script>





<style scoped>
@import url('@/assets/css/base.css');




</style>
