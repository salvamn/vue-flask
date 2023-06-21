<template>


    <div id="contenedor_todo">

        <div id="contenido_top">
            <crearTarea/>
        </div>
        



        <div id="contenido_bottom">

            <div id="contenedor_recorrido_for">
              <listaTarea />
            </div>
           
        </div>


    </div>





</template>



<script>
import crearTarea from '../components/Panel Todo - Componentes/crearTareaComponent.vue'
import listaTarea from '../components/Panel Todo - Componentes/listaTareaComponent.vue'



export default {
  components: {
    crearTarea,
    listaTarea,
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
    flex-direction: column;
    background: rgba(0, 0, 0, 0.123);
}

#contenido_top{
    width: 80%;
    height: auto;
    /*background: red;*/
    display: flex;
    justify-content: flex-start;
    align-items: center;
    
}

#contenido_bottom{
    height: 40%;
    width: 80%;
    background: rgba(7, 7, 7, 0.548);
    display: flex;
    justify-content: center;
    align-items: center;
}


</style>