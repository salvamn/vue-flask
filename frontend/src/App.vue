<template>
    
    <div id ="app"> <!---Acá sera nuestra aplicación donde pondremos los componentes que mandan para mostrar-->


        <navSito/>

        <transition name="fade" mode="out-in">
            <router-view/> <!---Esto se pone si osi , para tomar las rutas-->
        </transition>   

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


.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

</style>
