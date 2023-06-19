<template>


    <div id="contenedor_todo">


        <crearTarea/>

        <div>



        </div>





    </div>





</template>



<script>
import crearTarea from '../components/PeticionesHTTP/crearTareaComponent.vue'




export default {
  components: {
    crearTarea
    }
}





</script>




<style scoped>
#contenedor_todo {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}


#contenedor_todo>div {
    width: 80%;
    height: 80%;
    background: rgba(255, 255, 255, 0.096);
    padding: 20px;
}
</style>