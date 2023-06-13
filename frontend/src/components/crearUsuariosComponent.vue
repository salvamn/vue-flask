<template>





  <section id="contenedor_conjunto">

    <div id="contenido_top">

      <form @submit.prevent="crearUsuario">

        <label for="nombre">nombre</label>
        <input type="text" v-model="nombre" id="nombre">
        <label for="email">email</label>
        <input type="text" v-model="correo" id="email">
        <label for="email">nombre_usuario</label>
        <input type="text" v-model="nombre_usuario" id="email">
        <label for="email">contraseña</label>
        <input type="text" v-model="contrasenia" id="email">
        <button type="submit">crear usuario</button>

      </form>

    </div>


    <div id="contenido_bottom">
      <span>asd</span>
    </div>


  </section>






</template>






<script setup>


import { ref } from 'vue'
import { useStore } from 'vuex';

const store = useStore();

const nombre = ref ('');
const correo = ref ('');
const nombre_usuario = ref('');
const contrasenia = ref ('');


const crearUsuario = async () => {

  const usuario = {
    nombre: nombre.value,
    correo: correo.value,
    nombre_usuario: nombre_usuario.value,
    contrasenia: contrasenia.value
  };

  try {
    const respuesta = await store.dispatch('crearUsuario', usuario);
    console.log('Usuario creado:', respuesta);
  } catch (error) {
    console.error('error al crear el usaurio:', error);
   
  }


};


</script>






<style scoped>
#contenedor_conjunto {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: rgba(0, 0, 0, 0.514);
}


#contenido_top {
  /*background: red;*/
  width: 70%;
  height: 60%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 20px;
}

#contenido_bottom {
  width: 70%;
  height: 40%;
  /*background: green;*/
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  color: black;
}

form label{
  margin-top: 10px;
}

form input {
  color: black;
  padding: 10px;
  border-radius: 5px;
  outline: 0;
  border: 0;

}

form button {
  color: black;
  margin-top: 15px;
  padding: 7px;

}
</style>