<template>
    <section id="contenedor_conjunto">

        <div id="contenedor_top_tareas">

            <!--<publicacion/>-->

        </div>


        <div id="contenedor_top_bottom">

          
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

    </section>
</template>






<script>
//import publicacion from '@/components/publicacionComponent.vue';
import { useStore } from 'vuex';
import {ref} from 'vue'





export default {
  setup() {

    const store = useStore();
    const nombre = ref('');
    const correo = ref('');
    const nombre_usuario = ref('');
    const contrasenia = ref('');

    const crearUsuario = () => {
      const usuario = {
        nombre: nombre.value,
        correo: correo.value,
        nombre_usuario: nombre_usuario.value,
        contrasenia: contrasenia.value
      }

    
      store.dispatch('crearUsuario', usuario)
      .then(respuesta => {
        console.log('usuario creado:', respuesta)
      })
      .catch(error => {
        console.error('error al crear el usaurio',error)
      })


    }

    return {
      nombre,
      correo,
      nombre_usuario,
      contrasenia,
      crearUsuario

    };
  }
}
</script>






<style scoped>
#contenedor_top_bottom{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background: red;
}
form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    color: black;
}
form input{
    color: black;
}
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