<template>

      <div id="contenedor_tablas">

        <div id="contenido_top_header">

          <div id="campos">titulo</div>
          <div id="campos">descripcion</div>
          <div id="campos">prioridad</div>
          <div id="campos">nombre de usuario</div>
          <div id="campos">acciones</div>

        </div>

        <div id="contenido_top_resultados" v-for="tarea in tareas" :key="tarea.id">
          <div id="campos">{{ tarea.titulo }}</div>
          <div id="campos">{{ tarea.descripcion }}</div>
          <div id="campos">{{ tarea.prioridad }}</div>
          <div id="campos">{{ tarea.nombre_usuario }}</div>
          <div id="campos">
            <eliminarTarea :tarea="tarea" @tarea-eliminada="eliminarTarea"/>
          </div>

        </div>

        
      </div>


  </template>
  
  <script>

  import eliminarTarea from '@/components/Peticiones HTTP/EliminarTareasComponent.vue';
  import axios from 'axios';
  
  export default {
    props: ['tareas'],
    components: {
      eliminarTarea,
    },
    methods: {
      async eliminarTarea(id) {
        try {
          const response = await axios.post('http://localhost:5000/eliminar_tarea', { id });
          if (response.data.tarea) {
            this.$emit('tarea-eliminada', id);
          }
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
  </script>
  









<style scoped>


#contenedor_tablas {
    width: 50%;
    display: flex;
    flex-direction: column;
}

#contenido_top_header {
    display: flex;
    flex-direction: row;
    background-color: rgba(211, 211, 211, 0.288);
    font-weight: bold;
}

#contenido_top_resultados{
    display: flex;
    flex-direction: row;
    background-color: rgba(14, 13, 13, 0);
    font-weight: bold;
}
#campos{
    flex-basis: calc(100% / 6);
    padding: 8px;
    text-align: center;
}



</style>