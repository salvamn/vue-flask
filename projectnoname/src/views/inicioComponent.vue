<template>

    <div id="contenedor_principal_inicio">


        <!--<span>Este es el inicio</span>--->



        <publicacion/>
        
       


    </div>


</template>





<script setup>   /* setup = Composition API */

import publicacion from '@/components/publicacionComponent.vue';





</script>







<style scoped>   /* scoped quiere decir que mapea los estilos que le pondremos en este componente */
#contenedor_principal_inicio{
    width: 100%;
    background: rgb(14, 13, 13);
    height: 93%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}



</style>