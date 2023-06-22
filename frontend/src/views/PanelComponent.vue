<template>



    <div id="contenedor_todo">

        <div id="contenedor_top_panel">
            <crearTarea @tarea-creada="agregarTarea"/>
        </div>

  
   

        <div id="contenedor_bottom_panel">
            <listarTarea :tareas="tareas" @tarea-eliminada="eliminarTarea"/>
        </div>


    </div>




  </template>
  





  <script>


  import crearTarea from '@/components/Peticiones HTTP/CrearTareasComponent.vue';
  import listarTarea from '@/components/Peticiones HTTP/ListarTareasComponent.vue';
  import axios from 'axios';
  
  export default {
    components: {
      crearTarea,
      listarTarea,
    },
    data() {
      return {
        tareas: [],
      };
    },
    mounted() {
      this.leerTareas();
    },
    methods: {
       agregarTarea(tarea) {
        this.tareas.push(tarea);
      },
       eliminarTarea(id) {
        this.tareas = this.tareas.filter((tarea) => tarea.id !== id);
      },
      async leerTareas() {
        try {
          const response = await axios.post('http://localhost:5000/leer_tareas', { nombre_usuario: 'nombre_de_usuario' });
          this.tareas = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
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

#contenedor_top_panel{
    width: 100%;
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding-left: 20em;
}


#contenedor_bottom_panel{
    width: 100%;
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
}


</style>