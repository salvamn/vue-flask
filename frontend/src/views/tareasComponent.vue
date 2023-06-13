<template>




    <section id="contenedor_conjunto">



        <div id="contenedor_top_tareas">

            <publicacion />

        </div>




        <div id="contenedor_top_bottom">

            <div id="contenedor_top_bottom_interno">

                <router-link to="/"></router-link>
            </div>

        </div>



    </section>



</template>






<script setup>

import publicacion from '@/components/publicacionComponent.vue';



</script>






<style scoped>
#contenedor_conjunto {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

#contenedor_top_tareas {
    width: 100%;
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>