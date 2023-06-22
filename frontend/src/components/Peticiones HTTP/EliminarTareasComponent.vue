<template>


    <button id="btn_eliminar" @click="eliminarTarea(tarea.id)">borrar tarea</button>


</template>
  



  <script>



  import axios from 'axios';
  
  export default {
    props: ['tarea'],
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
#btn_eliminar{
    padding: 10px;
    background: green;
    color: white;
}
</style>