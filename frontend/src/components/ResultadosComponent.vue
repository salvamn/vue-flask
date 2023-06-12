<template>




  <h2>Lista de publicaciones</h2>

  <div v-for="publicacion in publicaciones" :key="publicacion.id">

    {{ publicacion.texto }}



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
  