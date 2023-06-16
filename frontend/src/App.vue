<template>
    
    <div id ="app"> <!---Acá sera nuestra aplicación donde pondremos los componentes que mandan para mostrar-->


        <navSito/>

        <router-view/> <!---Esto se pone si osi , para tomar las rutas-->


        <footerSito/>




    </div>




</template>





<script>
import navSito from '@/components/navSitoComponent.vue';

import footerSito from '@/components/footerComponent.vue';

export default {
    components: {
        navSito,
        footerSito
    }
}


</script>





<style>
@import url('@/assets/css/base.css');




</style>
