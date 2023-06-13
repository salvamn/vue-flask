<template>


  <div class="contenedor_resultados">

  <h2>Lista de publicaciones</h2>

  <div class="contenedor_recorrido_resultados" v-for="publicacion in publicaciones" :key="publicacion.id">

    {{ publicacion.texto }}


  </div>

</div>


</template>

  
<script>

import { mapState } from 'vuex';


export default {



  computed: {
    ...mapState(['publicaciones']),
  }






}


</script>
  


<style scoped>

.contenedor_resultados{
  width: 50%;

  
}
.contenedor_resultados h2 {
  background: white;
  color: black;
}

.contenedor_recorrido_resultados{
  background: white;
  color: black;
  display: flex;
  justify-content: center;
  align-items: center;
  
}


</style>